# Hard Strategy Rules - MNQ (Grok must obey these 100% of the time)

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

# MNQ 1-Minute Bot Strategy Rules

## Core Configuration
- Symbol: MNQ (Micro Nasdaq-100)
- Timeframe: 1 Minute (1M)
- Session: New York Open (09:30 - 16:00 EST)

## Technical Indicators
- EMA_Fast: 9 period
- EMA_Slow: 200 period (Trend Filter)
- Anchor: VWAP (Volume Weighted Average Price)
- Volatility: ATR 14

## Entry Logic (Binary Conditions)
1. Trend: Close > EMA_200 AND Close > VWAP = LONG_BIAS
2. Setup: Price touches EMA_9 and bounces.
3. Trigger: Enter Market when Current_Price > High_of_Last_Candle.

## Risk Management
- Max_Daily_Loss: $100 (Stop bot if hit)
- Max_Open_Trades: 1
- Position_Size: 1 Contract
- Stop_Loss: 40 Ticks (10 Points)
- Take_Profit: 60 Ticks (15 Points)

## No-Trade Zones
- Do not trade 5 minutes before/after High Impact News (CPI, FOMC).
- Do not trade if Spread > 4 ticks.
- Do not trade after 3 consecutive losses in one session.

