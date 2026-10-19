# Emoji rendering gate ðŸ˜€

This fixture exists to prove that emoji code points render as real color
glyphs in the output PDF, not as `.notdef` tofu boxes (â–¯).

Color emoji on one line: ðŸ˜€ â¤ï¸ ðŸš€ âœ… ðŸ’¡

A variation-selector sequence (FE0F) renders color: â¤ï¸ â€” the bare code point
â¤ is text-style. Both must come from a font in the cascade, never tofu.

Non-emoji Unicode (unchanged, regression guard): em dash â€”, times Ã—, arrow â†’,
bullet â€¢, ellipsis â€¦
