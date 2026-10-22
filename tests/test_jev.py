"""Offline boundary tests for the portable Jev client."""
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

PATH = Path(__file__).resolve().parents[1] / 'skills/scout-skills/scripts/jev.py'
SPEC = importlib.util.spec_from_file_location('jev', PATH)
jev = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(jev)


def answer(value=0.9):
    return {'model': jev.MODEL, 'usage': {'input_tokens': 12, 'output_tokens': 2},
            'answers': {'useful': {'type': 'noul', 'noul': value}}}


class JevTests(unittest.TestCase):
    def invoke(self, args, responses=None, env=None):
        output, errors = io.StringIO(), io.StringIO()
        with patch.dict(os.environ, env or {}, clear=True), \
                patch.object(jev, 'ask', side_effect=responses) as call, \
                contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
            try:
                code = jev.main(args)
            except SystemExit as exc:
                code = exc.code
        return code, output.getvalue(), errors.getvalue(), call

    def test_dry_run_has_no_key_or_network_and_pins_model(self):
        code, output, _, call = self.invoke(['--state', 'focus rules', '--noul',
                                             'useful=Does this help?', '--dry-run'])
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(output)['model'], jev.MODEL)
        call.assert_not_called()

    def test_missing_key_is_actionable_and_does_not_send(self):
        code, output, errors, call = self.invoke(['--state', 'x', '--noul', 'useful=Useful?'])
        self.assertEqual((code, output), (2, ''))
        self.assertIn('TYPESAFE_API_KEY', errors)
        call.assert_not_called()

    def test_all_input_is_validated_before_network(self):
        for contents in ('', '[]\n', '{"id":1,"text":"ok"}\n{"id":2}\n',
                         '{"text":null}\n', '{"text":NaN}\n'):
            with self.subTest(contents=contents), tempfile.TemporaryDirectory() as folder:
                path = Path(folder) / 'items.jsonl'
                path.write_text(contents, encoding='utf-8')
                code, _, _, call = self.invoke(['--state-jsonl', str(path), '--field', 'text',
                                                '--noul', 'useful=Useful?'], env={'TYPESAFE_API_KEY': 'test'})
                self.assertEqual(code, 2)
                call.assert_not_called()

    def test_batch_preserves_failed_rows_ids_order_and_nonzero_status(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'items.jsonl'
            path.write_text('{"id":"a","text":"yes"}\n{"id":"b","text":"no"}\n', encoding='utf-8')
            code, output, _, _ = self.invoke(['--state-jsonl', str(path), '--field', 'text',
                                              '--workers', '1', '--noul', 'useful=Useful?'],
                                             responses=[answer(), RuntimeError('TypeSafe HTTP 503')],
                                             env={'TYPESAFE_API_KEY': 'test'})
        rows = [json.loads(line) for line in output.splitlines()]
        self.assertEqual(code, 1)
        self.assertEqual([row['_id'] for row in rows], ['a', 'b'])
        self.assertEqual(rows[0]['useful'], 0.9)
        self.assertIn('_error', rows[1])

    def test_malformed_response_fails_instead_of_empty_success(self):
        for response in ({}, {'model': jev.MODEL, 'answers': {}}, answer(float('nan')), answer(True)):
            with self.subTest(response=response):
                code, output, _, _ = self.invoke(['--state', 'x', '--noul', 'useful=Useful?'],
                                                  responses=[response], env={'TYPESAFE_API_KEY': 'test'})
                self.assertEqual(code, 1)
                self.assertIn('_error', json.loads(output))

    def test_choice_and_score_keep_uncertainty(self):
        questions = {'route': {'type': 'choice', 'criteria': {'local': 'code', 'agent': 'write'}},
                     'fit': {'type': 'score', 'criteria': ['no', 'yes']}}
        response = {'model': jev.MODEL, 'answers': {
            'route': {'type': 'choice', 'choice': 'local', 'confidence': 0.2,
                      'probabilities': {'local': 0.6, 'agent': 0.4}},
            'fit': {'type': 'score', 'score': 0.6, 'confidence': 0.2,
                    'probabilities': {'0': 0.4, '1': 0.6}, 'legend': {'0': 'no', '1': 'yes'}}}}
        row = jev.flatten(response, questions)
        self.assertEqual(row['route_confidence'], 0.2)
        self.assertEqual(row['fit_probabilities'], {'0': 0.4, '1': 0.6})
        response['answers']['route']['choice'] = 'unknown'
        with self.assertRaises(ValueError):
            jev.flatten(response, questions)

    def test_invalid_question_definitions_never_send(self):
        for flags in (['--choice', 'x=route'], ['--score', 'x=fit', '--level', 'one'],
                      ['--noul', '_id=bad'], ['--noul', 'x=one', '--noul', 'x=two'],
                      ['--workers', '0'], ['--option', 'a=b'], ['--noul', 'missing-equals']):
            with self.subTest(flags=flags):
                code, _, _, call = self.invoke(['--state', 'x'] + flags)
                self.assertEqual(code, 2)
                call.assert_not_called()

    def test_answer_metadata_cannot_be_overwritten_by_another_question(self):
        for name in ('route_confidence', 'route_probabilities'):
            for flags in (['--choice', 'route=Route?', '--noul', name + '=Useful?'],
                          ['--noul', name + '=Useful?', '--choice', 'route=Route?']):
                code, _, errors, call = self.invoke(['--state', 'x', '--option', 'a=one',
                                                     '--option', 'b=two'] + flags)
                self.assertEqual(code, 2)
                self.assertIn('collide', errors)
                call.assert_not_called()

    def test_complete_bundle_runs_after_copy_without_library_or_credentials(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder) / 'project' / '.agents' / 'skills' / 'scout-skills'
            shutil.copytree(PATH.parents[1], destination, ignore=shutil.ignore_patterns('__pycache__'))
            self.assertTrue((destination / 'references/jev.md').is_file())
            result = subprocess.run([sys.executable, str(destination / 'scripts/jev.py'),
                                     '--state', 'example', '--noul', 'useful=Useful?', '--dry-run'],
                                    cwd=folder, env={k: v for k, v in os.environ.items()
                                                     if k not in ('TYPESAFE_API_KEY', 'JEV_MODEL')},
                                    text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)['state'], 'example')

    def test_transport_retry_and_authorization_header(self):
        response = io.StringIO(json.dumps(answer()))
        with patch.object(jev.urllib.request, 'urlopen', side_effect=[
                urllib.error.URLError('offline'), response]) as send, patch.object(jev.time, 'sleep'):
            self.assertEqual(jev.ask('test-key', {'state': 'x'}), answer())
        request = send.call_args.args[0]
        self.assertEqual(request.full_url, jev.API)
        self.assertEqual(request.get_header('Authorization'), 'Bearer test-key')

    def test_auth_failure_is_not_retried_or_echoed(self):
        error = urllib.error.HTTPError(jev.API, 401, 'secret-state', {}, io.BytesIO(b'private'))
        with patch.object(jev.urllib.request, 'urlopen', side_effect=error) as send:
            with self.assertRaisesRegex(RuntimeError, 'HTTP 401') as caught:
                jev.ask('test', {'state': 'private'})
        self.assertEqual(send.call_count, 1)
        self.assertNotIn('private', str(caught.exception))

    def test_retry_exhaustion_is_bounded(self):
        with patch.object(jev.urllib.request, 'urlopen', side_effect=urllib.error.URLError('offline')) as send, \
                patch.object(jev.time, 'sleep'):
            with self.assertRaisesRegex(RuntimeError, 'after 4 attempts'):
                jev.ask('test', {'state': 'x'})
        self.assertEqual(send.call_count, 4)


if __name__ == '__main__':
    unittest.main()
