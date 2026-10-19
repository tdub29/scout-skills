# AskUserQuestion â€” non-ASCII / CJK characters

Read this on demand when an AskUserQuestion contains Chinese (ç¹é«”/ç°¡é«”),
Japanese, Korean, or other non-ASCII text. The operative rule is in the
always-loaded AskUserQuestion self-check ("Non-ASCII characters written directly,
NOT \u-escaped"); this doc is the full justification.

## The rule

When any string field (question, option label, option description) contains
non-ASCII text, emit the literal UTF-8 characters in the JSON string. **Never
escape them as `\uXXXX`.**

Claude Code's tool parameter pipe is UTF-8 native and passes characters through
unchanged. Only JSON-mandatory escapes remain allowed: `\n`, `\t`, `\"`, `\\`.

## Why escaping fails

Manually escaping requires recalling each codepoint from training, which is
unreliable for long CJK strings â€” the model regularly emits the wrong codepoint.
Example: writing `ã„ƒ` thinking it is ç®¡ (U+7BA1), but `ã„ƒ` is actually ã„ƒ,
so the user sees `ç®¡ç†å·¥å…·` rendered as `ã„ƒ3ç”¨ç®±`.

The trigger is long, multi-line questions with hundreds of CJK characters: that
is exactly when reflexive escaping kicks in and exactly when miscoding is most
damaging. Long â‰  escape. Keep characters literal.

- Wrong: `"question": "è«‹é¸æ“‡\uXXXX\uXXXX\uXXXX\uXXXX"`
- Right: `"question": "è«‹é¸æ“‡ç®¡ç†å·¥å…·"`
