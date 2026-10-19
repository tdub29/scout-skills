#!/usr/bin/env python3
"""Build human navigation from installed bundles and recorded provenance. Stdlib only."""

import argparse
import collections
import json
from pathlib import Path
import re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]

# Names carry stronger evidence than descriptions. First category wins an equal score.
# ponytail: lexical navigation, not semantic classification; refine these rules for misroutes.
CATEGORIES = [
    ('sports-and-fantasy', 'Sports and fantasy', r'sports?|fantasy|dynasty|nfl|baseball|trackman|ratings-strength|pybaseball'),
    ('finance-and-trading', 'Finance and trading', r'financ\w*|trad\w*|stock\w*|invest\w*|options?|volatility|arbitrage|polymarket|kalshi|natenberg|saliba|grimes|katz|kase|chan|erlanger|fitschen|ciana|kezeli|williams|turtle|momentum|position-sizing|risk-metrics|rrg|chainlink'),
    ('careers-and-job-search', 'Careers and job search', r'career\w*|resume\w*|interview\w*|job\w*|cv|cover-letter|linkedin-profile|profile-optimizer|offer-comparison|reference-list|salary|brag'),
    ('security-and-compliance', 'Security and compliance', r'secur\w*|compliance|vulnerab\w*|attack\w*|exploit\w*|authenticat\w*|authorization|oauth\w*|jwt|csrf|cors|tls|ssl|sbom|penetration|leakage|secret\w*|idor|supply-chain-attacks|forced-browsing'),
    ('animation-and-web-effects', 'Animation and web effects', r'animat\w*|motion|scroll\w*|shader|webgl|threejs|gsap|particles?|glow|lasers?|dither|reveal|hover|cursor|masking|gradient|vantajs|lottie|marquee|matterjs|transitions?'),
    ('images-video-and-audio', 'Images, video and audio', r'images?|video\w*|photo\w*|audio|podcast|captions?|thumbnail|broll|clip\w*|heygen|remotion|hyperframes|watch|transcribe|vectorcraft|graphic-designer|algorithmic-art'),
    ('design-and-interfaces', 'Design and interfaces', r'design\w*|ui|ux|interface\w*|layout\w*|typograph\w*|colors?|figma|impeccable|accessibility|accessible|a11y|frontend|brandkit|brand|shadows?|glass|brutalist|minimalist|editorial|skeuomorphic|framed|container|bklit|refero|seam-craft|taste|stitch|apple'),
    ('data-and-analytics', 'Data and analytics', r'data\w*|analytics?|sql\w*|database\w*|powerbi|power-bi|pbi|te2|te-docs|kimball|dama|mcgilvray|marr|nigd|kleppmann|dropback|causal|statistic\w*|visualization|visualisation|bertin|tufte|model-card|model-interpretation|statistical-modeling|predictive-modeling|write-query|jupyter'),
    ('marketing-and-growth', 'Marketing and growth', r'market\w*|growth|seo|aso|ads?|advertis\w*|cro|conversion\w*|copywrit\w*|copy-editing|sales\w*|revops|prospect\w*|lead\w*|cold-email|cold-outbound|email\w*|sms|social|influencer|newsletter|hook\w*|jab-hook|public-relations|referrals?|retention|churn|signup|paywalls?|popups|pricing|positioning|offers|onboarding|launch|distribution|directory-submissions|value-prop\w*|value-proposition|plg'),
    ('agents-skills-and-workflows', 'Agents, skills and workflows', r'agents?|skills?|scout|harness|codex|claude|cursor-rules|cavecrew|caveman|ponytail|loopy|loopify|loop\w*|subagent\w*|llm\w*|prompt\w*|mcp|autoresearch|huyen|gemini|neuro-symbolic|training-data|model-eval|rde-eval|content-eval|full-output|rule\w*|screenshot|browser\w*|playwright|playwriter|dev-browser|iterate-until-verified'),
    ('software-engineering', 'Software engineering', r'code\w*|coding|software|api|react\w*|expo|native|swift|python|git\w*|gh|cli|debug\w*|refactor\w*|test\w*|verif\w*|deploy\w*|cloudflare|firebase|supabase|postgres|performance|error-handling|environment|npm|ship\w*|opensource|web-quality|pre-launch|content-hash|flux|toolify|container-lines|intended-vs-implemented'),
    ('business-product-and-operations', 'Business, product and operations', r'business|product\w*|operations?|ops|logistics|carrier|customs|freight|supply-chain|safety-stock|otif|forecast-accuracy|returns|inventory|fundrais\w*|stakeholder|lean-canvas|legal\w*|trademark|ip-management|llc|team|company|customer\w*|pm|priorit\w*|sprint|project\w*|capacity|monetization|journey|counterparty|buy-or-bounce|north-star|events'),
    ('writing-and-documents', 'Writing and documents', r'writ\w*|prose|documents?|docx|pdf|pptx|xlsx|slide\w*|deck\w*|present\w*|readme|read-book|book-to-skill|white-paper|voice\w*|minto|internal-comms|email-drafter|paste|no-ai-slop|ai-writing|content-strategy|post\w*|quote-post|x-longform'),
    ('personal-health-and-productivity', 'Personal health and productivity', r'health|nutrition|inflammation|wellbeing|inner-child|adhd|affirmation|personal|productiv\w*|obsidian|goal\w*|life|second-brain|hatch-pet|scheduling'),
    ('research-and-decisions', 'Research and decisions', r'research\w*|decid\w*|decision\w*|thinking|theory|experiment\w*|benchmark\w*|calibration|premortem|pre-mortem|hamming|greene|machiavelli|sun-tzu|marcus|newport|duhigg|tetlock|kohavi|provost|expert-panel|grill|unstuck|explain|audit-verify|cut-the-curve|measurement|root-cause'),
]

ORIGINS = {
    'imported': 'Imported; modification history unverified',
    'adapted': 'Adapted from recorded sources',
    'created_claimed_unverified': 'Local creation claim; unverified',
    'unresolved': 'Origin unresolved',
}


def frontmatter(text):
    """Read name/description scalars, including quoted continuations and YAML block text."""
    lines = text.lstrip('\ufeff').splitlines()
    if not lines or lines[0].strip() != '---':
        return {}
    result = {}
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == '---':
            break
        match = re.match(r'^(name|description):\s*(.*)$', line)
        if not match:
            continue
        key, value = match.groups()
        parts = [] if re.fullmatch(r'[>|][+-]?[1-9]?', value) else [value]
        for continuation in lines[i + 1:]:
            if continuation.strip() == '---' or (continuation and not continuation[0].isspace()):
                break
            parts.append(continuation.strip())
        value = ' '.join(parts).strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
            if value[0] == '"':
                try:
                    value = json.loads(value)
                except json.JSONDecodeError:
                    value = value[1:-1].replace('\\"', '"')
            else:
                value = value[1:-1].replace("''", "'")
        result[key] = re.sub(r'\s+', ' ', value).strip()
    return result


def category(name, description):
    # Explicit domain names outrank incidental implementation vocabulary.
    if re.search(r'(?:^|-)(?:security|vulnerabilities|xss|sqli|owasp|sast|dast)(?:-|$)', name.lower()):
        return 'security-and-compliance'
    if name.lower().startswith(('trademark-', 'safety-stock-')):
        return 'business-product-and-operations'
    if name.lower() == 'cursor-rules':
        return 'agents-skills-and-workflows'
    scores = []
    for slug, _title, pattern in CATEGORIES:
        regex = r'(?<![a-z0-9])(?:' + pattern + r')(?![a-z0-9])'
        name_hits = len(re.findall(regex, name.lower()))
        description_hits = len(set(re.findall(regex, description.lower())))
        scores.append((name_hits * 12 + min(description_hits, 5), slug))
    best = max(score for score, _slug in scores)
    return next(slug for score, slug in scores if score == best) if best else 'research-and-decisions'


def cell(text):
    return text.replace('\u2014', '-').replace('\u2013', '-').replace('|', '\\|').replace('\n', ' ').replace('<', '&lt;').replace('>', '&gt;')


def source_cell(record):
    url = record.get('upstream_url')
    if not url or not re.fullmatch(r'https?://[^\s<>]+', url):
        return 'Source not recorded' if not record.get('book') else cell(record['book']) + '; source URL not recorded'
    label = re.sub(r'^https?://(?:www\.)?', '', url).rstrip('/')
    source = f'[{cell(label)}](<{url}>)'
    revision = record.get('recorded_upstream_revision')
    if revision:
        verification = 'verified' if record.get('revision_verified') is True else 'unverified'
        repo = re.match(r'^https://github\.com/([^/]+/[^/]+?)(?:\.git)?/?$', url)
        if repo and re.fullmatch(r'[a-fA-F0-9]{7,40}', revision):
            source += f'; recorded revision [{revision[:12]}](https://github.com/{repo.group(1)}/commit/{revision}) ({verification})'
        else:
            source += '; recorded revision ' + cell(str(revision)) + f' ({verification})'
    else:
        source += '; revision not recorded'
    return source


def summary(text):
    if len(text) <= 220:
        return cell(text)
    return cell(text[:217].rsplit(' ', 1)[0] + '...')


def generate():
    provenance = json.loads((ROOT / 'provenance.json').read_text(encoding='utf-8'))
    records = provenance['records']
    by_name = {record['name']: record for record in records}
    if len(by_name) != len(records):
        raise ValueError('Duplicate provenance bundle names')
    bundles = sorted(p for p in (ROOT / 'skills').iterdir() if p.is_dir() and (p / 'SKILL.md').is_file())
    names = {p.name for p in bundles}
    if names != set(by_name):
        raise ValueError('Bundle/provenance mismatch: ' + ', '.join(sorted(names ^ set(by_name))))
    groups = collections.defaultdict(list)
    for bundle in bundles:
        metadata = frontmatter((bundle / 'SKILL.md').read_text(encoding='utf-8-sig'))
        description = metadata.get('description') or 'No description supplied in frontmatter.'
        origin = by_name[bundle.name]['classification']
        if origin not in ORIGINS:
            raise ValueError('Unknown origin classification: ' + origin)
        groups[category(bundle.name, description)].append((bundle.name, description, origin))
    assigned = [name for rows in groups.values() for name, _description, _origin in rows]
    if len(assigned) != len(names) or set(assigned) != names:
        raise ValueError('Catalog must cover every bundle exactly once')
    outputs = {}
    index = ['# Skill catalog', '',
             'Browse by the task you want to do. Each bundle has one primary category for navigation; categories make no authorship or licensing claim.', '',
             f'{len(names)} skill bundles across {len(CATEGORIES)} categories. Descriptions come from SKILL.md frontmatter and are shortened for browsing.', '',
             '| Category | Bundles |', '| --- | ---: |']
    for slug, title, _pattern in CATEGORIES:
        rows = groups[slug]
        index.append(f'| [{title}]({slug}.md) | {len(rows)} |')
        page = [f'# {title}', '', '[All categories](README.md)', '', f'{len(rows)} bundles. One primary category per bundle; cross-disciplinary skills may also help with other tasks.', '',
                '| Skill | What it does | Recorded origin | Upstream / source |', '| --- | --- | --- | --- |']
        for name, description, origin in rows:
            page.append(f'| [{cell(name)}](../../skills/{quote(name)}/SKILL.md) | {summary(description)} | {ORIGINS[origin]} | {source_cell(by_name[name])} |')
        page += ['', 'Origin labels preserve the recorded classifications. A local creation claim is unverified; an import is not certified as an unchanged upstream copy. Revisions are recorded pointers, not independently verified baselines. See [provenance](../../PROVENANCE.md), [source records](../../provenance.json), [third-party notices](../../THIRD_PARTY_NOTICES.md), and [updating skills](../UPDATING.md).', '']
        outputs[ROOT / 'docs' / 'catalog' / (slug + '.md')] = '\n'.join(page)
    index += ['', '## Recorded origins', '', '| Label | Bundles |', '| --- | ---: |']
    origin_counts = collections.Counter(record['classification'] for record in records)
    for origin, label in ORIGINS.items():
        index.append(f'| {label} | {origin_counts[origin]} |')
    index += ['', 'These labels describe recorded provenance, not license clearance or certified original authorship. Each category lists recorded upstream source links and revisions where available. See [provenance](../../PROVENANCE.md), [third-party notices](../../THIRD_PARTY_NOTICES.md), and [how to review and update skills](../UPDATING.md).', '',
              '## Search or rebuild', '', 'For overlapping topics, use the local ranker from the repository root:', '', '```sh', 'python scripts/find-local-skill.py "your task" --top 8', 'python scripts/build-catalog.py', 'python scripts/build-catalog.py --check', '```', '',
              'The generator uses skill frontmatter, provenance records and ordered lexical category rules. Results are deterministic; categories guide browsing rather than replacing a read of the skill itself.', '']
    outputs[ROOT / 'docs' / 'catalog' / 'README.md'] = '\n'.join(index)
    outputs[ROOT / 'skills' / 'README.md'] = '\n'.join(['# Skills', '', f'Browse all {len(names)} bundles in the [category catalog](../docs/catalog/README.md). Each skill stays in its existing folder, with its supporting files.', '',
        'Use the catalog descriptions to find a starting point, then read the selected SKILL.md. Recorded origin labels distinguish imports, source-derived adaptations, unverified local creation claims and unresolved origins; categories do not establish authorship.', '',
        'See [provenance](../PROVENANCE.md) and [third-party notices](../THIRD_PARTY_NOTICES.md) for source and licensing context. Follow [updating skills](../docs/UPDATING.md) to review upstream changes.', ''])
    return outputs, groups, len(names)


def selfcheck():
    assert frontmatter('---\nname: sample\ndescription: >-\n  First line\n  second line\n---')['description'] == 'First line second line'
    assert frontmatter('---\ndescription: "A quoted\n  continuation"\n---')['description'] == 'A quoted continuation'
    assert frontmatter("---\ndescription: 'It''s quoted'\n---")['description'] == "It's quoted"
    assert 'Source not recorded' == source_cell({})
    assert '/commit/abcdef1234567' in source_cell({'upstream_url': 'https://github.com/example/skills', 'recorded_upstream_revision': 'abcdef1234567'})
    for name, expected in [('scout-skills', 'agents-skills-and-workflows'), ('resume-tailor', 'careers-and-job-search'), ('natenberg-volatility-skew', 'finance-and-trading'), ('dynasty-trade-construction', 'sports-and-fantasy'), ('sql-query-optimization', 'data-and-analytics'), ('testing-for-xss-vulnerabilities', 'security-and-compliance')]:
        assert category(name, '') == expected, name
    for name, description, expected in [
        ('testing-api-security-with-owasp-top-10', 'Test an API and integrate tests with GitHub.', 'security-and-compliance'),
        ('integrating-dast-with-owasp-zap-in-pipeline', 'Add API testing to the deployment pipeline.', 'security-and-compliance'),
        ('trademark-search', 'Search trademark registrations.', 'business-product-and-operations'),
        ('safety-stock-review', 'Review inventory safety stock.', 'business-product-and-operations'),
        ('cursor-rules', 'Configure Cursor agent rules.', 'agents-skills-and-workflows'),
    ]:
        assert category(name, description) == expected, name


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check deterministic output and exact bundle coverage without writing.')
    args = parser.parse_args()
    selfcheck()
    outputs, groups, total = generate()
    stale = [path for path, content in outputs.items() if not path.exists() or path.read_bytes() != content.encode('utf-8')]
    extra = set((ROOT / 'docs' / 'catalog').glob('*.md')) - set(outputs)
    if args.check:
        if stale or extra:
            for path in sorted(set(stale) | extra):
                print('Out of date: ' + path.relative_to(ROOT).as_posix())
            return 1
    else:
        if extra:
            raise ValueError('Unexpected category pages; review before replacing: ' + ', '.join(p.name for p in sorted(extra)))
        for path, content in outputs.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content.encode('utf-8'))
    print(f'{"Checked" if args.check else "Built"} {len(outputs)} catalog files: {total} bundles, {len(CATEGORIES)} categories, every bundle exactly once.')
    for slug, title, _pattern in CATEGORIES:
        print(f'{title}: {len(groups[slug])}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
