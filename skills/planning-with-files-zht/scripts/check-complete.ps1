# æª¢æŸ¥ task_plan.md ä¸­æ‰€æœ‰éšŽæ®µæ˜¯å¦å®Œæˆ
# å§‹çµ‚ä»¥é€€å‡ºç¢¼ 0 çµæŸ â€” ä½¿ç”¨æ¨™æº–è¼¸å‡ºå›žå ±ç‹€æ…‹
# ç”± Stop é‰¤å­å‘¼å«ä»¥å›žå ±ä»»å‹™å®Œæˆç‹€æ…‹

param(
    [string]$PlanFile = "task_plan.md"
)

if (-not (Test-Path $PlanFile)) {
    Write-Host '[planning-with-files] æœªæ‰¾åˆ° task_plan.md â€” æ²’æœ‰é€²è¡Œä¸­çš„è¦åŠƒæœƒè©±ã€‚'
    exit 0
}

# è®€å–æª”æ¡ˆå…§å®¹
$content = Get-Content $PlanFile -Raw

# è¨ˆç®—éšŽæ®µç¸½æ•¸
$TOTAL = ([regex]::Matches($content, "### éšŽæ®µ")).Count

# å…ˆæª¢æŸ¥ **ç‹€æ…‹ï¼š** æ ¼å¼
$COMPLETE = ([regex]::Matches($content, "\*\*ç‹€æ…‹ï¼š\*\* complete")).Count
$IN_PROGRESS = ([regex]::Matches($content, "\*\*ç‹€æ…‹ï¼š\*\* in_progress")).Count
$PENDING = ([regex]::Matches($content, "\*\*ç‹€æ…‹ï¼š\*\* pending")).Count

# å‚™ç”¨ï¼šå¦‚æžœæœªæ‰¾åˆ° **ç‹€æ…‹ï¼š** å‰‡æª¢æŸ¥ [complete] è¡Œå…§æ ¼å¼
if ($COMPLETE -eq 0 -and $IN_PROGRESS -eq 0 -and $PENDING -eq 0) {
    $COMPLETE = ([regex]::Matches($content, "\[complete\]")).Count
    $IN_PROGRESS = ([regex]::Matches($content, "\[in_progress\]")).Count
    $PENDING = ([regex]::Matches($content, "\[pending\]")).Count
}

# å›žå ±ç‹€æ…‹ â€” å§‹çµ‚ä»¥é€€å‡ºç¢¼ 0 çµæŸï¼Œæœªå®Œæˆçš„ä»»å‹™æ˜¯æ­£å¸¸ç‹€æ…‹
if ($COMPLETE -eq $TOTAL -and $TOTAL -gt 0) {
    Write-Host ('[planning-with-files] æ‰€æœ‰éšŽæ®µå·²å®Œæˆï¼ˆ' + $COMPLETE + '/' + $TOTAL + 'ï¼‰ã€‚å¦‚æžœä½¿ç”¨è€…æœ‰é¡å¤–å·¥ä½œï¼Œè«‹åœ¨é–‹å§‹å‰æ–¼ task_plan.md ä¸­æ–°å¢žéšŽæ®µã€‚')
} else {
    Write-Host ('[planning-with-files] ä»»å‹™é€²è¡Œä¸­ï¼ˆ' + $COMPLETE + '/' + $TOTAL + ' å€‹éšŽæ®µå·²å®Œæˆï¼‰ã€‚åœæ­¢å‰è«‹æ›´æ–° progress.mdã€‚')
    if ($IN_PROGRESS -gt 0) {
        Write-Host ('[planning-with-files] ' + $IN_PROGRESS + ' å€‹éšŽæ®µä»åœ¨é€²è¡Œä¸­ã€‚')
    }
    if ($PENDING -gt 0) {
        Write-Host ('[planning-with-files] ' + $PENDING + ' å€‹éšŽæ®µå¾…è™•ç†ã€‚')
    }
}
exit 0
