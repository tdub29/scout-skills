#!/usr/bin/env python3
"""Optional TypeSafe Jev client. Stdlib only; credentials come from the environment."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import math
import os
from pathlib import Path
import sys
import time
import urllib.error
import urllib.request

API = 'https://api.typesafe.ai/v1/systemone'
MODEL = 'jev-1.13.0'


def positive(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError('must be at least 1')
    return number


def questions_from(args):
    questions = {}

    def add(spec, kind, criteria=None):
        name, sep, instruction = spec.partition('=')
        if not name.strip() or not sep or not instruction.strip():
            raise ValueError('questions must use name=instructions')
        if name.startswith('_') or name in questions:
            raise ValueError('question names must be unique and must not start with _')
        questions[name] = {'type': kind, 'instructions': instruction}
        if criteria is not None:
            questions[name]['criteria'] = criteria

    options = {}
    for spec in args.option:
        name, sep, description = spec.partition('=')
        if not name or not sep or not description or name in options:
            raise ValueError('options must be unique name=description pairs')
        options[name] = description
    if args.choice and not 2 <= len(options) <= 255:
        raise ValueError('--choice needs 2 to 255 --option pairs')
    if args.score and not 2 <= len(args.level) <= 10:
        raise ValueError('--score needs 2 to 10 ordered --level descriptions')
    if options and not args.choice or args.level and not args.score:
        raise ValueError('--option requires --choice; --level requires --score')
    for spec in args.noul:
        add(spec, 'noul')
    for spec in args.choice:
        add(spec, 'choice', options)
    for spec in args.score:
        add(spec, 'score', args.level)
    if not questions:
        raise ValueError('provide --noul, --choice or --score')
    output_keys = set()
    for name, question in questions.items():
        keys = {name}
        if question['type'] in ('choice', 'score'):
            keys.update((name + '_confidence', name + '_probabilities'))
        if question['type'] == 'score':
            keys.add(name + '_legend')
        if output_keys & keys:
            raise ValueError('question names collide with generated answer metadata')
        output_keys.update(keys)
    return questions


def load_items(args):
    if args.state is not None:
        if args.field:
            raise ValueError('--field requires --state-jsonl')
        return [(None, args.state)]
    items = []
    for number, line in enumerate(Path(args.state_jsonl).read_text(encoding='utf-8-sig').splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except ValueError as exc:
            raise ValueError(f'line {number}: invalid JSON') from exc
        if not isinstance(row, dict):
            raise ValueError(f'line {number}: expected a JSON object')
        if args.field and args.field not in row:
            raise ValueError(f'line {number}: missing field {args.field!r}')
        state = row[args.field] if args.field else row
        if not isinstance(state, (str, dict, list)):
            raise ValueError(f'line {number}: state must be text, an object or an array')
        items.append((row.get(args.id_field), state))
    if not items:
        raise ValueError('input batch is empty')
    return items


def ask(key, payload, attempts=4):
    data = json.dumps(payload, ensure_ascii=False, allow_nan=False).encode('utf-8')
    for attempt in range(attempts):
        request = urllib.request.Request(API, data=data, headers={
            'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            status = exc.code
            exc.close()
            if status not in (408, 429, 500, 502, 503, 504, 529):
                # Do not echo provider bodies: they can contain supplied private state.
                raise RuntimeError(f'TypeSafe HTTP {status}; check credentials or request') from None
            error = f'TypeSafe HTTP {status}'
        except (urllib.error.URLError, TimeoutError, OSError):
            error = 'TypeSafe transport error'
        if attempt + 1 < attempts:
            time.sleep(2 ** attempt)
    raise RuntimeError(error + f' after {attempts} attempts')


def probability(value):
    return (isinstance(value, (float, int)) and not isinstance(value, bool)
            and math.isfinite(value) and 0 <= value <= 1)


def flatten(response, questions):
    """Reject incomplete/mismatched answers instead of emitting false success."""
    answers = response.get('answers')
    if not isinstance(answers, dict) or set(answers) != set(questions):
        raise ValueError('response is missing requested answers or contains unexpected answers')
    if not isinstance(response.get('model'), str) or not response['model']:
        raise ValueError('response is missing its model ID')
    row = {'_model': response['model'], '_usage': response.get('usage', {})}
    for name, question in questions.items():
        answer = answers[name]
        kind = question['type']
        if not isinstance(answer, dict) or answer.get('type') != kind:
            raise ValueError(f'invalid answer type for {name}')
        value = answer.get(kind)
        if kind == 'noul':
            if not probability(value):
                raise ValueError(f'invalid noul for {name}')
        else:
            criteria = question['criteria']
            keys = set(criteria) if kind == 'choice' else {str(i) for i in range(len(criteria))}
            probabilities = answer.get('probabilities')
            if (not probability(answer.get('confidence')) or not isinstance(probabilities, dict)
                    or set(probabilities) != keys
                    or not all(probability(p) for p in probabilities.values())
                    or abs(sum(probabilities.values()) - 1) > 0.02):
                raise ValueError(f'invalid confidence/probabilities for {name}')
            if kind == 'choice' and (not isinstance(value, str) or value not in criteria):
                raise ValueError(f'unknown choice for {name}')
            if kind == 'score' and (not isinstance(value, (int, float)) or isinstance(value, bool)
                                    or not math.isfinite(value) or not 0 <= value <= len(criteria) - 1):
                raise ValueError(f'invalid score for {name}')
            row[name + '_confidence'] = answer['confidence']
            row[name + '_probabilities'] = probabilities
            if kind == 'score':
                row[name + '_legend'] = answer.get('legend', {})
        row[name] = value
    return row


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--state')
    source.add_argument('--state-jsonl')
    parser.add_argument('--field')
    parser.add_argument('--id-field', default='id')
    for flag in ('noul', 'choice', 'option', 'score', 'level'):
        parser.add_argument('--' + flag, action='append', default=[])
    parser.add_argument('--model', default=os.environ.get('JEV_MODEL') or MODEL)
    parser.add_argument('--workers', type=positive, default=4)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args(argv)
    try:
        questions = questions_from(args)
        items = load_items(args)
        # Validate the whole batch before sending any item. Never truncate evidence.
        json.dumps(items, allow_nan=False)
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    if args.dry_run:
        print(json.dumps({'model': args.model, 'state': items[0][1], 'questions': questions},
                         indent=2, ensure_ascii=False))
        print(f'[dry run] {len(items)} item(s); no network requests', file=sys.stderr)
        return 0
    key = os.environ.get('TYPESAFE_API_KEY', '').strip()
    if not key:
        print('Set TYPESAFE_API_KEY locally, or use --dry-run. Never paste a key into chat.', file=sys.stderr)
        return 2

    def work(item):
        identifier, state = item
        try:
            row = flatten(ask(key, {'model': args.model, 'state': state, 'questions': questions}), questions)
        except Exception as exc:
            # Exception text from parsing can contain supplied data; expose only known messages.
            detail = str(exc) if isinstance(exc, RuntimeError) else type(exc).__name__
            row = {'_model': args.model, '_usage': {}, '_error': detail}
        row['_id'] = identifier
        return row

    failed = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for row in pool.map(work, items):
            failed += int('_error' in row)
            print(json.dumps(row, ensure_ascii=False), flush=True)
    print(f'{len(items)} item(s), {failed} failed', file=sys.stderr)
    return 1 if failed else 0


if __name__ == '__main__':
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    sys.exit(main())
