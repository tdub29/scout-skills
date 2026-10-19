"""CJK-aware tokenization for relevance scoring and near-duplicate detection.

The skill ships with zero hard dependencies (pyproject ``dependencies = []``)
so it installs across 50+ Agent Skills hosts as plain Python. Chinese text has
no whitespace word boundaries, so the original ``str.split()`` tokenizers in
relevance.py / dedupe.py collapse a whole sentence into a single token and
break token-overlap scoring and Jaccard de-duplication for Chinese sources
(Xiaohongshu, Bilibili).

``segment(text)`` fixes that. It splits text into maximal CJK and non-CJK runs:

- Non-CJK (ASCII / Latin) runs keep the original ``\\w+`` word behaviour.
- CJK runs are routed through jieba when it is installed (best quality), and
  fall back to character bigrams when jieba is absent. Bigrams are a
  dictionary-free segmentation that still gives robust overlap signal â€” e.g.
  query "å¤§æ¨¡åž‹" -> {å¤§æ¨¡, æ¨¡åž‹} overlaps text "å›½äº§å¤§æ¨¡åž‹è¯„æµ‹" -> {..å¤§æ¨¡, æ¨¡åž‹..}.

jieba stays OPTIONAL: present -> used; absent -> bigram fallback. We never add
it to the hard dependency set, preserving the install-anywhere property.
"""

from __future__ import annotations

import re
from typing import List

# CJK ideographs + Japanese kana + Korean hangul. The Chinese ideograph block
# (ä¸€-é¿¿) and its extension-A (ã€-ä¶¿) cover the cases we care
# about; kana/hangul are included so mixed-language text degrades gracefully.
_CJK_CHARS = r"ã€-ä¶¿ä¸€-é¿¿ï¤€-ï«¿ã€-ãƒ¿ê°€-íž¯"
_CJK_RE = re.compile(f"[{_CJK_CHARS}]")
_CJK_RUN_RE = re.compile(f"[{_CJK_CHARS}]+")
_LATIN_RE = re.compile(r"\w+")

# High-frequency Chinese function words that dilute overlap signal, mirroring
# the role of the English STOPWORDS sets in relevance.py / dedupe.py.
CHINESE_STOPWORDS = frozenset(
    {
        "çš„", "äº†", "å’Œ", "æ˜¯", "åœ¨", "æˆ‘", "æœ‰", "ä¹Ÿ", "å°±", "ä¸", "äºº", "éƒ½",
        "ä¸€", "ä¸€ä¸ª", "ä¸Š", "å¾ˆ", "åˆ°", "è¯´", "è¦", "åŽ»", "ä½ ", "ä¼š", "ç€",
        "æ²¡æœ‰", "çœ‹", "å¥½", "è‡ªå·±", "è¿™", "é‚£", "è¿™ä¸ª", "é‚£ä¸ª", "ä»€ä¹ˆ", "æ€Žä¹ˆ",
        "ä¸ºä»€ä¹ˆ", "ä»¥åŠ", "æˆ–è€…", "ä½†æ˜¯", "å› ä¸º", "æ‰€ä»¥", "å¦‚æžœ", "å¯ä»¥",
        "è¿™æ ·", "é‚£æ ·", "ä»–ä»¬", "æˆ‘ä»¬", "ä½ ä»¬", "å®ƒ", "å¥¹", "ä»–", "å—", "å‘¢",
        "å§", "å•Š", "å“¦", "å—¯", "ä¸Ž", "åŠ", "ç­‰", "è¢«", "æŠŠ", "è®©", "ç»™", "å‘",
        "è¿˜", "å†", "åˆ", "ä»Ž", "å¯¹", "ä¸º", "ä»¥", "ä¹‹", "å…¶", "ä¸­",
    }
)

# Optional jieba, resolved once at import time. Binding it here (rather than
# lazily on first use) avoids a race: the pipeline scores relevance inside a
# ThreadPoolExecutor, so a lazy initializer with mutable globals could have two
# threads import concurrently and observe a half-initialized state. Doing it at
# module load means the binding is settled before any worker thread runs.
#
# The BROAD `except Exception` is intentional: jieba is an optional enhancement,
# so ANY failure to load it â€” package absent, corrupted install, missing data
# files, or a setLogLevel signature change across versions â€” must degrade to the
# bigram fallback, never crash the skill. jieba guards its own first-call
# dictionary build with an internal lock, so concurrent `cut()` is safe once the
# module object is bound.
try:
    import jieba as _jieba  # type: ignore

    _jieba.setLogLevel(60)  # silence dictionary-build chatter on stderr
except Exception:
    _jieba = None


def has_cjk(text: str) -> bool:
    """True if the text contains any CJK / kana / hangul character."""
    return bool(text) and _CJK_RE.search(text) is not None


def _cjk_tokens(run: str) -> List[str]:
    # Reads the module-global _jieba at call time, so tests can force the bigram
    # path deterministically by setting cjk._jieba = None regardless of whether
    # jieba is installed in the environment.
    if _jieba is not None:
        return [w for w in _jieba.cut(run) if w.strip() and _CJK_RE.search(w)]
    # Dictionary-free fallback: character bigrams (single char if run length 1).
    if len(run) <= 1:
        return [run] if run else []
    return [run[i:i + 2] for i in range(len(run) - 1)]


def segment(text: str) -> List[str]:
    """Tokenize mixed CJK / Latin text into a flat list of lowercased tokens.

    CJK runs -> jieba words or character bigrams. Latin runs -> ``\\w+`` words.
    Order is preserved; callers that want a set can wrap the result.
    """
    if not text:
        return []
    text = text.lower()
    if not has_cjk(text):
        return _LATIN_RE.findall(text)

    out: List[str] = []
    pos = 0
    for match in _CJK_RUN_RE.finditer(text):
        if match.start() > pos:
            out.extend(_LATIN_RE.findall(text[pos:match.start()]))
        out.extend(_cjk_tokens(match.group()))
        pos = match.end()
    if pos < len(text):
        out.extend(_LATIN_RE.findall(text[pos:]))
    return out
