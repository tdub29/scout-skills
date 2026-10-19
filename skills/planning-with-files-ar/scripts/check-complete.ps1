# Ø§Ù„ØªØ­Ù‚Ù‚ Ù…Ù† Ø§ÙƒØªÙ…Ø§Ù„ Ø¬Ù…ÙŠØ¹ Ø§Ù„Ù…Ø±Ø§Ø­Ù„ ÙÙŠ task_plan.md
# ÙŠÙ†Ù‡ÙŠ Ø¯Ø§Ø¦Ù…Ù‹Ø§ Ø¨Ø±Ù…Ø² Ø®Ø±ÙˆØ¬ 0 â€” ÙŠØ³ØªØ®Ø¯Ù… stdout Ù„Ù„Ø¥Ø¨Ù„Ø§Øº Ø¹Ù† Ø§Ù„Ø­Ø§Ù„Ø©
# ÙŠÙØ³ØªØ¯Ø¹Ù‰ Ø¨ÙˆØ§Ø³Ø·Ø© Ø®Ø·Ø§Ù Stop Ù„Ù„Ø¥Ø¨Ù„Ø§Øº Ø¹Ù† Ø­Ø§Ù„Ø© Ø§ÙƒØªÙ…Ø§Ù„ Ø§Ù„Ù…Ù‡Ù…Ø©

param(
    [string]$PlanFile = "task_plan.md"
)

if (-not (Test-Path $PlanFile)) {
    Write-Host '[planning-with-files-ar] Ù„Ù… ÙŠØªÙ… Ø§Ù„Ø¹Ø«ÙˆØ± Ø¹Ù„Ù‰ task_plan.md â€” Ù„Ø§ ØªÙˆØ¬Ø¯ Ø¬Ù„Ø³Ø© ØªØ®Ø·ÙŠØ· Ù†Ø´Ø·Ø©.'
    exit 0
}

# Ù‚Ø±Ø§Ø¡Ø© Ù…Ø­ØªÙˆÙ‰ Ø§Ù„Ù…Ù„Ù
$content = Get-Content $PlanFile -Raw

# Ø­Ø³Ø§Ø¨ Ø¥Ø¬Ù…Ø§Ù„ÙŠ Ø¹Ø¯Ø¯ Ø§Ù„Ù…Ø±Ø§Ø­Ù„
$TOTAL = ([regex]::Matches($content, "### Ø§Ù„Ù…Ø±Ø­Ù„Ø©")).Count

# Ø§Ù„ØªØ­Ù‚Ù‚ Ø£ÙˆÙ„Ø§Ù‹ Ù…Ù† ØªÙ†Ø³ÙŠÙ‚ **Ø§Ù„Ø­Ø§Ù„Ø©:**
$COMPLETE = ([regex]::Matches($content, "\*\*Ø§Ù„Ø­Ø§Ù„Ø©:\*\* complete")).Count
$IN_PROGRESS = ([regex]::Matches($content, "\*\*Ø§Ù„Ø­Ø§Ù„Ø©:\*\* in_progress")).Count
$PENDING = ([regex]::Matches($content, "\*\*Ø§Ù„Ø­Ø§Ù„Ø©:\*\* pending")).Count

# Ø¨Ø¯ÙŠÙ„: Ø¥Ø°Ø§ Ù„Ù… ÙŠØªÙ… Ø§Ù„Ø¹Ø«ÙˆØ± Ø¹Ù„Ù‰ **Ø§Ù„Ø­Ø§Ù„Ø©:** ÙØªØ­Ù‚Ù‚ Ù…Ù† ØªÙ†Ø³ÙŠÙ‚ [complete] Ø§Ù„Ù…Ø¶Ù…Ù†
if ($COMPLETE -eq 0 -and $IN_PROGRESS -eq 0 -and $PENDING -eq 0) {
    $COMPLETE = ([regex]::Matches($content, "\[complete\]")).Count
    $IN_PROGRESS = ([regex]::Matches($content, "\[in_progress\]")).Count
    $PENDING = ([regex]::Matches($content, "\[pending\]")).Count
}

# Ø§Ù„Ø¥Ø¨Ù„Ø§Øº Ø¹Ù† Ø§Ù„Ø­Ø§Ù„Ø© â€” ÙŠÙ†Ù‡ÙŠ Ø¯Ø§Ø¦Ù…Ù‹Ø§ Ø¨Ø±Ù…Ø² Ø®Ø±ÙˆØ¬ 0ØŒ Ø§Ù„Ù…Ù‡Ø§Ù… ØºÙŠØ± Ø§Ù„Ù…ÙƒØªÙ…Ù„Ø© Ø­Ø§Ù„Ø© Ø·Ø¨ÙŠØ¹ÙŠØ©
if ($COMPLETE -eq $TOTAL -and $TOTAL -gt 0) {
    Write-Host ('[planning-with-files-ar] Ø§ÙƒØªÙ…Ù„Øª Ø¬Ù…ÙŠØ¹ Ø§Ù„Ù…Ø±Ø§Ø­Ù„ (' + $COMPLETE + '/' + $TOTAL + '). Ø¥Ø°Ø§ ÙƒØ§Ù† Ù„Ø¯Ù‰ Ø§Ù„Ù…Ø³ØªØ®Ø¯Ù… Ø¹Ù…Ù„ Ø¥Ø¶Ø§ÙÙŠØŒ Ø£Ø¶Ù Ù…Ø±Ø§Ø­Ù„ ÙÙŠ task_plan.md Ù‚Ø¨Ù„ Ø§Ù„Ø¨Ø¯Ø¡.')
} else {
    Write-Host ('[planning-with-files-ar] Ø§Ù„Ù…Ù‡Ù…Ø© Ù‚ÙŠØ¯ Ø§Ù„ØªÙ†ÙÙŠØ° (' + $COMPLETE + '/' + $TOTAL + ' Ù…Ø±Ø­Ù„Ø© Ù…ÙƒØªÙ…Ù„Ø©). Ø­Ø¯Ù‘Ø« progress.md Ù‚Ø¨Ù„ Ø§Ù„ØªÙˆÙ‚Ù.')
    if ($IN_PROGRESS -gt 0) {
        Write-Host ('[planning-with-files-ar] ' + $IN_PROGRESS + ' Ù…Ø±Ø­Ù„Ø©/Ù…Ø±Ø§Ø­Ù„ Ù„Ø§ ØªØ²Ø§Ù„ Ù‚ÙŠØ¯ Ø§Ù„ØªÙ†ÙÙŠØ°.')
    }
    if ($PENDING -gt 0) {
        Write-Host ('[planning-with-files-ar] ' + $PENDING + ' Ù…Ø±Ø­Ù„Ø©/Ù…Ø±Ø§Ø­Ù„ Ù…Ø¹Ù„Ù‚Ø©.')
    }
}
exit 0
