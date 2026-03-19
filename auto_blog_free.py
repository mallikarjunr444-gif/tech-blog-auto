"""
╔══════════════════════════════════════════════════════════════════════╗
║        TECH NEWS WITH AI — AUTO BLOG SYSTEM (100% FREE)            ║
║        Blog: technewsai.me                                          ║
║        AI  : Groq (FREE) — Llama 3.3 70B + Grok fallback           ║
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

import os

GROQ_API_KEY    = os.environ.get("GROQ_API_KEY", "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")
NEWS_API_KEY    = os.environ.get("NEWS_API_KEY", "673bca5ceab54fa8bb7ed0344c8f6d13")
XAI_API_KEY     = os.environ.get("XAI_API_KEY", "")   # Get free key at console.x.ai
BLOG_ID         = "6974086222747114440"

# ══════════════════════════════════════════════════════════════════════
# BLOGGER CREDENTIALS — just your Google email and password
# ══════════════════════════════════════════════════════════════════════

GOOGLE_EMAIL    = "mallikarjunr444@gmail.com"   # your gmail
GOOGLE_PASSWORD = "YOUR_GOOGLE_PASSWORD_HERE"   # your google password

# ══════════════════════════════════════════════════════════════════════
#  SETTINGS
# ══════════════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════════════
#  BLOGGER EMAIL POSTING — No token needed!
# ══════════════════════════════════════════════════════════════════════
BLOGGER_POST_EMAIL = "mallikarjunr444.technewswithai6361@blogger.com"
GMAIL_ADDRESS      = "mallikarjunr444@gmail.com"
GMAIL_APP_PASSWORD = "oeirtosmlhuwntka"  # Get from Google Account settings

ARTICLES_PER_RUN = 3
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
#  MODULE 1 — NEWS FETCHER (Multiple Sources)
# ══════════════════════════════════════════════════════════════════════

# FREE RSS FEEDS — Top Tech News Channels
RSS_FEEDS = [
    # ── Global Tech News ──────────────────────────────
    ("The Verge",          "https://www.theverge.com/rss/index.xml"),
    ("TechCrunch",         "https://techcrunch.com/feed/"),
    ("Engadget",           "https://www.engadget.com/rss.xml"),
    ("Wired",              "https://www.wired.com/feed/rss"),
    ("CNET",               "https://www.cnet.com/rss/news/"),
    ("GSMArena",           "https://www.gsmarena.com/rss-news-articles.php3"),
    ("AndroidAuthority",   "https://www.androidauthority.com/feed/"),
    ("9to5Mac",            "https://9to5mac.com/feed/"),
    ("9to5Google",         "https://9to5google.com/feed/"),
    ("MacRumors",          "https://feeds.macrumors.com/MacRumors-All"),
    ("PhoneArena",         "https://www.phonearena.com/phones/articles/rss"),
    ("XDA Developers",     "https://www.xda-developers.com/feed/"),
    ("NotebookCheck",      "https://www.notebookcheck.net/News.rss"),
    ("LaptopMag",          "https://www.laptopmag.com/feeds/all"),
    ("Tom's Guide",       "https://www.tomsguide.com/feeds/all"),
    # ── India Tech News ───────────────────────────────
    ("91Mobiles",          "https://www.91mobiles.com/hub/feed/"),
    ("MySmartPrice",       "https://www.mysmartprice.com/feed/"),
    ("GizmoChina",         "https://www.gizmochina.com/feed/"),
    ("Pricebaba",          "https://pricebaba.com/blog/feed/"),
    ("GadgetsNow",         "https://www.gadgetsnow.com/rssfeedstopstories.cms"),
]

def fetch_from_rss(feed_name, feed_url, keyword):
    """Fetch latest articles from an RSS feed matching a keyword."""
    try:
        import xml.etree.ElementTree as ET
        r = requests.get(feed_url, timeout=8,
                        headers={"User-Agent": "Mozilla/5.0"})
        if r.status_code != 200:
            return []

        root = ET.fromstring(r.content)
        ns = {"atom": "http://www.w3.org/2005/Atom"}

        articles = []
        # Handle both RSS and Atom feeds
        items = root.findall(".//item") or root.findall(".//atom:entry", ns)

        for item in items[:10]:
            # Get title
            title_el = item.find("title")
            title = title_el.text if title_el is not None else ""
            if not title:
                continue

            # Filter by keyword
            if keyword.lower().split()[0] not in title.lower():
                continue

            # Get description
            desc_el = item.find("description") or item.find("summary")
            description = desc_el.text if desc_el is not None else ""
            if description:
                import re
                description = re.sub(r"<[^>]+>", "", description)[:300]

            # Get link
            link_el = item.find("link")
            link = link_el.text if link_el is not None else feed_url

            # Get date
            date_el = item.find("pubDate") or item.find("published")
            published = date_el.text if date_el is not None else ""

            if title and description:
                articles.append({
                    "title":       title.strip(),
                    "description": description.strip(),
                    "content":     description.strip(),
                    "url":         link.strip() if link else feed_url,
                    "source":      feed_name,
                    "published":   published or "2026-03-15T00:00:00Z",
                })

        return articles[:3]

    except Exception:
        return []


def fetch_from_newsapi(query, count=3):
    """Fetch from NewsAPI (backup source)."""
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
        return [
            {"title": a["title"], "description": a.get("description") or "",
             "content": a.get("content") or "", "url": a["url"],
             "source": a["source"]["name"], "published": a["publishedAt"]}
            for a in data.get("articles", [])
            if a.get("title") and a.get("description")
        ]
    except Exception:
        return []


def fetch_news(query, count=3):
    """Fetch from RSS feeds + NewsAPI combined."""
    print(f"  Searching: '{query}'")
    all_articles = []

    # Extract main keyword from query
    keyword = query.split()[0]

    # Try RSS feeds first (faster and more sources)
    random.shuffle(RSS_FEEDS)
    for feed_name, feed_url in RSS_FEEDS[:8]:
        articles = fetch_from_rss(feed_name, feed_url, keyword)
        all_articles.extend(articles)
        if len(all_articles) >= 3:
            break

    # If RSS didn't find enough, use NewsAPI
    if len(all_articles) < 2:
        newsapi_articles = fetch_from_newsapi(query, count)
        all_articles.extend(newsapi_articles)

    # Remove duplicates by title
    seen = set()
    unique = []
    for a in all_articles:
        if a["title"] not in seen:
            seen.add(a["title"])
            unique.append(a)

    print(f"    {len(unique)} articles found")
    return unique[:count]


def pick_story():
    """Pick best story from all sources."""
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

SYSTEM_PROMPT = """You are a passionate Indian tech journalist writing for "Tech News With AI" (technewsai.me), a blog by Mallikarjun R from Bengaluru, India.

YOUR WRITING IDENTITY:
You are a real person who loves technology. You have personally used many smartphones and laptops. You share genuine opinions, frustrations, and excitement. You are NOT a robot — you are a tech-enthusiast friend explaining things to another friend over chai.

STRICT HUMAN WRITING RULES:
- Start with a personal hook — something like "I have been following this device for weeks and let me tell you..." or "When I first heard about this, I could not believe the price..."
- Share personal opinions throughout — "Honestly, I think...", "In my experience...", "What surprised me was...", "I have to be honest here..."
- Include genuine doubts and criticisms — no device is perfect, mention real drawbacks
- Use conversational transitions — "Now here is the interesting part", "But wait, there is more", "Here is where it gets tricky"
- Vary sentence length — mix short punchy sentences with longer detailed ones
- Add India-specific context — mention how this compares to what people use in Mumbai, Delhi, Bengaluru
- Reference real Indian usage scenarios — auto-rickshaw rides, hot Indian summers, long Bangalore commutes, college students on tight budgets
- NEVER use generic AI phrases like "In conclusion", "It is worth noting", "Furthermore", "Moreover"
- NEVER start paragraphs with the same word twice in a row
- Include at least 3 genuine opinions or personal takes per article

CONTENT DEPTH RULES:
- Explain WHY each spec matters with real-world impact
- BAD: "Has a 5000mAh battery"
- GOOD: "That 5000mAh battery means I can leave home at 7am, use GPS all day through Bengaluru traffic, stream YouTube on breaks, and still have 30% left by midnight — that is genuinely impressive"
- Always include India price (convert USD to INR at 85x, mention EMI options on Flipkart/Amazon India)
- Compare with 2-3 competitors that Indian buyers actually consider
- Mention which variant to buy in India specifically
- Add context about availability — Flipkart, Amazon India, brand stores
- Include actual use cases: college student, office professional, content creator, gamer, parent

QUALITY STANDARDS (Critical for Google AdSense approval):
- Minimum 2500 words — aim for 3000+
- Every section must have unique insights, not just spec repetition
- Each paragraph must add NEW information
- No filler sentences — every sentence must earn its place
- Write like a Forbes India or Gadgets360 journalist
- Add specific details that show genuine research

FORMAT RULES:
- NO bullet points anywhere — flowing paragraphs only
- NO tables — write comparisons in prose
- Use <h2> for main section headings
- Use <h3> for sub-sections within
- Wrap every paragraph in <p> tags
- Clean HTML only, no markdown
- Bold important specs using <strong> tags

SECTIONS TO COVER:
1. Opening Hook — personal angle on why this device matters right now in India
2. First Impressions and Design — materials, build quality, colors available in India, how it feels
3. Display Deep Dive — panel type, size, resolution, refresh rate explained in real terms
4. Camera Analysis — each lens with real-world photo scenarios an Indian user would face
5. Performance and Gaming — chipset explained simply, gaming benchmarks in layman terms
6. Battery Life Reality Check — realistic India usage scenario from morning to night
7. Software Experience — OS version, bloatware situation, update promise
8. India Price and Value — exact Indian pricing, variants, EMI, competitors at same price
9. Who Should Buy This and Who Should Not — specific Indian buyer profiles
10. Final Honest Verdict — genuine recommendation with clear reasoning
11. FAQ — 5 questions real Indian buyers ask before purchasing"""

def write_post(story):
    prompt = f"""Write a detailed, human, and genuinely helpful blog post for Indian tech readers.

NEWS HEADLINE : {story['title']}
NEWS SUMMARY  : {story['description']}
EXTRA DETAILS : {story['content'][:600] if story['content'] else 'Not available'}
SOURCE        : {story['source']}

CRITICAL REQUIREMENTS:
- Write minimum 3000 words
- Sound like a real Indian tech journalist, NOT an AI
- Start with a personal, engaging hook sentence
- Include at least 3 genuine opinions or personal takes
- Mention specific India prices in INR (convert USD x 85)
- Reference Flipkart/Amazon India availability
- Compare with 2 real competitors Indian buyers consider
- Include realistic India usage scenarios (commute, heat, budget)
- Every paragraph must add new value — no filler
- Output clean HTML using only h2, h3, p, strong tags
- First element must be an h2 with a catchy, unique title
- Do NOT include html, head, body tags
- Cover all 10 sections plus FAQ
- End with 5 FAQ questions real Indian buyers ask

Write the complete article now, starting with the h2 title:"""

    def build_footer(story):
        return f"""
<hr>
<p><em><strong>Source:</strong> {story['source']} | <strong>Published:</strong> {story['published'][:10]} | <a href="{story['url']}" target="_blank">Read original article</a></em></p>
<p><em>Stay updated at <a href="https://technewsai.me">Tech News With AI</a>. Follow on <a href="https://www.instagram.com/mallikarjunr_8055">Instagram</a> and join our <a href="https://whatsapp.com/channel/0029VazWwdn0wajoizN5PY3Q">WhatsApp channel</a>.</em></p>
"""

    def parse_response(raw, story):
        raw = re.sub(r"```html\s*", "", raw)
        raw = re.sub(r"```\s*", "", raw)
        raw = raw.strip()
        title = story["title"]
        m = re.search(r"<h2[^>]*>(.*?)</h2>", raw, re.IGNORECASE | re.DOTALL)
        if m:
            title = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        words = len(re.sub(r"<[^>]+>", "", raw).split())
        print(f"    Done - {words} words")
        return title, raw + build_footer(story)

    # Try Grok first (better writing quality)
    if XAI_API_KEY:
        try:
            print("\n  Writing with Grok (xAI)...")
            from openai import OpenAI as OpenAIClient
            grok_client = OpenAIClient(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")
            response = grok_client.chat.completions.create(
                model="grok-3",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user",   "content": prompt}
                ],
                max_tokens=4000,
                temperature=0.8,
            )
            return parse_response(response.choices[0].message.content, story)
        except Exception as e:
            print(f"    Grok error: {e} — falling back to Groq...")

    # Fallback: Groq (always free)
    print("\n  Writing with Groq Llama 3.3 70B...")
    client = Groq(api_key=GROQ_API_KEY)
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
        return parse_response(response.choices[0].message.content, story)
    except Exception as e:
        print(f"    Groq error: {e}")
        raise

# ══════════════════════════════════════════════════════════════════════
#  MODULE 3 — POST TO BLOGGER (using Google OAuth2 token directly)
# ══════════════════════════════════════════════════════════════════════

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

def post_via_email(title, html, labels):
    """Post to Blogger via email — no token, no OAuth needed!"""
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    print(f"  Sending to Blogger via email...")
    gmail_password = os.environ.get("GMAIL_APP_PASSWORD", GMAIL_APP_PASSWORD)

    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = title
        msg["From"]    = GMAIL_ADDRESS
        msg["To"]      = BLOGGER_POST_EMAIL
        msg.attach(MIMEText(html, "html"
