# Stock Analysis - Future Enhancements

## Roadmap Overview

### v4.0.0 (Current) - Geopolitical Risk & News Sentiment
âœ… 8 analysis dimensions with Fear/Greed, short interest, VIX structure, put/call ratio
âœ… Safe-haven indicators (GLD, TLT, UUP) with risk-off detection
âœ… Breaking news alerts via Google News RSS
âœ… Geopolitical risk mapping (Taiwan, China, Russia, Middle East, Banking)
âœ… Sector-specific crisis flagging with confidence penalties
âœ… 1h caching for shared indicators (Fear/Greed, VIX structure, breaking news)
âœ… Async parallel sentiment fetching (5 indicators with 10s timeouts)

### v5.0.0 (Current) - Portfolio & Crypto
âœ… Portfolio management (create, add, remove, show assets)
âœ… Cryptocurrency support (Top 20 by market cap)
âœ… Portfolio analysis with --portfolio flag
âœ… Periodic returns (--period daily/weekly/monthly/quarterly/yearly)
âœ… Concentration warnings (>30% single asset)
âœ… Crypto fundamentals (market cap, category, BTC correlation)

### v4.1.0 - Performance & Completeness
âœ… Full insider trading parsing via edgartools (Task #1)
âœ… Market context caching with 1h TTL (Task #3b)
ðŸ”§ SEC EDGAR rate limit monitoring (Task #4 - low priority)

### Future (v6.0+)
ðŸ’¡ Research phase: Social sentiment, fund flows, on-chain metrics

---

## Sentiment Analysis Improvements

### 1. Implement Full Insider Trading Parsing
**Status**: âœ… DONE
**Priority**: Medium
**Effort**: 2-3 hours

**Current State**:
- âœ… `get_insider_activity()` fetches Form 4 filings via edgartools
- âœ… SEC identity configured (`stock-analysis@clawd.bot`)
- âœ… Aggregates buys/sells over 90-day window
- âœ… Scoring logic: strong buying (+0.8), moderate (+0.4), neutral (0), moderate selling (-0.4), strong (-0.8)

**Tasks**:
- [ ] Research edgartools API for Form 4 parsing
- [ ] Implement transaction aggregation (90-day window)
- [ ] Calculate net shares bought/sold
- [ ] Calculate net value in millions USD
- [ ] Apply scoring logic:
  - Strong buying (>100K shares or >$1M): +0.8
  - Moderate buying (>10K shares or >$0.1M): +0.4
  - Neutral: 0
  - Moderate selling: -0.4
  - Strong selling: -0.8
- [ ] Add error handling for missing/incomplete filings
- [ ] Test with multiple tickers (BAC, TSLA, AAPL)
- [ ] Verify SEC rate limit compliance (10 req/s)

**Expected Impact**:
- Insider activity detection for 4th sentiment indicator
- Increase from 3/5 to 4/5 indicators typically available

---

### 2. Add Parallel Async Fetching
**Status**: âœ… DONE (sentiment indicators)
**Priority**: High
**Effort**: 4-6 hours

**Current State**:
- âœ… Sentiment indicators fetched in parallel via `asyncio.gather()`
- âœ… 10s timeout per indicator
- Main data fetches (yfinance) still sequential (acceptable)

**Tasks**:
- [ ] Convert sentiment helper functions to async
  - [ ] `async def get_fear_greed_index()`
  - [ ] `async def get_short_interest(data)`
  - [ ] `async def get_vix_term_structure()`
  - [ ] `async def get_insider_activity(ticker)`
  - [ ] `async def get_put_call_ratio(data)`
- [ ] Update `analyze_sentiment()` to use `asyncio.gather()`
- [ ] Handle yfinance thread safety (may need locks)
- [ ] Add timeout per indicator (10s max)
- [ ] Test with multiple stocks in sequence
- [ ] Measure actual runtime improvement
- [ ] Update SKILL.md with new runtime (target: 3-4s)

**Expected Impact**:
- Reduce runtime from 6-10s to 3-4s per stock
- Better user experience for multi-stock analysis

---

### 3. Add Caching for Shared Indicators
**Status**: âœ… DONE (sentiment + breaking news)
**Priority**: Medium
**Effort**: 2-3 hours

**Current State**:
- âœ… Fear & Greed Index cached (1h TTL)
- âœ… VIX term structure cached (1h TTL)
- âœ… Breaking news cached (1h TTL)
- âœ… Market context (VIX/SPY/QQQ/GLD/TLT/UUP) cached (1h TTL)

**Tasks**:
- [ ] Design cache structure (simple dict or functools.lru_cache)
- [ ] Implement TTL (time-to-live):
  - Fear & Greed: 1 hour
  - VIX structure: 1 hour
  - Short interest: No cache (per-stock)
  - Insider activity: No cache (per-stock)
  - Put/Call ratio: No cache (per-stock)
- [ ] Add cache invalidation logic
- [ ] Add verbose logging for cache hits/misses
- [ ] Test multi-stock analysis (e.g., `BAC TSLA AAPL`)
- [ ] Measure performance improvement
- [ ] Document caching behavior in SKILL.md

**Expected Impact**:
- Multi-stock analysis faster (e.g., 3 stocks: 18-30s â†’ 10-15s)
- Reduced API calls to Fear/Greed and VIX data sources
- Same-session analysis efficiency

---

### 4. Monitor SEC EDGAR Rate Limits
**Status**: Not Started
**Priority**: Low (until insider trading implemented)
**Effort**: 1-2 hours

**Current State**:
- SEC EDGAR API has 10 requests/second rate limit
- No rate limit tracking or logging
- edgartools may handle rate limiting internally

**Tasks**:
- [ ] Research edgartools rate limit handling
- [ ] Add request counter/tracker if needed
- [ ] Implement exponential backoff on 429 errors
- [ ] Add logging for rate limit hits
- [ ] Test with high-volume scenarios (10+ stocks in quick succession)
- [ ] Document rate limit behavior
- [ ] Add error message if rate limited: "SEC API rate limited, try again in 1 minute"

**Expected Impact**:
- Robust handling of SEC API limits in production
- Clear user feedback if limits hit
- Prevent API blocking/banning

---

## Stock Analysis 4.0: Geopolitical Risk & News Sentiment

### What's Currently Missing

The current implementation captures:
- âœ… VIX (general market fear)
- âœ… SPY/QQQ trends (market direction)
- âœ… Sector performance

What we **don't** have yet:
- âŒ Geopolitical risk indicators
- âŒ News sentiment analysis
- âŒ Sector-specific crisis flags

---

### 7. Geopolitical Risk Index
**Status**: âœ… DONE (keyword-based)
**Priority**: High
**Effort**: 8-12 hours

**Proposed Approach**:
Option A: Use GPRD (Geopolitical Risk Daily Index) from policyuncertainty.com
Option B: Scan news APIs (NewsAPI, GDELT) for geopolitical keywords

**Tasks**:
- [ ] Research free geopolitical risk data sources
  - [ ] Check policyuncertainty.com API availability
  - [ ] Evaluate NewsAPI free tier limits
  - [ ] Consider GDELT Project (free, comprehensive)
- [ ] Design risk scoring system (0-100 scale)
- [ ] Implement data fetching with caching (4-hour TTL)
- [ ] Map risk levels to sentiment scores:
  - Low risk (0-30): +0.2 (bullish)
  - Moderate risk (30-60): 0 (neutral)
  - High risk (60-80): -0.3 (caution)
  - Extreme risk (80-100): -0.5 (bearish)
- [ ] Add to sentiment analysis as 6th indicator
- [ ] Test with historical crisis periods
- [ ] Update SKILL.md with geopolitical indicator

**Expected Impact**:
- Early warning for market-wide risk events
- Better context for earnings-season volatility
- Complement to VIX (VIX is reactive, geopolitical is predictive)

**Example Output**:
```
âš ï¸ GEOPOLITICAL RISK: HIGH (72/100)
   Context: Elevated Taiwan tensions detected
   Market Impact: Risk-off sentiment likely
```

---

### 8. Sector-Specific Crisis Mapping
**Status**: âœ… DONE
**Priority**: High
**Effort**: 6-8 hours

**Current Gap**:
- No mapping between geopolitical events and affected sectors
- No automatic flagging of at-risk holdings

**Proposed Risk Mapping**:

| Geopolitical Event | Affected Sectors | Example Tickers |
|-------------------|------------------|-----------------|
| Taiwan conflict | Semiconductors | NVDA, AMD, TSM, INTC |
| Russia-Ukraine | Energy, Agriculture | XLE, MOS, CF, NTR |
| Middle East escalation | Oil, Defense | XOM, CVX, LMT, RTX |
| China tensions | Tech supply chain, Retail | AAPL, QCOM, NKE, SBUX |
| Banking crisis | Financials | JPM, BAC, WFC, C |

**Tasks**:
- [ ] Build event â†’ sector â†’ ticker mapping database
- [ ] Implement keyword detection in news feeds:
  - "Taiwan" + "military" â†’ Semiconductors âš ï¸
  - "Russia" + "sanctions" â†’ Energy âš ï¸
  - "Iran" + "attack" â†’ Oil, Defense âš ï¸
  - "China" + "tariffs" â†’ Tech, Consumer âš ï¸
- [ ] Add sector exposure check to analysis
- [ ] Generate automatic warnings in output
- [ ] Apply confidence penalty for high-risk sectors
- [ ] Test with historical crisis events
- [ ] Document in SKILL.md

**Expected Impact**:
- Automatic detection of sector-specific risks
- Clear warnings for exposed holdings
- Reduced false positives (only flag relevant sectors)

**Example Output**:
```
âš ï¸ SECTOR RISK ALERT: Semiconductors
   Event: Taiwan military exercises (elevated tensions)
   Impact: NVDA HIGH RISK - supply chain exposure
   Recommendation: HOLD â†’ downgraded from BUY
```

---

### 9. Breaking News Check
**Status**: âœ… DONE
**Priority**: Medium
**Effort**: 4-6 hours

**Current Gap**:
- No real-time news scanning before analysis
- User might get stale recommendation during breaking events

**Proposed Solution**:
- Scan Google News or Reuters RSS before analysis
- Flag high-impact keywords within last 24 hours

**Tasks**:
- [ ] Choose news source (Google News RSS, Reuters API, or NewsAPI)
- [ ] Implement news fetching with 24-hour lookback
- [ ] Define crisis keywords:
  - **War/Conflict**: "war", "invasion", "military strike", "attack"
  - **Economic**: "recession", "crisis", "collapse", "default"
  - **Regulatory**: "sanctions", "embargo", "ban", "investigation"
  - **Natural disaster**: "earthquake", "hurricane", "pandemic"
- [ ] Add ticker-specific news check (company name + keywords)
- [ ] Generate automatic caveat in output
- [ ] Cache news check results (1 hour TTL)
- [ ] Add `--skip-news` flag for offline mode
- [ ] Test with historical crisis dates
- [ ] Document in SKILL.md

**Expected Impact**:
- Real-time awareness of breaking events
- Automatic caveats during high volatility
- User protection from stale recommendations

**Example Output**:
```
âš ï¸ BREAKING NEWS ALERT (last 6 hours):
   "Fed announces emergency rate hike"
   Impact: Market-wide volatility expected
   Caveat: Analysis may be outdated - rerun in 24h
```

---

### 10. Safe-Haven Indicators
**Status**: âœ… DONE
**Priority**: Medium
**Effort**: 3-4 hours

**Current Gap**:
- No detection of "risk-off" market regime
- VIX alone is insufficient (measures implied volatility, not capital flows)

**Proposed Indicators**:
- Gold (GLD) - Flight to safety
- US Treasuries (TLT) - Bond market fear
- USD Index (UUP) - Dollar strength during crisis

**Risk-Off Detection Logic**:
```
IF GLD +2% AND TLT +1% AND UUP +1% (all rising together)
THEN Market Regime = RISK-OFF
```

**Tasks**:
- [ ] Fetch GLD, TLT, UUP price data (5-day change)
- [ ] Implement risk-off detection algorithm
- [ ] Add to market context analysis
- [ ] Apply broad risk penalty:
  - Risk-off detected â†’ Reduce all BUY confidence by 30%
  - Add caveat: "Market in risk-off mode - defensive positioning recommended"
- [ ] Test with historical crisis periods (2008, 2020, 2022)
- [ ] Add verbose output for safe-haven movements
- [ ] Document in SKILL.md

**Expected Impact**:
- Detect market-wide flight to safety
- Automatic risk reduction during panics
- Complement geopolitical risk scoring

**Example Output**:
```
ðŸ›¡ï¸ SAFE-HAVEN ALERT: Risk-off mode detected
   - Gold (GLD): +3.2% (5d)
   - Treasuries (TLT): +2.1% (5d)
   - USD Index: +1.8% (5d)
   Recommendation: Reduce equity exposure, favor defensives
```

---

## General Improvements

### 11. Add Social Sentiment (Future Phase)
**Status**: Deferred
**Priority**: Low
**Effort**: 8-12 hours

**Notes**:
- Requires free API (Twitter/Reddit alternatives?)
- Most sentiment APIs are paid (StockTwits, etc.)
- Research needed for viable free sources

### 12. Add Fund Flows (Future Phase)
**Status**: Deferred
**Priority**: Low
**Effort**: 6-8 hours

**Notes**:
- Requires ETF flow data
- May need paid data source
- Research free alternatives

---

## Implementation Priorities

### v4.1.0 Complete
- âœ… Task #1 - Insider trading parsing via edgartools
- âœ… Task #3b - Market context caching (1h TTL)
- ðŸ”§ Task #4 - SEC EDGAR rate limits (low priority, only if hitting limits)

### Completed in v4.0.0
- âœ… Task #2 - Async parallel fetching (sentiment)
- âœ… Task #3 - Caching for shared indicators (sentiment + news)
- âœ… Task #7 - Geopolitical risk (keyword-based)
- âœ… Task #8 - Sector-specific crisis mapping
- âœ… Task #9 - Breaking news check
- âœ… Task #10 - Safe-haven indicators

---

## Version History

- **v5.0.0** (2026-01-16): Portfolio management, cryptocurrency support (Top 20), periodic analysis
- **v4.1.0** (2026-01-16): Full insider trading parsing via edgartools, market context caching
- **v4.0.0** (2026-01-15): Geopolitical risk, breaking news, safe-haven detection, sector crisis mapping
- **v3.0.0** (2026-01-15): Sentiment analysis added with 5 indicators (3-4 typically working)
- **v2.0.0**: Market context, sector performance, earnings timing, momentum
- **v1.0.0**: Initial release with earnings, fundamentals, analysts, historical
