# Hard Strategy Rules - MNQ ORB Bot (Grok must obey these 100% of the time)

## Account & Risk Rules (never break)
- Account type: PAPER / SIM trading until further notice
- Instrument: MNQ (Micro E-mini Nasdaq-100 futures) ONLY
- Max risk per trade: 1% of account equity (calculated from stop distance)
- Max total open risk: 2%
- Always use hard stop-loss (never widen or remove)
- Minimum risk-reward: 1:2
- Max 6 contracts per trade
- Flat all positions by 15:45 ET (no overnight holds)
- Daily loss limit: Stop trading if down >2%

## Trading Session
- Only Regular Trading Hours: 9:30 – 16:00 ET
- Highest probability windows: first 90–120 min after open + last 90 min before close
- Avoid trading 30 min before/after major news or FOMC

## Core Strategy: 15-Minute Opening Range Breakout (ORB) on MNQ
- Define the 15-minute Opening Range (9:30–9:45 ET) on the 1-minute chart
- Goal: Take only high-probability ORB setups each day

### Entry Rules (ALL must align - pure ORB)
- The 15-minute Opening Range is defined as the high and low from 9:30–9:45 ET
- Long entry: Price breaks and closes above the OR High on a 1-minute candle
- Short entry: Price breaks and closes below the OR Low on a 1-minute candle
- Volume spike on the breakout candle (above average)

### Exit Rules (mandatory)
- Stop-loss: Opposite side of the 15-min OR or 8–12 points (whichever is tighter)
- Take-profit: Minimum 1:2 R:R (Tier 1 at 1:1, Tier 2 at 1:2 or next major level)
- Trailing stop: Move stop to breakeven after +1R is reached, then trail using 9 EMA on the 5-minute chart
- Max hold: 45 minutes

## Best Practices Built In
- Only A+ ORB setups (all entry rules required)
- Focus on the two highest-volume windows
- No revenge trading
- All decisions must be logged with full reasoning
- Strategy can only be changed by user instruction

Current preferred style: "15-Minute Opening Range Breakout on MNQ — pure price and volume, disciplined entries only"

These rules are non-negotiable. Grok must follow them exactly on every trade via Tradovate.
