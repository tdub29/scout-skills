#!/usr/bin/env bash
# Ø§Ù„ØªØ­Ù‚Ù‚ Ù…Ù† Ø§ÙƒØªÙ…Ø§Ù„ Ø¬Ù…ÙŠØ¹ Ø§Ù„Ù…Ø±Ø§Ø­Ù„ ÙÙŠ task_plan.md
# ÙŠÙ†Ù‡ÙŠ Ø¯Ø§Ø¦Ù…Ù‹Ø§ Ø¨Ø±Ù…Ø² Ø®Ø±ÙˆØ¬ 0 â€” ÙŠØ³ØªØ®Ø¯Ù… stdout Ù„Ù„Ø¥Ø¨Ù„Ø§Øº Ø¹Ù† Ø§Ù„Ø­Ø§Ù„Ø©
# ÙŠÙØ³ØªØ¯Ø¹Ù‰ Ø¨ÙˆØ§Ø³Ø·Ø© Ø®Ø·Ø§Ù Stop Ù„Ù„Ø¥Ø¨Ù„Ø§Øº Ø¹Ù† Ø­Ø§Ù„Ø© Ø§ÙƒØªÙ…Ø§Ù„ Ø§Ù„Ù…Ù‡Ù…Ø©

PLAN_FILE="${1:-task_plan.md}"

if [ ! -f "$PLAN_FILE" ]; then
    echo "[planning-with-files-ar] Ù„Ù… ÙŠØªÙ… Ø§Ù„Ø¹Ø«ÙˆØ± Ø¹Ù„Ù‰ task_plan.md â€” Ù„Ø§ ØªÙˆØ¬Ø¯ Ø¬Ù„Ø³Ø© ØªØ®Ø·ÙŠØ· Ù†Ø´Ø·Ø©."
    exit 0
fi

# Ø­Ø³Ø§Ø¨ Ø¥Ø¬Ù…Ø§Ù„ÙŠ Ø¹Ø¯Ø¯ Ø§Ù„Ù…Ø±Ø§Ø­Ù„
TOTAL=$(grep -c "### Ø§Ù„Ù…Ø±Ø­Ù„Ø©" "$PLAN_FILE" || true)

# Ø§Ù„ØªØ­Ù‚Ù‚ Ø£ÙˆÙ„Ø§Ù‹ Ù…Ù† ØªÙ†Ø³ÙŠÙ‚ **Ø§Ù„Ø­Ø§Ù„Ø©:**
COMPLETE=$(grep -cF "**Ø§Ù„Ø­Ø§Ù„Ø©:** complete" "$PLAN_FILE" || true)
IN_PROGRESS=$(grep -cF "**Ø§Ù„Ø­Ø§Ù„Ø©:** in_progress" "$PLAN_FILE" || true)
PENDING=$(grep -cF "**Ø§Ù„Ø­Ø§Ù„Ø©:** pending" "$PLAN_FILE" || true)

# Ø¨Ø¯ÙŠÙ„: Ø¥Ø°Ø§ Ù„Ù… ÙŠØªÙ… Ø§Ù„Ø¹Ø«ÙˆØ± Ø¹Ù„Ù‰ **Ø§Ù„Ø­Ø§Ù„Ø©:** ÙØªØ­Ù‚Ù‚ Ù…Ù† ØªÙ†Ø³ÙŠÙ‚ [complete] Ø§Ù„Ù…Ø¶Ù…Ù†
if [ "$COMPLETE" -eq 0 ] && [ "$IN_PROGRESS" -eq 0 ] && [ "$PENDING" -eq 0 ]; then
    COMPLETE=$(grep -c "\[complete\]" "$PLAN_FILE" || true)
    IN_PROGRESS=$(grep -c "\[in_progress\]" "$PLAN_FILE" || true)
    PENDING=$(grep -c "\[pending\]" "$PLAN_FILE" || true)
fi

# Ø§Ù„Ø§ÙØªØ±Ø§Ø¶ÙŠ 0 (Ø¥Ø°Ø§ ÙƒØ§Ù† ÙØ§Ø±ØºÙ‹Ø§)
: "${TOTAL:=0}"
: "${COMPLETE:=0}"
: "${IN_PROGRESS:=0}"
: "${PENDING:=0}"

# Ø§Ù„Ø¥Ø¨Ù„Ø§Øº Ø¹Ù† Ø§Ù„Ø­Ø§Ù„Ø© (ÙŠÙ†Ù‡ÙŠ Ø¯Ø§Ø¦Ù…Ù‹Ø§ Ø¨Ø±Ù…Ø² Ø®Ø±ÙˆØ¬ 0 â€” Ø§Ù„Ù…Ù‡Ø§Ù… ØºÙŠØ± Ø§Ù„Ù…ÙƒØªÙ…Ù„Ø© Ø­Ø§Ù„Ø© Ø·Ø¨ÙŠØ¹ÙŠØ©)
if [ "$COMPLETE" -eq "$TOTAL" ] && [ "$TOTAL" -gt 0 ]; then
    echo "[planning-with-files-ar] Ø§ÙƒØªÙ…Ù„Øª Ø¬Ù…ÙŠØ¹ Ø§Ù„Ù…Ø±Ø§Ø­Ù„ ($COMPLETE/$TOTAL). Ø¥Ø°Ø§ ÙƒØ§Ù† Ù„Ø¯Ù‰ Ø§Ù„Ù…Ø³ØªØ®Ø¯Ù… Ø¹Ù…Ù„ Ø¥Ø¶Ø§ÙÙŠØŒ Ø£Ø¶Ù Ù…Ø±Ø§Ø­Ù„ ÙÙŠ task_plan.md Ù‚Ø¨Ù„ Ø§Ù„Ø¨Ø¯Ø¡."
else
    echo "[planning-with-files-ar] Ø§Ù„Ù…Ù‡Ù…Ø© Ù‚ÙŠØ¯ Ø§Ù„ØªÙ†ÙÙŠØ° ($COMPLETE/$TOTAL Ù…Ø±Ø­Ù„Ø© Ù…ÙƒØªÙ…Ù„Ø©). Ø­Ø¯Ù‘Ø« progress.md Ù‚Ø¨Ù„ Ø§Ù„ØªÙˆÙ‚Ù."
    if [ "$IN_PROGRESS" -gt 0 ]; then
        echo "[planning-with-files-ar] $IN_PROGRESS Ù…Ø±Ø­Ù„Ø©/Ù…Ø±Ø§Ø­Ù„ Ù„Ø§ ØªØ²Ø§Ù„ Ù‚ÙŠØ¯ Ø§Ù„ØªÙ†ÙÙŠØ°."
    fi
    if [ "$PENDING" -gt 0 ]; then
        echo "[planning-with-files-ar] $PENDING Ù…Ø±Ø­Ù„Ø©/Ù…Ø±Ø§Ø­Ù„ Ù…Ø¹Ù„Ù‚Ø©."
    fi
fi
exit 0
