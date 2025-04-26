import requests
from datetime import datetime

def post_to_slack(webhook: str, text: str):
    payload = {
        "text": f":newspaper: *{datetime.now().strftime('%Y-%m-%d')} DB News*\n{text}"
    }
    r = requests.post(webhook, json=payload, timeout=10)
    r.raise_for_status()
