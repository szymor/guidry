#!/usr/bin/env python3
import csv
import sys
from pathlib import Path
from html import escape

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 700px; margin: 2em auto; padding: 0 1em; background: #f7f7f8; color: #1c1e21; }}
  h1 {{ font-size: 1.3em; margin-bottom: 1.5em; }}
  .tweet {{ background: #fff; border: 1px solid #e1e8ed; border-radius: 12px; padding: 1em; margin-bottom: 1em; }}
  .tweet-meta {{ font-size: 0.85em; color: #657786; margin-bottom: 0.3em; }}
  .tweet-meta a {{ color: inherit; text-decoration: none; }}
  .tweet-meta a:hover {{ text-decoration: underline; }}
  .tweet-text {{ font-size: 1em; line-height: 1.5; margin-bottom: 0.6em; white-space: pre-wrap; word-wrap: break-word; }}
  .tweet-text a {{ color: #1b95e0; text-decoration: none; }}
  .tweet-text a:hover {{ text-decoration: underline; }}
  .tweet-type {{ display: inline-block; font-size: 0.75em; background: #e8f5fd; color: #1b95e0; border-radius: 4px; padding: 0.1em 0.5em; }}
  .tweet-stats {{ display: flex; gap: 1em; font-size: 0.8em; color: #657786; margin-top: 0.5em; }}
  .tweet-stats span {{ white-space: nowrap; }}
  .tweet-hashtags {{ margin-top: 0.4em; font-size: 0.85em; }}
  .tweet-hashtags a {{ color: #1b95e0; text-decoration: none; }}
  .tweet-media {{ margin-top: 0.6em; }}
  .tweet-media img {{ max-width: 100%; border-radius: 8px; }}
  .meta-count {{ font-size: 0.85em; color: #657786; margin-bottom: 1em; }}
</style>
</head>
<body>
<h1>{title}</h1>
<p class="meta-count">{count} tweets</p>
{tweets}
</body>
</html>"""

TWEET_TEMPLATE = """<div class="tweet">
  <div class="tweet-meta">
    <a href="https://x.com/i/web/status/{tweet_id}">{created_at}</a>
    &middot; {type_badge}
    &middot; {client}
  </div>
  <div class="tweet-text">{text}</div>
  {hashtags_html}
  {media_html}
  <div class="tweet-stats">
    <span>&#x2661; {favorites}</span>
    <span>&#x21A9; {retweets}</span>
    <span>&#x1F4AC; {replies}</span>
    <span>&#x1F441; {views}</span>
    <span>&#x1F516; {bookmarks}</span>
  </div>
</div>"""


def fmt_count(n):
    if n == "" or n is None:
        return "0"
    try:
        return f"{int(n):,}"
    except (ValueError, TypeError):
        return str(n)


def make_type_badge(tweet_type):
    labels = {"Tweet": "Tweet", "Reply": "Reply", "Retweet": "Retweet"}
    return f'<span class="tweet-type">{labels.get(tweet_type, tweet_type)}</span>'


def make_hashtags(hashtags_str):
    if not hashtags_str:
        return ""
    tags = [h.strip() for h in hashtags_str.split(",") if h.strip()]
    if not tags:
        return ""
    links = " ".join(
        f'<a href="https://x.com/hashtag/{t[1:] if t.startswith("#") else t}">{escape(t)}</a>'
        for t in tags
    )
    return f'<div class="tweet-hashtags">{links}</div>'


def make_media(media_type, media_urls_str):
    if not media_type or not media_urls_str:
        return ""
    urls = [u.strip() for u in media_urls_str.split(",") if u.strip()]
    if not urls:
        return ""
    imgs = "".join(f'<img src="{escape(url)}" alt="" loading="lazy">' for url in urls)
    return f'<div class="tweet-media">{imgs}</div>'


def make_text(text):
    return escape(text)


def process_csv(csv_path):
    output_path = csv_path.with_suffix(".html")
    tweets_html = []
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if all(v is None or v == "" for v in row.values()):
                continue
            tweet_id = row.get("tweet_id", "").strip("'\" ")
            text = make_text(row.get("text", ""))
            tweet_type = row.get("type", "")
            created_at = row.get("created_at", "")
            client = row.get("client", "")
            favorites = fmt_count(row.get("favorite_count"))
            retweets = fmt_count(row.get("retweet_count"))
            replies = fmt_count(row.get("reply_count"))
            views = fmt_count(row.get("view_count"))
            bookmarks = fmt_count(row.get("bookmark_count"))
            hashtags = row.get("hashtags", "")
            media_type = row.get("media_type", "")
            media_urls = row.get("media_urls", "")

            tweets_html.append(
                TWEET_TEMPLATE.format(
                    tweet_id=tweet_id,
                    created_at=escape(created_at),
                    type_badge=make_type_badge(tweet_type),
                    client=client if client else "",
                    text=text,
                    hashtags_html=make_hashtags(hashtags),
                    media_html=make_media(media_type, media_urls),
                    favorites=favorites,
                    retweets=retweets,
                    replies=replies,
                    views=views,
                    bookmarks=bookmarks,
                )
            )

    title = escape(csv_path.stem.replace("_", " ").replace(".csv", ""))
    html = TEMPLATE.format(
        title=title,
        count=fmt_count(len(tweets_html)),
        tweets="\n".join(tweets_html),
    )
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    return output_path


def main():
    tweets_dir = Path(__file__).parent
    csv_files = sorted(tweets_dir.glob("*.csv"))
    if not csv_files:
        print("No CSV files found in", tweets_dir)
        sys.exit(1)
    for csv_file in csv_files:
        out = process_csv(csv_file)
        print(f"Generated {out}")


if __name__ == "__main__":
    main()
