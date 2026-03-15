"""
╔══════════════════════════════════════════════════════════════════════╗
║        TECH NEWS WITH AI — AUTO BLOG SYSTEM (100% FREE)            ║
║        Blog: technewswithai.blogspot.com                            ║
║        AI  : Groq (FREE) — Llama 3.3 70B                           ║
╠══════════════════════════════════════════════════════════════════════╣
║  SETUP (one time only):                                              ║
║   1. pip install groq requests                                       ║
║           google-auth google-auth-oauthlib                          ║
║           google-api-python-client                                   ║
║   2. python auto_blog_free.py                                        ║
║   3. First run: browser opens for Google login → allow it           ║
╚══════════════════════════════════════════════════════════════════════╝
"""

GROQ_API_KEY = "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"
NEWS_API_KEY = "673bca5ceab54fa8bb7ed0344c8f6d13"
BLOG_ID      = "6974086222747114440"

ARTICLES_PER_RUN = 1
POST_AS_DRAFT    = False

NEWS_TOPICS = [
    "iPhone 2026 launch specifications",
    "Samsung Galaxy launch specs review",
    "MacBook launch price specifications",
    "OnePlus Realme Xiaomi launch India 2026",
    "Google Pixel launch specs 2026",
    "Nothing phone launch India 2026",
    "laptop launch specifications 2026",
    "Android phone launch specs 2026",
]

import os, sys, json, time, random, requests, datetime, re

def require(package, install):
    try:
        __import__(package)
    except ImportError:
        print(f"Missing: {package}  Fix: pip install {install}")
        sys.exit(1)

require("groq",                        "groq")
require("google.oauth2.credentials",   "google-auth")
require("google_auth_oauthlib.flow",   "google-auth-oauthlib")
require("googleapiclient.discovery",   "google-api-python-client")

from groq                             import Groq
from google.oauth2.credentials        import Credentials
from google_auth_oauthlib.flow        import InstalledAppFlow
from google.auth.transport.requests   import Request
from googleapiclient.discovery        import build

def fetch_news(query, count=3):
    print(f"  Searching: '{query}'")
    try:
        r = requests.get(
            "https://newsapi.org/v2/everything",
            params={"q": query, "language": "en", "sortBy": "publishedAt",
                    "pageSize": count, "apiKey": NEWS_API_KEY},
            timeout=10,
        )
        data = r.json()
        if data.get("status") != "ok":
            return []
        articles = [
            {"title": a["title"], "description": a.get("description") or "",
             "content": a.get("content") or "", "url": a["url"],
             "source": a["source"]["name"], "published": a["publishedAt"]}
            for a in data.get("articles", [])
            if a.get("title") and a.get("description")
        ]
        print(f"    {len(articles)} articles found")
        return articles
    except Exception as e:
        print(f"    Error: {e}")
        return []

def pick_story():
    topics = NEWS_TOPICS.copy()
    random.shuffle(topics)
    for topic in topics:
        articles = fetch_news(topic)
        if articles:
            s = articles[0]
            print(f"\n  Picked : {s['title']}")
            print(f"  Source : {s['source']}")
            return s
    return None

SYSTEM_PROMPT = """You write for the tech blog "Tech News With AI" (technewswithai.blogspot.com) by Mallikarjun R, Bengaluru, India.

VOICE:
- Passionate and enthusiastic like explaining to a smart friend
- Simple English, not just for experts
- Use phrases: "here is the thing", "let us break this down", "this is where it gets interesting", "think of it this way", "in plain simple terms"
- Address reader directly ("you will love this", "when you hold this phone")

CONTENT RULES:
- Explain WHY each spec matters, never just list numbers
- BAD: "120Hz display"  GOOD: "120Hz means the screen refreshes 120 times every second, making scrolling feel like butter"
- Explain every technical term in plain language when first used
- Always include India price (USD price x 85 = INR estimate)
- Always compare with at least one competitor
- MINIMUM 1500 words

FORMAT RULES:
- NO bullet point lists, always flowing paragraphs only
- NO tables, write comparisons as prose sentences
- Use <h2> for main headings, <h3> for sub headings
- Wrap every paragraph in <p> tags
- Output clean HTML only, no markdown, no code fences

SECTIONS TO ALWAYS WRITE:
1. Introduction - hook and why this device matters
2. Design and Build - materials, dimensions, colors
3. Display Explained - size, resolution, refresh rate in simple terms
4. Camera System - explain each lens individually
5. Processor and Speed - chip name and real world meaning
6. Battery and Charging - capacity and daily usage estimate
7. Software and Features - OS and unique features
8. Price in India - India price and best variant to buy
9. Final Verdict - clear buy or wait or skip recommendation"""

def write_post(story):
    print("\n  Writing with Groq Llama 3.3 70B...")
    client = Groq(api_key=GROQ_API_KEY)
    prompt = f"""Write a complete detailed blog post about this tech news.

HEADLINE  : {story['title']}
SUMMARY   : {story['description']}
EXTRA INFO: {story['content'][:600] if story['content'] else 'Not available'}
SOURCE    : {story['source']}

Rules:
- Minimum 1500 words
- Output valid HTML using h2 h3 p tags only
- First tag must be h2 with a catchy article title
- Do NOT include html head body tags
- Write all 9 sections
- Always mention India pricing

Write the full article now:"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": prompt}
            ],
            max_tokens=4000,
            temperature=0.8,
        )
        raw = response.choices[0].message.content
        raw = re.sub(r"```html\s*", "", raw)
        raw = re.sub(r"```\s*", "", raw)
        raw = raw.strip()

        title = story["title"]
        m = re.search(r"<h2[^>]*>(.*?)</h2>", raw, re.IGNORECASE | re.DOTALL)
        if m:
            title = re.sub(r"<[^>]+>", "", m.group(1)).strip()

        footer = f"""
<hr>
<p><em><strong>Source:</strong> {story['source']} | <strong>Published:</strong> {story['published'][:10]} | <a href="{story['url']}" target="_blank">Read original article</a></em></p>
<p><em>Stay updated at <a href="https://technewswithai.blogspot.com" target="_blank">Tech News With AI</a>. Follow on <a href="https://www.instagram.com/mallikarjunr_8055" target="_blank">Instagram</a> and join our <a href="https://whatsapp.com/channel/0029VazWwdn0wajoizN5PY3Q" target="_blank">WhatsApp channel</a>.</em></p>
"""
        words = len(re.sub(r"<[^>]+>", "", raw).split())
        print(f"    Done - {words} words")
        return title, raw + footer

    except Exception as e:
        print(f"    Groq error: {e}")
        raise

SCOPES           = ["https://www.googleapis.com/auth/blogger"]
CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE       = "token.json"

def blogger_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                print("credentials.json not found! Put it in the same folder.")
                sys.exit(1)
            print("  Opening browser for Google login (one time only)...")
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())
        print("  Google auth saved")
    return build("blogger", "v3", credentials=creds)

def auto_labels(title, html):
    text = (title + " " + html[:300]).lower()
    labels = ["Tech News"]
    MAP = {
        "iphone": ["iPhone","Apple"], "samsung": ["Samsung","Android"],
        "macbook": ["MacBook","Laptop"], "google": ["Google","Android"],
        "oneplus": ["OnePlus","Android"], "realme": ["Realme","Android"],
        "xiaomi": ["Xiaomi","Android"], "nothing": ["Nothing Phone","Android"],
        "pixel": ["Google Pixel","Android"], "laptop": ["Laptop"],
        "android": ["Android"], "apple": ["Apple"], "india": ["Price in India"],
    }
    for kw, tags in MAP.items():
        if kw in text:
            for t in tags:
                if t not in labels:
                    labels.append(t)
    labels.append(str(datetime.datetime.now().year))
    return labels[:10]

def post_article(title, html, labels):
    print(f"\n  Posting to Blogger...")
    print(f"  Title  : {title}")
    service = blogger_service()
    try:
        result = service.posts().insert(
            blogId=BLOG_ID,
            body={"title": title, "content": html, "labels": labels},
            isDraft=POST_AS_DRAFT,
        ).execute()
        url = result.get("url", "")
        print(f"  Published live!")
        print(f"  URL: {url}")
        return url
    except Exception as e:
        print(f"  Blogger error: {e}")
        raise

def save_log(title, url):
    log_file = "posted_articles.json"
    log = []
    if os.path.exists(log_file):
        with open(log_file) as f:
            log = json.load(f)
    log.append({"title": title, "url": url, "posted_at": datetime.datetime.now().isoformat()})
    with open(log_file, "w") as f:
        json.dump(log, f, indent=2)
    print(f"  Log saved (total: {len(log)} posts)")

def main():
    print("""
╔══════════════════════════════════════════════════════╗
║    TECH NEWS WITH AI — AUTO BLOG (100% FREE)        ║
║    technewswithai.blogspot.com                      ║
╚══════════════════════════════════════════════════════╝""")

    success = 0
    for i in range(ARTICLES_PER_RUN):
        try:
            story = pick_story()
            if not story:
                continue
            title, html = write_post(story)
            labels      = auto_labels(title, html)
            url         = post_article(title, html, labels)
            save_log(title, url)
            success += 1
            if i < ARTICLES_PER_RUN - 1:
                time.sleep(20)
        except KeyboardInterrupt:
            print("\nStopped.")
            break
        except Exception as e:
            print(f"\nFailed: {e}")
            continue

    print(f"""
╔══════════════════════════════════════════════════════╗
║  DONE! {success}/{ARTICLES_PER_RUN} article(s) posted!
║  technewswithai.blogspot.com
╚══════════════════════════════════════════════════════╝""")

if __name__ == "__main__":
    main()
