#!/usr/bin/env bash
# æª¢æŸ¥ task_plan.md ä¸­æ‰€æœ‰éšŽæ®µæ˜¯å¦å®Œæˆ
# å§‹çµ‚ä»¥é€€å‡ºç¢¼ 0 çµæŸ â€” ä½¿ç”¨æ¨™æº–è¼¸å‡ºå›žå ±ç‹€æ…‹
# ç”± Stop é‰¤å­å‘¼å«ä»¥å›žå ±ä»»å‹™å®Œæˆç‹€æ…‹

PLAN_FILE="${1:-task_plan.md}"

if [ ! -f "$PLAN_FILE" ]; then
    echo "[planning-with-files] æœªæ‰¾åˆ° task_plan.md â€” æ²’æœ‰é€²è¡Œä¸­çš„è¦åŠƒæœƒè©±ã€‚"
    exit 0
fi

# è¨ˆç®—éšŽæ®µç¸½æ•¸
TOTAL=$(grep -c "### éšŽæ®µ" "$PLAN_FILE" || true)

# å…ˆæª¢æŸ¥ **ç‹€æ…‹ï¼š** æ ¼å¼
COMPLETE=$(grep -cF "**ç‹€æ…‹ï¼š** complete" "$PLAN_FILE" || true)
IN_PROGRESS=$(grep -cF "**ç‹€æ…‹ï¼š** in_progress" "$PLAN_FILE" || true)
PENDING=$(grep -cF "**ç‹€æ…‹ï¼š** pending" "$PLAN_FILE" || true)

# å‚™ç”¨ï¼šå¦‚æžœæœªæ‰¾åˆ° **ç‹€æ…‹ï¼š** å‰‡æª¢æŸ¥ [complete] è¡Œå…§æ ¼å¼
if [ "$COMPLETE" -eq 0 ] && [ "$IN_PROGRESS" -eq 0 ] && [ "$PENDING" -eq 0 ]; then
    COMPLETE=$(grep -c "\[complete\]" "$PLAN_FILE" || true)
    IN_PROGRESS=$(grep -c "\[in_progress\]" "$PLAN_FILE" || true)
    PENDING=$(grep -c "\[pending\]" "$PLAN_FILE" || true)
fi

# é è¨­ç‚º 0ï¼ˆå¦‚æžœç‚ºç©ºï¼‰
: "${TOTAL:=0}"
: "${COMPLETE:=0}"
: "${IN_PROGRESS:=0}"
: "${PENDING:=0}"

# å›žå ±ç‹€æ…‹ï¼ˆå§‹çµ‚ä»¥é€€å‡ºç¢¼ 0 çµæŸ â€” æœªå®Œæˆçš„ä»»å‹™æ˜¯æ­£å¸¸ç‹€æ…‹ï¼‰
if [ "$COMPLETE" -eq "$TOTAL" ] && [ "$TOTAL" -gt 0 ]; then
    echo "[planning-with-files] æ‰€æœ‰éšŽæ®µå·²å®Œæˆï¼ˆ$COMPLETE/$TOTALï¼‰ã€‚å¦‚æžœä½¿ç”¨è€…æœ‰é¡å¤–å·¥ä½œï¼Œè«‹åœ¨é–‹å§‹å‰æ–¼ task_plan.md ä¸­æ–°å¢žéšŽæ®µã€‚"
else
    echo "[planning-with-files] ä»»å‹™é€²è¡Œä¸­ï¼ˆ$COMPLETE/$TOTAL å€‹éšŽæ®µå·²å®Œæˆï¼‰ã€‚åœæ­¢å‰è«‹æ›´æ–° progress.mdã€‚"
    if [ "$IN_PROGRESS" -gt 0 ]; then
        echo "[planning-with-files] $IN_PROGRESS å€‹éšŽæ®µä»åœ¨é€²è¡Œä¸­ã€‚"
    fi
    if [ "$PENDING" -gt 0 ]; then
        echo "[planning-with-files] $PENDING å€‹éšŽæ®µå¾…è™•ç†ã€‚"
    fi
fi
exit 0
