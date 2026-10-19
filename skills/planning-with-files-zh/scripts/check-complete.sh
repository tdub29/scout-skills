#!/usr/bin/env bash
# æ£€æŸ¥ task_plan.md ä¸­æ‰€æœ‰é˜¶æ®µæ˜¯å¦å®Œæˆ
# å§‹ç»ˆä»¥é€€å‡ºç  0 ç»“æŸ â€” ä½¿ç”¨æ ‡å‡†è¾“å‡ºæŠ¥å‘ŠçŠ¶æ€
# ç”± Stop é’©å­è°ƒç”¨ä»¥æŠ¥å‘Šä»»åŠ¡å®ŒæˆçŠ¶æ€

PLAN_FILE="${1:-task_plan.md}"

if [ ! -f "$PLAN_FILE" ]; then
    echo "[planning-with-files] æœªæ‰¾åˆ° task_plan.md â€” æ²¡æœ‰è¿›è¡Œä¸­çš„è§„åˆ’ä¼šè¯ã€‚"
    exit 0
fi

# è®¡ç®—é˜¶æ®µæ€»æ•°
TOTAL=$(grep -c "### é˜¶æ®µ" "$PLAN_FILE" || true)

# å…ˆæ£€æŸ¥ **çŠ¶æ€ï¼š** æ ¼å¼
COMPLETE=$(grep -cF "**çŠ¶æ€ï¼š** complete" "$PLAN_FILE" || true)
IN_PROGRESS=$(grep -cF "**çŠ¶æ€ï¼š** in_progress" "$PLAN_FILE" || true)
PENDING=$(grep -cF "**çŠ¶æ€ï¼š** pending" "$PLAN_FILE" || true)

# å¤‡ç”¨ï¼šå¦‚æžœæœªæ‰¾åˆ° **çŠ¶æ€ï¼š** åˆ™æ£€æŸ¥ [complete] è¡Œå†…æ ¼å¼
if [ "$COMPLETE" -eq 0 ] && [ "$IN_PROGRESS" -eq 0 ] && [ "$PENDING" -eq 0 ]; then
    COMPLETE=$(grep -c "\[complete\]" "$PLAN_FILE" || true)
    IN_PROGRESS=$(grep -c "\[in_progress\]" "$PLAN_FILE" || true)
    PENDING=$(grep -c "\[pending\]" "$PLAN_FILE" || true)
fi

# é»˜è®¤ä¸º 0ï¼ˆå¦‚æžœä¸ºç©ºï¼‰
: "${TOTAL:=0}"
: "${COMPLETE:=0}"
: "${IN_PROGRESS:=0}"
: "${PENDING:=0}"

# æŠ¥å‘ŠçŠ¶æ€ï¼ˆå§‹ç»ˆä»¥é€€å‡ºç  0 ç»“æŸ â€” æœªå®Œæˆçš„ä»»åŠ¡æ˜¯æ­£å¸¸çŠ¶æ€ï¼‰
if [ "$COMPLETE" -eq "$TOTAL" ] && [ "$TOTAL" -gt 0 ]; then
    echo "[planning-with-files] æ‰€æœ‰é˜¶æ®µå·²å®Œæˆï¼ˆ$COMPLETE/$TOTALï¼‰ã€‚å¦‚æžœç”¨æˆ·æœ‰é¢å¤–å·¥ä½œï¼Œè¯·åœ¨å¼€å§‹å‰äºŽ task_plan.md ä¸­æ–°å¢žé˜¶æ®µã€‚"
else
    echo "[planning-with-files] ä»»åŠ¡è¿›è¡Œä¸­ï¼ˆ$COMPLETE/$TOTAL ä¸ªé˜¶æ®µå·²å®Œæˆï¼‰ã€‚åœæ­¢å‰è¯·æ›´æ–° progress.mdã€‚"
    if [ "$IN_PROGRESS" -gt 0 ]; then
        echo "[planning-with-files] $IN_PROGRESS ä¸ªé˜¶æ®µä»åœ¨è¿›è¡Œä¸­ã€‚"
    fi
    if [ "$PENDING" -gt 0 ]; then
        echo "[planning-with-files] $PENDING ä¸ªé˜¶æ®µå¾…å¤„ç†ã€‚"
    fi
fi
exit 0
