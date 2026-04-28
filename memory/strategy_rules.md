# Hard Strategy Rules - MNQ Scalping Bot (Grok must obey these 100% of the time)

## Account & Risk Rules (never break)
- Account type: PAPER / SIM trading until further notice
- Instrument: MNQ (Micro E-mini Nasdaq-100 futures) ONLY
- Max risk per trade: 1% of account equity (based on stop distance)
- Max total open risk: 2%
- Always use hard stop-loss (never widen or remove)
- Minimum risk-reward: 1:2
- Max 6 contracts per trade
- Flat all positions by 15:45 ET (no overnight holds)
- Daily loss limit: Stop trading if down >2%

## Trading Session
- Only Regular Trading Hours: 9:30 – 16:00 ET
- Focus on highest-probability windows: first 90–120 min after open + last 90 min before close
- Avoid trading 30 min before/after major news or FOMC

## Core Strategy: 5-Min Trend Bias + 1-Min VWAP/EMA Pullback Scalp
- Trend filter: 5-minute chart
- Execution: 1-minute chart
- Goal: 3–8 scalps per day on MNQ

### Trend Filter (5M chart)
- Bullish: Price above VWAP + 9 EMA above 21 EMA and sloping upward
- Bearish: Price below VWAP + 9 EMA below 21 EMA and sloping downward

### Entry Rules (ALL must align)
- 5-minute chart shows clear trend bias (as defined above)
- On the 1-minute chart, price pulls back to VWAP or the 9 EMA (whichever is closer) in the direction of the 5M trend
- Strong reversal candle on 1-minute (large body, closes in direction of trend)
- Volume spike on the entry candle (above average)

### Exit Rules (mandatory)
- Stop-loss: 8–12 points or just beyond the recent 1M swing (tighter wins)
- Take-profit: Minimum 1:2 R:R (Tier 1 at 1:1, Tier 2 at 1:2 or next major level)
- Trailing stop: Move to breakeven after +1R, then trail 9 EMA on the 5-minute chart
- Max hold: 25 minutes

## Best Practices Built In
- Only A+ setups (all entry rules required)
- No revenge trading
- All decisions logged with full reasoning
- Strategy can only be changed by user instruction

Current preferred style: "5-Min Trend Bias + 1-Min VWAP/EMA Pullback Scalp on MNQ — high-probability momentum scalps with institutional VWAP alignment"

These rules are non-negotiable. Grok must follow them exactly on every trade via Tradovate.
