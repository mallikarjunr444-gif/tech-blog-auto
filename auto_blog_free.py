"""
TECH NEWS WITH AI - AUTO BLOG SYSTEM
Blog: technewsai.me
AI  : Groq Llama 3.3 70B (FREE) + Grok fallback
POST: Blogger via Email
"""

import os
import sys
import json
import time
import random
import requests
import datetime
import re
import smtplib
import xml.etree.ElementTree as ET
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ══════════════════════════════════════════════════════
#  API KEYS AND SETTINGS
# ══════════════════════════════════════════════════════

GROQ_API_KEY       = os.environ.get("GROQ_API_KEY", "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")
NEWS_API_KEY       = os.environ.get("NEWS_API_KEY", "673bca5ceab54fa8bb7ed0344c8f6d13")
XAI_API_KEY        = os.environ.get("XAI_API_KEY", "")
BLOG_ID            = "6974086222747114440"
BLOGGER_POST_EMAIL = "mallikarjunr444.technewswithai6361@blogger.com"
GMAIL_ADDRESS      = "mallikarjunr444@gmail.com"
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "oeirtosmlhuwntka")
ARTICLES_PER_RUN   = 3

# ══════════════════════════════════════════════════════
#  NEWS TOPICS WITH SEO KEYWORDS
# ══════════════════════════════════════════════════════

NEWS_TOPICS = [
    "iPhone 2026 launch specifications price India",
    "MacBook launch price specifications 2026",
    "iPad launch specifications 2026",
    "Samsung Galaxy S launch specs India 2026",
    "Samsung Galaxy A launch India specs 2026",
    "OnePlus launch specifications India 2026",
    "Realme launch specifications India 2026",
    "OPPO launch specifications India 2026",
    "Xiaomi launch specifications India 2026",
    "Poco launch specifications India 2026",
    "Redmi launch specifications India 2026",
    "Vivo launch specifications India 2026",
    "iQOO launch specifications India 2026",
    "Google Pixel launch specs India 2026",
    "Motorola launch specifications India 2026",
    "Nokia launch specifications India 2026",
    "Nothing phone launch India 2026",
    "Infinix launch specifications India 2026",
    "Tecno launch specifications India 2026",
    "Honor launch specifications India 2026",
    "Dell laptop launch specifications 2026",
    "HP laptop launch specifications 2026",
    "Lenovo laptop launch specifications 2026",
    "ASUS laptop launch specifications 2026",
    "Acer laptop launch specifications 2026",
    "Microsoft Surface launch specifications 2026",
    "smartwatch launch India specs 2026",
    "TWS earbuds launch India specs 2026",
    "Android tablet launch specifications 2026",
    "smart TV launch India specs 2026",
    "best phone under 20000 India 2026",
    "best phone under 30000 India 2026",
    "best laptop under 50000 India 2026",
    "AI smartphone features India 2026",
]

# ══════════════════════════════════════════════════════
#  RSS FEEDS
# ══════════════════════════════════════════════════════

RSS_FEEDS = [
    ("The Verge",        "https://www.theverge.com/rss/index.xml"),
    ("TechCrunch",       "https://techcrunch.com/feed/"),
    ("Engadget",         "https://www.engadget.com/rss.xml"),
    ("CNET",             "https://www.cnet.com/rss/news/"),
    ("GSMArena",         "https://www.gsmarena.com/rss-news-articles.php3"),
    ("AndroidAuthority", "https://www.androidauthority.com/feed/"),
    ("9to5Google",       "https://9to5google.com/feed/"),
    ("XDA Developers",   "https://www.xda-developers.com/feed/"),
    ("NotebookCheck",    "https://www.notebookcheck.net/News.rss"),
    ("91Mobiles",        "https://www.91mobiles.com/hub/feed/"),
    ("MySmartPrice",     "https://www.mysmartprice.com/feed/"),
    ("GizmoChina",       "https://www.gizmochina.com/feed/"),
    ("GadgetsNow",       "https://www.gadgetsnow.com/rssfeedstopstories.cms"),
]

# ══════════════════════════════════════════════════════
#  NEWS FETCHER
# ══════════════════════════════════════════════════════

def fetch_from_rss(feed_name, feed_url, keyword):
    try:
        r = requests.get(feed_url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        if r.status_code != 200:
            return []
        root = ET.fromstring(r.content)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        items = root.findall(".//item") or root.findall(".//atom:entry", ns)
        articles = []
        for item in items[:10]:
            title_el = item.find("title")
            title = title_el.text if title_el is not None else ""
            if not title:
                continue
            if keyword.lower().split()[0] not in title.lower():
                continue
            desc_el = item.find("description") or item.find("summary")
            description = desc_el.text if desc_el is not None else ""
            if description:
                description = re.sub(r"<[^>]+>", "", description)[:400]
            link_el = item.find("link")
            link = link_el.text if link_el is not None else feed_url
            date_el = item.find("pubDate") or item.find("published")
            published = date_el.text if date_el is not None else ""
            if title and description:
                articles.append({
                    "title":       title.strip(),
                    "description": description.strip(),
                    "content":     description.strip(),
                    "url":         link.strip() if link else feed_url,
                    "source":      feed_name,
                    "published":   published or "2026-03-19T00:00:00Z",
                })
        return articles[:3]
    except Exception:
        return []


def fetch_from_newsapi(query, count=3):
    try:
        r = requests.get(
            "https://newsapi.org/v2/everything",
            params={
                "q":        query,
                "language": "en",
                "sortBy":   "publishedAt",
                "pageSize": count,
                "apiKey":   NEWS_API_KEY,
            },
            timeout=10,
        )
        data = r.json()
        if data.get("status") != "ok":
            return []
        return [
            {
                "title":       a["title"],
                "description": a.get("description") or "",
                "content":     a.get("content") or "",
                "url":         a["url"],
                "source":      a["source"]["name"],
                "published":   a["publishedAt"],
            }
            for a in data.get("articles", [])
            if a.get("title") and a.get("description")
        ]
    except Exception:
        return []


def fetch_news(query, count=3):
    print("  Searching: " + query)
    all_articles = []
    keyword = query.split()[0]
    feeds = RSS_FEEDS[:]
    random.shuffle(feeds)
    for feed_name, feed_url in feeds[:8]:
        articles = fetch_from_rss(feed_name, feed_url, keyword)
        all_articles.extend(articles)
        if len(all_articles) >= 3:
            break
    if len(all_articles) < 2:
        all_articles.extend(fetch_from_newsapi(query, count))
    seen = set()
    unique = []
    for a in all_articles:
        if a["title"] not in seen:
            seen.add(a["title"])
            unique.append(a)
    print("    " + str(len(unique)) + " articles found")
    return unique[:count]


def pick_story():
    topics = NEWS_TOPICS[:]
    random.shuffle(topics)
    for topic in topics:
        articles = fetch_news(topic)
        if articles:
            s = articles[0]
            print("  Picked : " + s["title"])
            print("  Source : " + s["source"])
            return s
    return None

# ══════════════════════════════════════════════════════
#  AI WRITER — AdSense-Friendly Human Content
# ══════════════════════════════════════════════════════

SYSTEM_PROMPT = (
    "You are a passionate Indian tech journalist writing for Tech News With AI "
    "(technewsai.me), a blog by Mallikarjun R from Bengaluru, India. "
    "You are a real person who loves technology. You share genuine opinions, "
    "frustrations, and excitement. You are NOT an AI robot. You are a "
    "tech-enthusiast friend explaining things to another friend over chai.\n\n"
    "WRITING RULES:\n"
    "Start with a personal hook. Share real opinions: Honestly I think, "
    "In my experience, What surprised me was. "
    "Include genuine criticisms - no device is perfect. "
    "Use conversational transitions: Now here is the interesting part, "
    "Here is where it gets tricky. "
    "Add India-specific context: Mumbai, Delhi, Bengaluru usage scenarios. "
    "Reference real Indian situations: hot summers, long commutes, college budgets. "
    "NEVER use: In conclusion, It is worth noting, Furthermore, Moreover. "
    "Include at least 3 personal opinions per article.\n\n"
    "SEO RULES:\n"
    "Use target keywords naturally in headings and first paragraphs. "
    "Explain WHY each spec matters in real-world India terms. "
    "Always include India price in INR (USD times 85), mention EMI on Flipkart and Amazon India. "
    "Compare with 2 or 3 competitors Indian buyers actually consider. "
    "Mention which variant to buy in India. "
    "Include use cases: college student, office professional, content creator, gamer. "
    "Minimum 3000 words. Every paragraph must add new value.\n\n"
    "FORMAT:\n"
    "NO bullet points - flowing paragraphs only. "
    "NO tables - write comparisons in prose. "
    "Use h2 for main headings, h3 for sub-sections. "
    "Wrap every paragraph in p tags. "
    "Bold important specs using strong tags. "
    "Clean HTML only, no markdown.\n\n"
    "SECTIONS:\n"
    "1. Opening Hook - personal angle on why this matters in India right now\n"
    "2. Design and First Impressions - build quality, colors in India\n"
    "3. Display Deep Dive - panel type, refresh rate explained simply\n"
    "4. Camera Analysis - each lens with Indian photography scenarios\n"
    "5. Performance and Gaming - chipset explained in layman terms\n"
    "6. Battery Life Reality - realistic India usage from morning to night\n"
    "7. Software Experience - OS, bloatware, update promise\n"
    "8. India Price and Value - exact INR pricing, EMI, competitors\n"
    "9. Who Should Buy and Who Should Not - specific Indian profiles\n"
    "10. Final Honest Verdict - genuine recommendation with clear reasoning\n"
    "11. FAQ - 5 questions real Indian buyers ask before purchasing"
)


def build_prompt(story):
    lines = [
        "Write a detailed human genuinely helpful blog post for Indian tech readers.",
        "",
        "NEWS HEADLINE : " + story["title"],
        "NEWS SUMMARY  : " + story["description"],
        "EXTRA DETAILS : " + (story["content"][:600] if story["content"] else "Not available"),
        "SOURCE        : " + story["source"],
        "",
        "REQUIREMENTS:",
        "Write minimum 3000 words.",
        "Sound like a real Indian tech journalist not an AI.",
        "Start with a personal engaging hook sentence.",
        "Include at least 3 genuine personal opinions.",
        "Mention India prices in INR at USD times 85.",
        "Reference Flipkart and Amazon India.",
        "Compare with 2 real competitors Indian buyers consider.",
        "Include realistic India usage scenarios.",
        "Output clean HTML using h2 h3 p strong tags only.",
        "First element must be h2 with a catchy unique SEO-optimized title.",
        "Do NOT include html head body tags.",
        "Cover all 10 sections plus FAQ.",
        "",
        "Write the complete article now starting with the h2 title:",
    ]
    return "\n".join(lines)


def build_footer(story):
    src = story["source"]
    pub = story["published"][:10]
    url = story["url"]
    parts = [
        "<hr>",
        "<p><em><strong>Source:</strong> " + src +
        " | <strong>Published:</strong> " + pub +
        ' | <a href="' + url + '" target="_blank">Read original article</a></em></p>',
        '<p><em>Stay updated at <a href="https://technewsai.me">Tech News With AI</a>. '
        'Follow on <a href="https://www.instagram.com/mallikarjunr_8055">Instagram</a> '
        'and join our <a href="https://whatsapp.com/channel/0029VazWwdn0wajoizN5PY3Q">'
        "WhatsApp channel</a>.</em></p>",
    ]
    return "\n".join(parts)


def parse_response(raw, story):
    raw = re.sub(r"```html\s*", "", raw)
    raw = re.sub(r"```\s*", "", raw)
    raw = raw.strip()
    title = story["title"]
    m = re.search(r"<h2[^>]*>(.*?)</h2>", raw, re.IGNORECASE | re.DOTALL)
    if m:
        title = re.sub(r"<[^>]+>", "", m.group(1)).strip()
    words = len(re.sub(r"<[^>]+>", "", raw).split())
    print("    Done - " + str(words) + " words")
    return title, raw + "\n" + build_footer(story)


def write_post(story):
    prompt = build_prompt(story)

    if XAI_API_KEY:
        try:
            print("  Writing with Grok (xAI)...")
            from openai import OpenAI as OpenAIClient
            grok = OpenAIClient(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")
            resp = grok.chat.completions.create(
                model="grok-3",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user",   "content": prompt},
                ],
                max_tokens=4000,
                temperature=0.8,
            )
            return parse_response(resp.choices[0].message.content, story)
        except Exception as e:
            print("    Grok error: " + str(e) + " - falling back to Groq...")

    print("  Writing with Groq Llama 3.3 70B...")
    from groq import Groq
    client = Groq(api_key=GROQ_API_KEY)
    resp = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": prompt},
        ],
        max_tokens=4000,
        temperature=0.8,
    )
    return parse_response(resp.choices[0].message.content, story)

# ══════════════════════════════════════════════════════
#  BLOGGER POSTER
# ══════════════════════════════════════════════════════

def auto_labels(title, html):
    text = (title + " " + html[:300]).lower()
    labels = ["Tech News"]
    label_map = {
        "iphone":   ["iPhone", "Apple"],
        "macbook":  ["MacBook", "Laptop"],
        "ipad":     ["iPad", "Apple"],
        "samsung":  ["Samsung", "Android"],
        "oneplus":  ["OnePlus", "Android"],
        "realme":   ["Realme", "Android"],
        "xiaomi":   ["Xiaomi", "Android"],
        "poco":     ["Poco", "Android"],
        "redmi":    ["Redmi", "Android"],
        "vivo":     ["Vivo", "Android"],
        "iqoo":     ["iQOO", "Android"],
        "google":   ["Google", "Android"],
        "pixel":    ["Google Pixel"],
        "motorola": ["Motorola", "Android"],
        "nokia":    ["Nokia"],
        "nothing":  ["Nothing Phone"],
        "infinix":  ["Infinix"],
        "laptop":   ["Laptop"],
        "android":  ["Android"],
        "apple":    ["Apple"],
        "india":    ["Price in India"],
        "ai":       ["Artificial Intelligence"],
    }
    for kw, tags in label_map.items():
        if kw in text:
            for t in tags:
                if t not in labels:
                    labels.append(t)
    labels.append(str(datetime.datetime.now().year))
    return labels[:10]


def post_via_email(title, html, labels):
    print("  Sending to Blogger via email...")
    gmail_password = os.environ.get("GMAIL_APP_PASSWORD", GMAIL_APP_PASSWORD)
    msg = MIMEMultipart("alternative")
    msg["Subject"] = title
    msg["From"]    = GMAIL_ADDRESS
    msg["To"]      = BLOGGER_POST_EMAIL
    msg.attach(MIMEText(html, "html"))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_ADDRESS, gmail_password)
        server.sendmail(GMAIL_ADDRESS, BLOGGER_POST_EMAIL, msg.as_string())
    print("  Posted successfully!")
    print("  https://technewsai.me")
    return "https://technewsai.me"


def post_article(title, html, labels):
    print("  Posting: " + title[:60] + "...")
    return post_via_email(title, html, labels)


def save_log(title, url):
    log_file = "posted_articles.json"
    log = []
    if os.path.exists(log_file):
        with open(log_file) as f:
            log = json.load(f)
    log.append({
        "title":     title,
        "url":       url,
        "posted_at": datetime.datetime.now().isoformat(),
    })
    with open(log_file, "w") as f:
        json.dump(log, f, indent=2)
    print("  Log saved (total: " + str(len(log)) + " posts)")

# ══════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════

def main():
    print("=" * 55)
    print("  TECH NEWS WITH AI - AUTO BLOG")
    print("  technewsai.me")
    print("=" * 55)
    success = 0
    for i in range(ARTICLES_PER_RUN):
        try:
            story = pick_story()
            if not story:
                print("No story found, skipping...")
                continue
            title, html = write_post(story)
            labels = auto_labels(title, html)
            url = post_article(title, html, labels)
            save_log(title, url)
            success += 1
            if i < ARTICLES_PER_RUN - 1:
                time.sleep(20)
        except KeyboardInterrupt:
            print("Stopped.")
            break
        except Exception as e:
            print("Failed: " + str(e))
            continue
    print("=" * 55)
    print("  DONE! " + str(success) + "/" + str(ARTICLES_PER_RUN) + " articles posted!")
    print("  technewsai.me")
    print("=" * 55)


if __name__ == "__main__":
    main()
