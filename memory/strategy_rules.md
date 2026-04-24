# Hard Strategy Rules - MNQ Golden Candle Bot (Grok must obey these 100% of the time)

## Account & Risk Rules (never break)
- Account type: PAPER / SIM trading until further notice
- Instrument: MNQ (Micro E-mini Nasdaq-100 futures) ONLY
- Max risk per trade: 1% of account equity (calculated from stop distance)
- Max total open risk: 2%
- Always use hard stop-loss (never widen or remove)
- Minimum risk-reward: 1:2 (3-tier targets preferred)
- Max 6 contracts per trade (scale only on strong setups)
- Flat all positions by 15:45 ET (no overnight holds)
- Daily loss limit: Stop trading if down >2%

## Trading Session
- Only Regular Trading Hours: 9:30 – 16:00 ET (futures)
- Highest probability windows: first 90–120 min after open + last 90 min before close
- Avoid trading 30 min before/after major news or FOMC

## Core Strategy: 5-Min Trend Bias + 1-Min Golden Candle Scalp
- Trend filter: 5-minute chart
- Execution & confirmation: 1-minute chart
- Goal: 3–6 high-probability Golden Candle setups per day

### Trend filter (5M chart)
- Bullish: Price above 9 EMA and 21 EMA + 9 EMA sloping upward + MACD histogram expanding positive
- Bearish: Price below 9 EMA and 21 EMA + 9 EMA sloping downward + MACD histogram expanding negative

### Golden Candle Entry Rules (ALL must align)
- 5-minute chart shows clear trend bias (as defined above)
- On the 1-minute chart, price pulls back to the 9 EMA or Alpha Zone support/resistance
- Strong momentum reversal candle (large body, small wick, closes in direction of trend — “Golden Candle”)
- Volume spike on the entry candle (clearly above average / “Volume Bubble”)
- RSI(14) on 5M not extreme (>70 for longs, <30 for shorts)
- Market structure alignment (higher-timeframe swing break or trend wave continuation)

### Exit Rules (3-tier targets)
- Stop-loss: 0.75–1.25% or just beyond recent 1M swing (tighter on strong momentum)
- Take-Profit Tier 1: 1:1 R:R
- Take-Profit Tier 2: 1:2 R:R
- Take-Profit Tier 3: 1:3 R:R or next major level
- Optional: Move stop to breakeven after Tier 1 hit, then trail 9 EMA on 1M
- Max hold: 30 minutes

## Best Practices Built In
- Only A+ Golden Candle setups (all rules required)
- Focus on high-volume windows
- No revenge trading
- All decisions logged with full reasoning
- Strategy can only be changed by user instruction

Current preferred style: "5-Min Trend Bias + 1-Min Golden Candle Momentum Scalp on MNQ — high-probability, rule-based, institutional-style entries only"
