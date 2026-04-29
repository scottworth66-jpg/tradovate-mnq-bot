import os
import json
from datetime import datetime
from zoneinfo import ZoneInfo
import smtplib
from email.mime.text import MIMEText
import requests
import time

# ====================== SECRETS ======================
GROK_API_KEY = os.getenv("GROK_API_KEY")
TRADOVATE_API_KEY = os.getenv("TRADOVATE_API_KEY")
TRADOVATE_USERNAME = os.getenv("TRADOVATE_USERNAME")
TRADOVATE_PASSWORD = os.getenv("TRADOVATE_PASSWORD")
TRADOVATE_APP_ID = os.getenv("TRADOVATE_APP_ID", "grok-mnq-bot")

# Email settings
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")

ET = ZoneInfo("America/New_York")

# ====================== HELPERS (same as before) ======================
def get_tradovate_token():
    url = "https://live.tradovateapi.com/v1/auth/accessToken"
    payload = {"name": TRADOVATE_APP_ID, "apiKey": TRADOVATE_API_KEY, "username": TRADOVATE_USERNAME, "password": TRADOVATE_PASSWORD}
    resp = requests.post(url, json=payload)
    resp.raise_for_status()
    return resp.json()["accessToken"]

def place_mnq_order(token, side, qty=1):
    url = "https://live.tradovateapi.com/v1/order/placeOrder"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"accountSpec": TRADOVATE_USERNAME, "symbol": "MNQ", "side": side.upper(), "orderQty": qty, "orderType": "Market", "timeInForce": "Day"}
    resp = requests.post(url, json=payload, headers=headers)
    return resp.json()

def call_grok(prompt, routine_type):
    url = "https://api.x.ai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROK_API_KEY}", "Content-Type": "application/json"}
    data = {"model": "grok-4.20-reasoning", "messages": [{"role": "user", "content": prompt}], "temperature": 0.3, "response_format": {"type": "json_object"}}
    resp = requests.post(url, json=data, headers=headers)
    if resp.status_code != 200:
        return {"action": "none", "reasoning": f"API error {resp.status_code}"}
    try:
        content = resp.json()["choices"][0]["message"]["content"]
        return json.loads(content)
    except:
        return {"action": "none", "reasoning": "Parse error"}

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
    # (same email function as before - abbreviated for space)
    # ... keep your existing send_daily_email function here exactly as it is ...
    pass  # ← paste your current send_daily_email function here

# ====================== LIVE TRADING LOOP ======================
def run_live():
    print("🚀 MNQ Live Scalping Mode Started - Checking every 30 seconds during RTH")
    while True:
        now = datetime.now(ET)
        if now.weekday() >= 5 or not (9 <= now.hour < 16):  # Only run Mon-Fri 9:00-16:00 ET
            time.sleep(60)
            continue

        # Run the normal strategy check
        run_routine("live")
        time.sleep(30)  # Check every 30 seconds

# ====================== MAIN ======================
def run_routine(routine_type):
    # ... keep all your existing code for EOD, Weekly, Midday, etc. exactly as it is ...
    # (the full code you already have for summaries and normal trading logic)

    # Only the live part is new - the rest stays the same
    if routine_type == "live":
        # The loop is handled in run_live() above
        pass

    # (keep the rest of your existing run_routine code unchanged)

if __name__ == "__main__":
    import sys
    routine = sys.argv[1] if len(sys.argv) > 1 else "unknown"
    
    if routine == "live":
        run_live()
    else:
        run_routine(routine)
