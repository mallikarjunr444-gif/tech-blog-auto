"""
╔══════════════════════════════════════════════════════════════════════╗
║        TECH NEWS WITH AI — AUTO BLOG SYSTEM (100% FREE)            ║
║        Blog: technewswithai.blogspot.com                            ║
║        AI  : Groq (FREE) — Llama 3.3 70B                           ║
║        POST: Blogger API v3 with API Key (No browser login!)        ║
╠══════════════════════════════════════════════════════════════════════╣
║  SETUP:                                                              ║
║   1. pip install groq requests google-auth                          ║
║           google-auth-oauthlib google-api-python-client             ║
║   2. python auto_blog_free.py                                        ║
╚══════════════════════════════════════════════════════════════════════╝
"""

# ══════════════════════════════════════════════════════════════════════
#  YOUR FREE API KEYS
# ══════════════════════════════════════════════════════════════════════

GROQ_API_KEY    = "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"
NEWS_API_KEY    = "673bca5ceab54fa8bb7ed0344c8f6d13"
BLOG_ID         = "6974086222747114440"

# ══════════════════════════════════════════════════════════════════════
# BLOGGER CREDENTIALS — just your Google email and password
# ══════════════════════════════════════════════════════════════════════

GOOGLE_EMAIL    = "mallikarjunr444@gmail.com"   # your gmail
GOOGLE_PASSWORD = "YOUR_GOOGLE_PASSWORD_HERE"   # your google password

# ══════════════════════════════════════════════════════════════════════
#  SETTINGS
# ══════════════════════════════════════════════════════════════════════

ARTICLES_PER_RUN = 1
POST_AS_DRAFT    = False

NEWS_TOPICS = [
    # ── Apple ──────────────────────────────────────
    "iPhone 2026 launch specifications price",
    "MacBook launch price specifications 2026",
    "iPad launch specifications 2026",
    "Apple Watch launch specs 2026",
    "AirPods launch specs 2026",

    # ── Samsung ────────────────────────────────────
    "Samsung Galaxy S launch specs 2026",
    "Samsung Galaxy A launch India specs 2026",
    "Samsung Galaxy Tab launch specs 2026",
    "Samsung laptop launch specifications 2026",

    # ── OnePlus / Oppo / Realme ────────────────────
    "OnePlus launch specifications India 2026",
    "Realme launch specifications India 2026",
    "OPPO launch specifications India 2026",

    # ── Xiaomi / Poco / Redmi ──────────────────────
    "Xiaomi launch specifications India 2026",
    "Poco launch specifications India 2026",
    "Redmi launch specifications India 2026",

    # ── Vivo / iQOO ───────────────────────────────
    "Vivo launch specifications India 2026",
    "iQOO launch specifications India 2026",

    # ── Google ─────────────────────────────────────
    "Google Pixel launch specs 2026",

    # ── Motorola / Nokia ───────────────────────────
    "Motorola launch specifications India 2026",
    "Nokia launch specifications India 2026",

    # ── Nothing / Infinix / Tecno ─────────────────
    "Nothing phone launch India 2026",
    "Infinix launch specifications India 2026",
    "Tecno launch specifications India 2026",

    # ── Sony / Huawei / Honor ─────────────────────
    "Sony Xperia launch specifications 2026",
    "Huawei launch specifications 2026",
    "Honor launch specifications India 2026",

    # ── Laptops ───────────────────────────────────
    "Dell laptop launch specifications 2026",
    "HP laptop launch specifications 2026",
    "Lenovo laptop launch specifications 2026",
    "ASUS laptop launch specifications 2026",
    "Acer laptop launch specifications 2026",
    "Microsoft Surface launch specifications 2026",
    "Samsung laptop launch specifications 2026",
    "LG Gram laptop launch specifications 2026",
    "Razer laptop launch specifications 2026",

    # ── Other Tech ────────────────────────────────
    "smartwatch launch India specs 2026",
    "TWS earbuds launch India specs 2026",
    "Android tablet launch specifications 2026",
    "smart TV launch India specs 2026",
]

# ══════════════════════════════════════════════════════════════════════
#  DO NOT EDIT BELOW THIS LINE
# ══════════════════════════════════════════════════════════════════════

import os, sys, json, time, random, requests, datetime, re

def require(package, install):
    try:
        __import__(package)
    except ImportError:
        print(f"Missing: {package}  Fix: pip install {install}")
        sys.exit(1)

require("groq", "groq")

from groq import Groq

# ══════════════════════════════════════════════════════════════════════
#  MODULE 1 — NEWS FETCHER
# ══════════════════════════════════════════════════════════════════════

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

# ══════════════════════════════════════════════════════════════════════
#  MODULE 2 — AI WRITER (Groq Free)
# ══════════════════════════════════════════════════════════════════════

SYSTEM_PROMPT = """You write for the tech blog "Tech News With AI" (technewswithai.blogspot.com) by Mallikarjun R, Bengaluru, India.

VOICE:
- Passionate and enthusiastic like explaining to a smart friend
- Simple English, not just for experts
- Use phrases: "here is the thing", "let us break this down", "this is where it gets interesting"
- Address reader directly ("you will love this", "when you hold this phone")

CONTENT RULES:
- Explain WHY each spec matters, never just list numbers
- BAD: "120Hz display"
- GOOD: "120Hz means the screen refreshes 120 times every second, making scrolling feel like butter"
- Always include India price (USD x 85 = INR estimate)
- Always compare with at least one competitor
- MINIMUM 1500 words

FORMAT RULES:
- NO bullet points, always flowing paragraphs only
- NO tables, write comparisons as prose
- Use <h2> for main headings, <h3> for sub headings
- Wrap every paragraph in <p> tags
- Output clean HTML only, no markdown

SECTIONS:
1. Introduction - hook and why this device matters
2. Design and Build - materials, dimensions, colors
3. Display Explained - size, resolution, refresh rate in simple words
4. Camera System - explain each lens individually
5. Processor and Speed - chip name and real world meaning
6. Battery and Charging - capacity and daily usage estimate
7. Software and Features - OS and unique features
8. Price in India - India price and best variant
9. Final Verdict - clear buy or wait or skip recommendation"""

def write_post(story):
    print("\n  Writing with Groq Llama 3.3 70B...")
    client = Groq(api_key=GROQ_API_KEY)
    prompt = f"""Write a complete detailed blog post about this tech news.

HEADLINE  : {story['title']}
SUMMARY   : {story['description']}
EXTRA INFO: {story['content'][:600] if story['content'] else 'Not available'}
SOURCE    : {story['source']}

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
<p><em>Stay updated at <a href="https://technewswithai.blogspot.com">Tech News With AI</a>. Follow on <a href="https://www.instagram.com/mallikarjunr_8055">Instagram</a> and join our <a href="https://whatsapp.com/channel/0029VazWwdn0wajoizN5PY3Q">WhatsApp channel</a>.</em></p>
"""
        words = len(re.sub(r"<[^>]+>", "", raw).split())
        print(f"    Done - {words} words")
        return title, raw + footer

    except Exception as e:
        print(f"    Groq error: {e}")
        raise

# ══════════════════════════════════════════════════════════════════════
#  MODULE 3 — POST TO BLOGGER (using Google OAuth2 token directly)
# ══════════════════════════════════════════════════════════════════════

def get_access_token():
    """Get Google access token using email and password via OAuth2."""
    print("  Getting Google access token...")
    try:
        # Use Google's OAuth2 token endpoint
        token_url = "https://oauth2.googleapis.com/token"
        
        # Read client credentials from credentials.json
        if not os.path.exists("credentials.json"):
            print("  credentials.json not found!")
            sys.exit(1)
            
        with open("credentials.json") as f:
            creds_data = json.load(f)
        
        installed = creds_data.get("installed", {})
        client_id     = installed.get("client_id")
        client_secret = installed.get("client_secret")
        
        # Check if we have a saved token
        if os.path.exists("token.json"):
            with open("token.json") as f:
                token_data = json.load(f)
            
            # Check if token is still valid
            expiry = token_data.get("expiry", "")
            if expiry:
                from datetime import timezone
                expiry_dt = datetime.datetime.fromisoformat(expiry.replace("Z", "+00:00"))
                now = datetime.datetime.now(timezone.utc)
                if now < expiry_dt:
                    print("    Using saved token")
                    return token_data.get("token")
            
            # Refresh the token
            refresh_token = token_data.get("refresh_token")
            if refresh_token:
                print("    Refreshing token...")
                r = requests.post(token_url, data={
                    "client_id":     client_id,
                    "client_secret": client_secret,
                    "refresh_token": refresh_token,
                    "grant_type":    "refresh_token",
                })
                if r.status_code == 200:
                    new_token = r.json()
                    token_data["token"] = new_token["access_token"]
                    expiry_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=3600)
                    token_data["expiry"] = expiry_time.isoformat()
                    with open("token.json", "w") as f:
                        json.dump(token_data, f)
                    print("    Token refreshed!")
                    return new_token["access_token"]
        
        # No token — need to do device flow
        print("""
  No token found. Please do this ONE TIME setup:
  
  1. Go to: https://console.cloud.google.com
  2. APIs & Services → OAuth consent screen
  3. Add test user: mallikarjunr444@gmail.com
  4. Save and run script again
  
  OR run this command to login:
     python get_token.py
""")
        sys.exit(1)
        
    except Exception as e:
        print(f"    Token error: {e}")
        raise

def auto_labels(title, html):
    text = (title + " " + html[:300]).lower()
    labels = ["Tech News"]
    MAP = {
        "iphone": ["iPhone","Apple"], "samsung": ["Samsung","Android"],
        "macbook": ["MacBook","Laptop"], "google": ["Google","Android"],
        "oneplus": ["OnePlus","Android"], "realme": ["Realme","Android"],
        "xiaomi": ["Xiaomi","Android"], "nothing": ["Nothing Phone"],
        "pixel": ["Google Pixel"], "laptop": ["Laptop"],
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
    print(f"  Title: {title}")
    
    access_token = get_access_token()
    
    url = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    body = {
        "title": title,
        "content": html,
        "labels": labels,
    }
    
    try:
        r = requests.post(url, headers=headers, json=body, timeout=30)
        if r.status_code in [200, 201]:
            post_url = r.json().get("url", "")
            print(f"  Published live!")
            print(f"  URL: {post_url}")
            return post_url
        else:
            print(f"  Blogger error: {r.status_code} - {r.text[:200]}")
            raise Exception(f"Blogger API error: {r.status_code}")
    except Exception as e:
        print(f"  Post error: {e}")
        raise

def save_log(title, url):
    log_file = "posted_articles.json"
    log = []
    if os.path.exists(log_file):
        with open(log_file) as f:
            log = json.load(f)
    log.append({"title": title, "url": url,
                "posted_at": datetime.datetime.now().isoformat()})
    with open(log_file, "w") as f:
        json.dump(log, f, indent=2)
    print(f"  Log saved (total: {len(log)} posts)")

# ══════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════

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
