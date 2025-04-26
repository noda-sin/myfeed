import yaml, pytz, logging
from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv
import os

from aggregator import fetch_new_items
from summarizer import summarize
from notifier import post_to_slack

load_dotenv()

logging.basicConfig(level=logging.INFO)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def load_cfg():
    with open("config.yaml") as f:
        return yaml.safe_load(f)

def main():
    cfg = load_cfg()
    tz = pytz.timezone(cfg["timezone"])
    all_items = []
    for f in cfg["feeds"]:
        all_items.extend(fetch_new_items(f, tz))
    if cfg.get("keywords"):
        kw = tuple(cfg["keywords"])
        all_items = [
            i for i in all_items
            if any(k.lower() in i["title"].lower() for k in kw)
        ]
    summary = summarize(OPENAI_API_KEY, all_items, cfg)
    post_to_slack(SLACK_WEBHOOK_URL, summary)
    logging.info("Posted %d items", len(all_items))

if __name__ == "__main__":
    main()
