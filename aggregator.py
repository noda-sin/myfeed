import feedparser, pytz
from datetime import datetime, timedelta
from dateutil import parser as dt
import requests
from readability import Document

def fetch_article_text(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        doc = Document(response.text)
        content_html = doc.summary()
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(content_html, 'html.parser')
        return soup.get_text(separator="\n", strip=True)
    except Exception as e:
        print(f"[warn] Failed to fetch article: {url} ({e})")
        return ""

def fetch_new_items(feed_cfg: dict, tz) -> list[dict]:
    fp = feedparser.parse(feed_cfg["url"])
    cutoff = datetime.now(tz) - timedelta(hours=24)
    items = []
    for entry in fp.entries[:feed_cfg.get("max_items_per_feed", 20)]:
        if "published" not in entry:
            continue
        try:
            pub = dt.parse(entry.published)
        except (ValueError, TypeError):
            continue
        if not pub.tzinfo:
            pub = pub.replace(tzinfo=pytz.UTC)
        pub = pub.astimezone(tz)
        if pub >= cutoff:
            article_text = fetch_article_text(entry.link) or entry.get("summary", "")
            items.append({
                "title": entry.title,
                "link": entry.link,
                "published": pub.isoformat(),
                "summary": article_text
            })
    return items
