# æ£€æŸ¥ task_plan.md ä¸­æ‰€æœ‰é˜¶æ®µæ˜¯å¦å®Œæˆ
# å§‹ç»ˆä»¥é€€å‡ºç  0 ç»“æŸ â€” ä½¿ç”¨æ ‡å‡†è¾“å‡ºæŠ¥å‘ŠçŠ¶æ€
# ç”± Stop é’©å­è°ƒç”¨ä»¥æŠ¥å‘Šä»»åŠ¡å®ŒæˆçŠ¶æ€

param(
    [string]$PlanFile = "task_plan.md"
)

if (-not (Test-Path $PlanFile)) {
    Write-Host '[planning-with-files] æœªæ‰¾åˆ° task_plan.md â€” æ²¡æœ‰è¿›è¡Œä¸­çš„è§„åˆ’ä¼šè¯ã€‚'
    exit 0
}

# è¯»å–æ–‡ä»¶å†…å®¹
$content = Get-Content $PlanFile -Raw

# è®¡ç®—é˜¶æ®µæ€»æ•°
$TOTAL = ([regex]::Matches($content, "### é˜¶æ®µ")).Count

# å…ˆæ£€æŸ¥ **çŠ¶æ€ï¼š** æ ¼å¼
$COMPLETE = ([regex]::Matches($content, "\*\*çŠ¶æ€ï¼š\*\* complete")).Count
$IN_PROGRESS = ([regex]::Matches($content, "\*\*çŠ¶æ€ï¼š\*\* in_progress")).Count
$PENDING = ([regex]::Matches($content, "\*\*çŠ¶æ€ï¼š\*\* pending")).Count

# å¤‡ç”¨ï¼šå¦‚æžœæœªæ‰¾åˆ° **çŠ¶æ€ï¼š** åˆ™æ£€æŸ¥ [complete] è¡Œå†…æ ¼å¼
if ($COMPLETE -eq 0 -and $IN_PROGRESS -eq 0 -and $PENDING -eq 0) {
    $COMPLETE = ([regex]::Matches($content, "\[complete\]")).Count
    $IN_PROGRESS = ([regex]::Matches($content, "\[in_progress\]")).Count
    $PENDING = ([regex]::Matches($content, "\[pending\]")).Count
}

# æŠ¥å‘ŠçŠ¶æ€ â€” å§‹ç»ˆä»¥é€€å‡ºç  0 ç»“æŸï¼Œæœªå®Œæˆçš„ä»»åŠ¡æ˜¯æ­£å¸¸çŠ¶æ€
if ($COMPLETE -eq $TOTAL -and $TOTAL -gt 0) {
    Write-Host ('[planning-with-files] æ‰€æœ‰é˜¶æ®µå·²å®Œæˆï¼ˆ' + $COMPLETE + '/' + $TOTAL + 'ï¼‰ã€‚å¦‚æžœç”¨æˆ·æœ‰é¢å¤–å·¥ä½œï¼Œè¯·åœ¨å¼€å§‹å‰äºŽ task_plan.md ä¸­æ–°å¢žé˜¶æ®µã€‚')
} else {
    Write-Host ('[planning-with-files] ä»»åŠ¡è¿›è¡Œä¸­ï¼ˆ' + $COMPLETE + '/' + $TOTAL + ' ä¸ªé˜¶æ®µå·²å®Œæˆï¼‰ã€‚åœæ­¢å‰è¯·æ›´æ–° progress.mdã€‚')
    if ($IN_PROGRESS -gt 0) {
        Write-Host ('[planning-with-files] ' + $IN_PROGRESS + ' ä¸ªé˜¶æ®µä»åœ¨è¿›è¡Œä¸­ã€‚')
    }
    if ($PENDING -gt 0) {
        Write-Host ('[planning-with-files] ' + $PENDING + ' ä¸ªé˜¶æ®µå¾…å¤„ç†ã€‚')
    }
}
exit 0
