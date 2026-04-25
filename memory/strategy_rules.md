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

# MNQ 1M Scalping Strategy Rules (Bot)

## 1. Context & Timing
- **Instrument:** /MNQ (Micro E-mini Nasdaq-100)
- **Timeframe:** 1 Minute (1M)
- **Time Window:** 9:30 AM – 11:00 AM ET (High Volatility)
- **Market State:** Active only when Volume > 20-period average.

## 2. Setup Conditions (Filters)
- **Trend Filter:** Price must be above 200 SMA (Long only) or below 200 SMA (Short only).
- **Momentum Filter:** 9 EMA > 21 EMA (Bullish) or 9 EMA < 21 EMA (Bearish).

## 3. Entry Rules
- **Long:** Price retests 9 EMA after breaking above it, with a green engulfing candle.
- **Short:** Price retests 9 EMA after breaking below it, with a red engulfing candle.
- **Alternative (Breakout):** Enter if 1M candle closes > 15-min High (Long) or < 15-min Low (Short) with high volume.

## 4. Risk Management (Per Trade)
- **Stop Loss (SL):** 10-15 points (approx. $20-$30 per contract).
- **Take Profit (TP):** 15-20 points (1:1.5 Risk/Reward).
- **Max Daily Loss:** Close bot after 3 consecutive losses or -50 points total loss.
- **Position Size:** 1-2 Contracts (max) to start.

## 5. Exit Rules
- **Automatic:** TP or SL hit.
- **Exit Early:** 9 EMA crosses back over 21 EMA (trend reversal) or 2 consecutive opposite-color candles form.

## Best Practices Built In
- Focus on high-volume windows
- No revenge trading
- All decisions logged with full reasoning
- Strategy can only be changed by user instruction

Current preferred style: "5-Min Trend Bias + 1-Min Golden Candle Momentum Scalp on MNQ — high-probability, rule-based, institutional-style entries only"
