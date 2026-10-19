#!/usr/bin/env python
"""Search the locally installed skills by WHAT THEY DO, not by name.

Why this exists. The in-context skill listing is truncated to bare names: the full
name+description listing measured 588,453 chars against a 40,000-char budget at 1M context
(14.7x over), so every description is dropped and skill selection runs on names alone. The
installed `find-skills` skill searches the skills.sh REGISTRY, so asking "is there a skill
for X" reaches for the internet while the answer sits on disk. This greps the disk, ranks
the hits, and says which of them can actually be invoked.

Python rather than PowerShell: the ranking is a handful of dict comprehensions here and a
page of ugly hashtable code in 5.1, and the whole workspace already runs shared tooling on
the plain `python` on PATH.

Usage:
    python .agents/scripts/find-local-skill.py "options volatility"
    python .agents/scripts/find-local-skill.py "browser automation" --top 8
    python .agents/scripts/find-local-skill.py "x" --json
    python .agents/scripts/find-local-skill.py --rebuild        # force a reindex
    python .agents/scripts/find-local-skill.py --selftest

Ranking is deliberately simple and explainable: term frequency over the description, a
boost when the term is in the skill NAME, a bigger boost for the whole phrase. No embedding
model, no API key, no new dependency.
"""

import argparse
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
HOME = os.path.expanduser('~')

# A skill in .agents/skills alone is a DESCRIPTION SOURCE, not a loaded tree: it cannot be
# called with the Skill tool. Only the last two are loaded, so only they make a skill invocable.
TREES = [
    ('.agents', os.path.join(ROOT, '.agents', 'skills'), False),
    ('.claude', os.path.join(ROOT, '.claude', 'skills'), True),
    ('~/.claude', os.path.join(HOME, '.claude', 'skills'), True),
    ('.cursor', os.path.join(ROOT, '.cursor', 'skills'), False),
    ('skills', os.path.join(ROOT, 'skills'), False),
]

CACHE = os.path.join(HERE, '.find-local-skill-cache.json')
# Function words and first/second-person filler, which must not score.
#
# Extended 2026-09-01, and the gap was not cosmetic. The original list handled keyword-style
# queries but not the way a person actually types a request: "review this react component for
# accessibility issues before we ship" ranked education-data-compliance and icml-reviewer above
# EVERY react and accessibility skill installed, on filler alone. The same query without its
# trailing five words returned react-doctor first. That matters more now that the ranker feeds
# an automatic hook on every prompt, where a confident wrong suggestion is worse than silence.
#
# Domain verbs stay scoreable on purpose (review, audit, build, ship, deploy, test, debug,
# design, check, plan) because each is the head noun of a real skill.
STOP = set("""a an the and or of for to in on with by from as is are be it this that at into your you
use used using when where what which who how why not no all any if then than
skill skills claude agent agents user users task tasks work working also can should must
i me my mine we us our ours am was were been being do does did doing done
need needs needed want wants would will shall may might could
help please let lets go get gets getting got make makes making made
before after here now again still just really very quite pretty
some many much more most other another such own same too enough
have has had having them they their there these those he she his her
about over under out up down off through while during between across
thing things stuff way ways bit lot lots kind sort etc
one two three first next last new old good bad better best
like unlike per via each every both either neither""".split())


def parse_frontmatter(path):
    """Return (name, description) from a SKILL.md, or (None, None). BOM-safe."""
    try:
        with io.open(path, encoding='utf-8-sig', errors='replace') as fh:
            head = fh.read(8192)
    except Exception:
        return None, None
    if not head.startswith('---'):
        return None, None
    end = head.find('\n---', 3)
    block = head[3:end if end > 0 else len(head)]
    name = desc = None
    key = None
    buf = []
    for line in block.split('\n'):
        m = re.match(r'^(name|description)\s*:\s*(.*)$', line)
        if m:
            if key == 'description':
                desc = ' '.join(buf).strip()
            key, val = m.group(1), m.group(2).strip()
            buf = [val]
            if key == 'name':
                name = val.strip('"\'')
                key = None
                buf = []
        elif key == 'description' and (line.startswith('  ') or line.startswith('\t')):
            buf.append(line.strip())
        elif key == 'description' and not line.strip():
            continue
        elif key == 'description':
            desc = ' '.join(buf).strip()
            key = None
            buf = []
    if key == 'description':
        desc = ' '.join(buf).strip()
    if desc:
        desc = desc.strip('"\'').replace('>-', ' ').strip()
    return name, desc


def newest_mtime():
    newest = 0.0
    for _, base, _inv in TREES:
        if not os.path.isdir(base):
            continue
        for entry in os.scandir(base):
            if not entry.is_dir():
                continue
            f = os.path.join(entry.path, 'SKILL.md')
            try:
                m = os.stat(f).st_mtime
            except OSError:
                continue
            if m > newest:
                newest = m
    return newest


def build_index():
    """{skill_name: {description, trees:[...], invocable: bool, dir}}"""
    index = {}
    for label, base, invocable in TREES:
        if not os.path.isdir(base):
            continue
        for entry in os.scandir(base):
            if not entry.is_dir():
                continue
            path = os.path.join(entry.path, 'SKILL.md')
            if not os.path.isfile(path):
                continue
            name, desc = parse_frontmatter(path)
            key = (name or entry.name).strip()
            row = index.setdefault(key, {'description': '', 'trees': [], 'invocable': False,
                                         'dir': entry.name})
            if desc and len(desc) > len(row['description']):
                row['description'] = desc
            if label not in row['trees']:
                row['trees'].append(label)
            if invocable:
                row['invocable'] = True
    return index


def load_index(force=False):
    if not force and os.path.isfile(CACHE):
        try:
            with io.open(CACHE, encoding='utf-8-sig') as fh:
                blob = json.load(fh)
            if blob.get('newest_mtime', 0) >= newest_mtime() - 1:
                return blob['index'], False
        except Exception:
            pass
    index = build_index()
    try:
        with io.open(CACHE, 'w', encoding='utf-8', newline='') as fh:
            json.dump({'newest_mtime': newest_mtime(), 'index': index}, fh)
    except Exception:
        pass
    return index, True


def terms(text):
    return [t for t in re.split(r'[^a-z0-9+#.]+', text.lower()) if t and t not in STOP and len(t) > 1]


def score(query, name, desc):
    """Rank one skill against a query. Name evidence dominates; coverage scales the total.

    Rewritten 2026-09-02 after the `browser automation` selftest check had been failing
    unnoticed. Three defects, all measured, none of them the term-frequency bug the ticket
    guessed at:

    1. THE ABSENCE PENALTY SANK THE RIGHT ANSWERS. A flat `-2.0` per unmatched term applied
       even to a skill whose NAME is the thing asked for, and it did not care how strongly
       the other terms matched. `browser-use` scored 5.5 (+6 name, +1.5 desc, -2 because
       "automation" appears nowhere in its description) against a floor of 6.0, so the skill
       literally named for the job was excluded. `playwright` scored -0.5. A caller's synonym
       missing from a description is weak evidence, not disqualifying.
    2. AN INCIDENTAL PHRASE OUTRANKED A NAME MATCH. `phrase in description` paid 12.0 while
       a query term in the NAME paid 6.0, so `pbi-screenshotter`, `pbix-extractor` and
       `agents-sdk` each scored 15.0 on one passing mention of "browser automation" and
       leapfrogged the entire browser cluster.
    3. RAW TERM FREQUENCY REWARDED LONG DESCRIPTIONS. `browser-use-cloud` counted "browser"
       eight times across 817 chars and beat `browser-use` at 235 chars. Frequency in prose
       measures verbosity, not fit.

    So: coverage is a MULTIPLIER rather than a subtraction (a skill matching half the query
    keeps three quarters of its score instead of going negative), a description term scores on
    PRESENCE rather than frequency so length cannot buy rank, and name evidence outweighs
    anything found in prose. selftest() asserts all three against synthetic rows.
    """
    q_terms = terms(query)
    if not q_terms:
        return 0.0, []
    name_l = (name or '').lower()
    desc_l = (desc or '').lower()
    phrase = query.strip().lower()
    total = 0.0
    why = []
    matched = 0

    if len(phrase) > 3 and phrase.replace(' ', '-') in name_l:
        total += 18.0
        why.append('phrase in name')
    if len(phrase) > 3 and phrase in desc_l:
        # Below a single name-term match on purpose: the whole query appearing inside prose
        # is what let pbi-screenshotter, pbix-extractor and agents-sdk each outscore the
        # entire browser cluster on one passing mention.
        total += 4.0
        why.append('phrase in description')

    for t in q_terms:
        hit = False
        if t in name_l:
            # The name IS the skill's claim about itself, so it is the strongest single
            # signal available and must outweigh a mention buried in prose.
            total += 12.0
            why.append('%s in name' % t)
            hit = True
        n = desc_l.count(t)
        if n:
            # PRESENCE, not frequency. A description repeating a term is longer, not a better
            # match: browser-use-cloud counted "browser" eight times across 817 chars and beat
            # browser-use at 235. The count still goes in `why` because it explains the hit.
            total += 1.5
            why.append('%s x%d' % (t, n))
            hit = True
        if hit:
            matched += 1

    # Coverage as a multiplier, not a penalty. Every term matched keeps the full score; a
    # query half-covered keeps three quarters of it. Nothing matched scores zero, which the
    # floor then rejects, so the nonsense-query guarantee holds without going negative.
    total *= 0.5 + 0.5 * (float(matched) / len(q_terms))
    if matched < len(q_terms):
        why.append('%d/%d terms' % (matched, len(q_terms)))
    return total, why


def head_noun(name):
    parts = name.split('-')
    return parts[0] if parts else name


def search(index, query, top=6, floor=6.0):
    rows = []
    for name, row in index.items():
        s, why = score(query, name, row['description'])
        if s >= floor:
            rows.append({'name': name, 'score': round(s, 1), 'why': why[:4],
                         'description': row['description'], 'trees': row['trees'],
                         'invocable': row['invocable']})
    rows.sort(key=lambda r: (-r['score'], r['name']))
    return rows[:top]


def clusters(rows):
    """Group hits that share a head noun, so a caller can tell near-misses apart."""
    by = {}
    for r in rows:
        by.setdefault(head_noun(r['name']), []).append(r)
    return {k: v for k, v in by.items() if len(v) > 1}


def all_clusters(index, min_size=2):
    """Every head-noun cluster in the whole roster, biggest first."""
    by = {}
    for name in index:
        by.setdefault(head_noun(name), []).append(name)
    groups = {k: sorted(v) for k, v in by.items() if len(v) >= min_size}
    return sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0]))


def render_clusters(index, rows):
    groups = all_clusters(index)
    total = sum(len(v) for _, v in groups)
    out = ['collision report: %d cluster(s) covering %d of %d skill(s); %d cluster(s) have 3+ members'
           % (len(groups), total, len(index), sum(1 for _, v in groups if len(v) >= 3)), '']
    if rows:
        heads = sorted(set(head_noun(r['name']) for r in rows))
        out.append('clusters touching this query:')
        for h in heads:
            members = dict(groups).get(h)
            if members:
                out.append('  %-16s %s' % (h, ', '.join(members)))
        out.append('')
    out.append('largest clusters in the roster:')
    for head, members in groups[:12]:
        out.append('  %-16s %2d  %s' % (head, len(members), ', '.join(members[:6]) +
                                        (', ...' if len(members) > 6 else '')))
    return '\n'.join(out)


def render(query, rows, rebuilt):
    if not rows:
        return ('no local skill matches "%s".\n'
                'Nothing on disk covers it - check the skills.sh registry with the find-skills '
                'skill before concluding the capability is missing.' % query)
    out = ['%d local skill(s) match "%s"%s:' % (len(rows), query, ' (index rebuilt)' if rebuilt else ''), '']
    groups = clusters(rows)
    for r in rows:
        flag = 'INVOCABLE' if r['invocable'] else 'NOT INVOCABLE (description source only, .agents tree)'
        desc = r['description'] or '(no description in frontmatter)'
        if len(desc) > 300:
            desc = desc[:297] + '...'
        out.append('%-34s %-5s %s' % (r['name'], r['score'], flag))
        out.append('    trees: %s' % ', '.join(r['trees']))
        out.append('    %s' % desc)
        out.append('')
    if groups:
        out.append('COLLISION CLUSTERS (same head noun - read both before picking):')
        for head, members in sorted(groups.items()):
            out.append('  %s: %s' % (head, ', '.join(m['name'] for m in members)))
        out.append('')
    if not any(r['invocable'] for r in rows):
        out.append('NOTE: every hit lives only in .agents/skills, which is a description source, '
                   'not a loaded tree. Copy the bundle into .claude/skills before calling it.')
    return '\n'.join(out)


def selftest():
    index, _ = load_index()
    fails = []

    ran = [0]

    def check(name, cond, detail=''):
        ran[0] += 1
        if not cond:
            fails.append('%s %s' % (name, detail))

    check('index is populated', len(index) > 300, '(got %d)' % len(index))

    vol = search(index, 'options volatility', top=8)
    names = [r['name'] for r in vol]
    check('options volatility finds the natenberg family',
          any(n.startswith('natenberg') for n in names), str(names[:5]))

    br = search(index, 'browser automation', top=8)
    br_names = set(r['name'] for r in br)
    wanted = {'browser-use', 'playwriter', 'dev-browser', 'agent-browser'}
    check('browser automation finds the browser cluster',
          len(wanted & br_names) >= 2, str(sorted(br_names)))

    junk = search(index, 'zzqqxx nonexistent gibberish', top=8)
    check('nonsense query returns nothing', junk == [], str(junk))

    # The three defects behind the browser-cluster miss, asserted directly so a scoring
    # change cannot quietly reintroduce one. Synthetic rows, because these are properties of
    # score() and must not depend on what happens to be installed today.
    named, _ = score('browser automation', 'browser-use',
                     'Drive a real Chrome session to fill forms and read a rendered page.')
    check('a name match survives an unmatched query term', named >= 6.0, '(got %.1f)' % named)
    incidental, _ = score('browser automation', 'pbi-report-thing',
                          'Capture a Power BI page. Uses browser automation internally.')
    check('a name match outranks an incidental phrase in prose', named > incidental,
          '(name %.1f vs prose %.1f)' % (named, incidental))
    terse, _ = score('browser automation', 'x-tool', 'browser automation')
    verbose, _ = score('browser automation', 'y-tool',
                       'browser browser browser browser browser automation ' + 'filler ' * 90)
    check('description length does not buy rank', terse >= verbose,
          '(terse %.1f vs verbose %.1f)' % (terse, verbose))

    # Added 2026-09-01 with the stopword extension, because the ranker now feeds an automatic
    # hook on every prompt and a person does not type keywords. Before that extension, the
    # accessibility query below ranked education-data-compliance and icml-reviewer above every
    # react and accessibility skill installed, purely on filler words.
    nat = [r['name'] for r in search(index, 'help me analyze the earnings report and decide '
                                            'whether to trade it', top=5)]
    check('a natural-language earnings request finds the earnings family',
          sum(1 for n in nat if 'earnings' in n) >= 2, str(nat))
    lp = [r['name'] for r in search(index, 'I need to build a high converting landing page for '
                                           'the product', top=5)]
    check('a natural-language landing-page request ranks landing-page first',
          bool(lp) and lp[0] == 'landing-page', str(lp))

    # Invocability must be reported, never assumed: a skill only in .agents cannot be called.
    # Asserted against a synthetic row, not against the current roster, because today every
    # installed skill happens to be mirrored into a loaded tree and the check would pass for
    # the wrong reason. What matters is that the RULE holds when the case arises.
    fake = {'agents-only-example': {'description': 'x', 'trees': ['.agents'], 'invocable': False}}
    rendered = render('x', [{'name': 'agents-only-example', 'score': 9, 'why': [],
                             'description': 'x', 'trees': ['.agents'], 'invocable': False}], False)
    check('an .agents-only skill renders as NOT INVOCABLE', 'NOT INVOCABLE' in rendered, rendered[:120])
    check('and says how to fix it', 'Copy the bundle' in rendered)
    check('a loaded-tree skill renders as INVOCABLE',
          'NOT INVOCABLE' not in render('x', [{'name': 'y', 'score': 9, 'why': [], 'description': 'x',
                                               'trees': ['.claude'], 'invocable': True}], False))
    del fake

    if fails:
        print('FAIL:\n  ' + '\n  '.join(fails))
        return 1
    print('find-local-skill selftest OK: %d checks (index size, domain query, cluster query, '
          'nonsense floor, scoring regressions, natural language, invocability)' % ran[0])
    return 0


def main():
    # Windows consoles default to cp1252, and one non-Latin char in a description crashed the print.
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    ap = argparse.ArgumentParser(description='Search locally installed skills by what they do.')
    ap.add_argument('query', nargs='*', help='what you need a skill for')
    ap.add_argument('--top', type=int, default=6)
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--rebuild', action='store_true')
    ap.add_argument('--clusters', action='store_true',
                    help='full name-collision report (which is a third of the roster)')
    ap.add_argument('--selftest', action='store_true')
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    index, rebuilt = load_index(force=args.rebuild)
    if args.clusters and not args.query:
        print(render_clusters(index, []))
        return 0
    if not args.query:
        print('indexed %d skill(s) across %d tree(s). Pass a query.'
              % (len(index), sum(1 for _, b, _ in TREES if os.path.isdir(b))))
        return 0

    query = ' '.join(args.query)
    rows = search(index, query, top=args.top)
    if args.json:
        # Windows stdout defaults to cp1252, and `ensure_ascii=False` then raises
        # UnicodeEncodeError on the first skill description carrying a non-ANSI character
        # (found 2026-09-01: a `â†’` arrow in one description made --json unusable on this
        # machine, so every programmatic consumer got a traceback instead of results).
        # Reconfigure rather than escape, so the JSON stays readable.
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except (AttributeError, ValueError):
            pass
        print(json.dumps({'query': query, 'hits': rows, 'clusters': clusters(rows)},
                         ensure_ascii=False, indent=2))
    else:
        print(render(query, rows, rebuilt))
        if args.clusters:
            print()
            print(render_clusters(index, rows))
    return 0


if __name__ == '__main__':
    sys.exit(main())
