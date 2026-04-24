import os
import json
from datetime import datetime
from zoneinfo import ZoneInfo
import smtplib
from email.mime.text import MIMEText
import requests

# Load secrets
GROK_API_KEY = os.getenv("GROK_API_KEY")
TRADOVATE_API_KEY = os.getenv("TRADOVATE_API_KEY")   # Your Tradovate API Key
TRADOVATE_USERNAME = os.getenv("TRADOVATE_USERNAME") # Tradovate login username
TRADOVATE_PASSWORD = os.getenv("TRADOVATE_PASSWORD") # Tradovate login password
TRADOVATE_APP_ID = os.getenv("TRADOVATE_APP_ID", "grok-mnq-bot")  # Any name you want

# Email settings (same as Alpaca bot)
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")

ET = ZoneInfo("America/New_York")

def get_tradovate_token():
    url = "https://live.tradovateapi.com/v1/auth/accessToken"
    payload = {
        "name": TRADOVATE_APP_ID,
        "apiKey": TRADOVATE_API_KEY,
        "username": TRADOVATE_USERNAME,
        "password": TRADOVATE_PASSWORD
    }
    resp = requests.post(url, json=payload)
    resp.raise_for_status()
    return resp.json()["accessToken"]

def place_mnq_order(token, side, qty=1):
    url = "https://live.tradovateapi.com/v1/order/placeOrder"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "accountSpec": TRADOVATE_USERNAME,
        "accountId": 0,  # Will be filled by Tradovate
        "symbol": "MNQ",
        "side": side.upper(),
        "orderQty": qty,
        "orderType": "Market",
        "timeInForce": "Day"
    }
    resp = requests.post(url, json=payload, headers=headers)
    return resp.json()

def load_memory(file):
    path = f"memory/{file}"
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def save_memory(file, content):
    with open(f"memory/{file}", "w", encoding="utf-8") as f:
        f.write(content)

def send_daily_email(routine_type, content):
  print(f"📧 DEBUG: Attempting to send email for routine: '{routine_type}'")
    if not all([EMAIL_HOST, EMAIL_USER, EMAIL_PASS, EMAIL_TO]):
        print("⚠️ Email settings not fully configured - skipping")
        return
    today = datetime.now(ET).strftime("%Y-%m-%d")
    body = f"""
🟢 Grok Trading Bot — {routine_type.upper()} Summary
📅 {datetime.now(ET).strftime("%A, %B %d, %Y at %H:%M ET")}

{content}

🔗 Full journal: https://github.com/{os.getenv('GITHUB_REPOSITORY', 'your-username/grok-trading-bot')}/blob/main/memory/journal.md
    """.strip()
    msg = MIMEText(body, "plain")
    msg["Subject"] = f"📈 Daily Trading Recap — {today}"
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_TO
    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, EMAIL_TO, msg.as_string())
        server.quit()
        print("✅ Daily summary email sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", str(e))

def run_routine(routine_type):
    strategy = load_memory("strategy_rules.md")
    journal = load_memory("journal.md")
    positions = load_memory("positions.md") or "No open positions"

    now_et = datetime.now(ET)
    current_et_time = now_et.strftime("%Y-%m-%d %H:%M ET")

    if "eod" in routine_type.lower() or "summary" in routine_type.lower() or "weekly" in routine_type.lower():
        if "weekly" in routine_type.lower():
            instructions_file = "weekly_summary_instructions.md"
            summary_type = "Weekly Summary"
        else:
            instructions_file = "eod_summary_instructions.md"
            summary_type = "EOD Summary"

        instructions = load_memory(instructions_file)
    
    # Trading logic for MNQ
    prompt = f"""You are a professional futures trading bot for MNQ. Current time (ET): {current_et_time}

STRATEGY RULES (never break these):
{strategy}

JOURNAL HISTORY:
{journal}

Positions: {positions}

Your job:
- Analyze current MNQ market using the exact Golden Candle rules
- Decide exact action (buy/sell/hold/flat)
- Output ONLY valid JSON with keys: action, qty, stop_loss_price, take_profit_price, reasoning"""

    # Call Grok (same as Alpaca bot)
    # ... paste your existing call_grok function here ...

    decision = call_grok(prompt, routine_type)

    if decision.get("action") in ["buy", "sell"]:
        token = get_tradovate_token()
        side = "Buy" if decision["action"] == "buy" else "Sell"
        result = place_mnq_order(token, side, decision.get("qty", 1))
        print(f"✅ Placed {side} order for {decision.get('qty', 1)} MNQ | Response: {result}")

    new_entry = f"\n\n### {current_et_time} - {routine_type}\n{decision.get('reasoning', 'No reasoning provided')}"
    save_memory("journal.md", journal + new_entry)
    print("Routine complete. Decision:", decision)

if __name__ == "__main__":
    import sys
    routine = sys.argv[1] if len(sys.argv) > 1 else "unknown"
    run_routine(routine)
