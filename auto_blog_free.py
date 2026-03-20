"""
╔══════════════════════════════════════════════════════════════════════╗
║        TECH NEWS WITH AI — AUTO BLOG SYSTEM (100% FREE)            ║
║        Blog: technewswithai.blogspot.com                            ║
║        FOCUS: HIGH QUALITY content for AdSense approval            ║
╚══════════════════════════════════════════════════════════════════════╝
"""

# ══════════════════════════════════════════════════════════════════════
#  YOUR FREE API KEYS
# ══════════════════════════════════════════════════════════════════════

GROQ_API_KEY       = "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"
NEWS_API_KEY       = "673bca5ceab54fa8bb7ed0344c8f6d13"
BLOGGER_POST_EMAIL = "mallikarjunr444.technewswithai6361@blogger.com"
GMAIL_ADDRESS      = "mallikarjunr444@gmail.com"
GMAIL_APP_PASSWORD = "oeirtosmlhuwntka"

# ══════════════════════════════════════════════════════════════════════
#  SETTINGS — 1 HIGH QUALITY article per day for AdSense
# ══════════════════════════════════════════════════════════════════════

ARTICLES_PER_RUN = 1      # 1 per day — quality over quantity
POST_AS_DRAFT    = False

# Official brand newsrooms
BRAND_SOURCES = {
    "OPPO":     "https://www.oppo.com/en/newsroom/",
    "Honor":    "https://www.hihonor.com/global/news/",
    "Huawei":   "https://consumer.huawei.com/en/press/news/",
    "Samsung":  "https://news.samsung.com/global/",
    "OnePlus":  "https://www.oneplus.com/global/newsroom",
    "Xiaomi":   "https://blog.mi.com/en/",
    "Realme":   "https://www.realme.com/in/info/news",
    "Vivo":     "https://www.vivo.com/en/news",
    "Nothing":  "https://nothing.tech/blogs/news",
    "Motorola": "https://newsroom.motorola.com/",
    "Apple":    "https://www.apple.com/newsroom/",
    "Google":   "https://blog.google/products/pixel/",
}

import os, sys, json, time, random, requests, datetime, re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText

def require(package, install):
    try:
        __import__(package)
    except ImportError:
        print(f"Missing: {package}  Fix: pip install {install}")
        sys.exit(1)

require("groq", "groq")
from groq import Groq

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
}

# ══════════════════════════════════════════════════════════════════════
#  MODULE 1 — SCRAPE REAL SPECS
# ══════════════════════════════════════════════════════════════════════

def scrape_gsmarena(device_name):
    """Get full specs from GSMArena."""
    print(f"    Scraping GSMArena: {device_name[:50]}")
    try:
        query = device_name.replace(" ", "+")
        r = requests.get(
            f"https://www.gsmarena.com/search.php3?sQuickSearch={query}",
            headers=HEADERS, timeout=10)

        links = re.findall(r'href="([a-z0-9_]+-\d+\.php)"', r.text)
        if not links:
            return {}

        r2 = requests.get(
            f"https://www.gsmarena.com/{links[0]}",
            headers=HEADERS, timeout=10)

        specs = {}
        pairs = re.findall(
            r'<td class="ttl">.*?<a[^>]*>([^<]+)</a>.*?</td>\s*<td class="nfo">([^<]+)',
            r2.text, re.DOTALL)
        for k, v in pairs:
            specs[k.strip()] = v.strip()

        specs['gsmarena_url'] = f"https://www.gsmarena.com/{links[0]}"
        print(f"      ✅ {len(specs)} specs found")
        return specs
    except Exception as e:
        print(f"      GSMArena: {e}")
        return {}


def scrape_page_content(url):
    """Scrape full text content from any URL."""
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        # Remove scripts and styles
        text = re.sub(r'<script[^>]*>.*?</script>', '', r.text, flags=re.DOTALL)
        text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
        # Get clean text
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text[:3000]
    except:
        return ""


def fetch_newsapi(query):
    """Fetch from NewsAPI."""
    try:
        r = requests.get(
            "https://newsapi.org/v2/everything",
            params={"q": query, "language": "en",
                    "sortBy": "publishedAt", "pageSize": 5,
                    "apiKey": NEWS_API_KEY},
            timeout=10)
        data = r.json()
        if data.get("status") != "ok":
            return []
        return [a for a in data.get("articles", [])
                if a.get("title") and a.get("description")]
    except:
        return []


def pick_story():
    """Find latest device news with real specs."""
    print("\n  Finding latest tech news...")

    # Try brand newsrooms
    brands = list(BRAND_SOURCES.items())
    random.shuffle(brands)

    for brand, url in brands[:5]:
        try:
            r = requests.get(url, headers=HEADERS, timeout=8)
            titles = re.findall(r'<h[123][^>]*>([^<]{20,120})</h[123]>', r.text)
            titles = [t.strip() for t in titles if
                      any(w in t.lower() for w in
                          ['launch','new','release','pro','series',
                           'phone','smartphone','announce'])]
            if titles:
                headline = titles[0]
                print(f"\n  Found: {headline[:60]}")
                print(f"  Brand: {brand}")

                # Get specs and article content
                specs = scrape_gsmarena(headline)
                article_content = scrape_page_content(url)

                return {
                    "title":    headline,
                    "brand":    brand,
                    "source":   f"{brand} Official",
                    "url":      url,
                    "specs":    specs,
                    "content":  article_content[:2000],
                    "published": datetime.datetime.now().isoformat(),
                    "description": f"Latest {brand} device news"
                }
        except:
            continue

    # Fallback NewsAPI
    topics = [
        "OPPO phone launch India 2026",
        "Honor smartphone launch specs",
        "Samsung Galaxy launch India",
        "OnePlus launch specifications India",
        "iPhone launch specs 2026",
        "Xiaomi Redmi launch India",
        "laptop launch India 2026",
    ]
    random.shuffle(topics)
    for topic in topics:
        articles = fetch_newsapi(topic)
        if articles:
            a = articles[0]
            brand = topic.split()[0]
            specs = scrape_gsmarena(a["title"])
            # Also scrape the article URL for more content
            extra = scrape_page_content(a["url"])
            return {
                "title":     a["title"],
                "brand":     brand,
                "source":    a["source"]["name"],
                "url":       a["url"],
                "specs":     specs,
                "content":   (a.get("content","") or "") + extra,
                "published": a["publishedAt"],
                "description": a.get("description","")
            }
    return None


# ══════════════════════════════════════════════════════════════════════
#  MODULE 2 — HIGH QUALITY AI WRITER
# ══════════════════════════════════════════════════════════════════════

SYSTEM_PROMPT = """You are a professional tech journalist writing for "Tech News With AI" (technewswithai.blogspot.com) by Mallikarjun R, Bengaluru, India.

YOUR WRITING STYLE:
- Write like a passionate tech expert explaining to a smart friend
- Simple English that anyone can understand
- Use phrases: "here is the thing", "let us break this down", "this is where it gets interesting"
- Address readers directly: "you will love", "when you pick this up"
- Every paragraph must be UNIQUE and add NEW information
- Never repeat the same point twice
- Write with DEPTH — go beyond surface level information

GOOGLE ADSENSE CONTENT REQUIREMENTS:
- MINIMUM 3000 words — longer articles get better AdSense scores
- Write COMPLETE full articles — never leave any section empty or shallow
- Every section must have minimum 4 detailed paragraphs
- Each paragraph minimum 4-5 sentences
- Use ONLY real specs provided — never invent specs
- Explain every technical term simply when first used
- Give real world examples in every section
- Compare with exactly 3 competitor devices
- Include exact India pricing with EMI breakdown
- Add unique personal insights not found on other blogs
- Write as if you personally tested the device

IMPORTANT — FULL CONTENT ON EVERY PAGE:
- Start article with a 3 paragraph introduction BEFORE any heading
- Every section must be COMPLETE with full paragraphs
- Never use placeholder text or incomplete sentences
- Each FAQ answer must be minimum 3 sentences

FORMAT RULES:
- NO bullet points anywhere — always flowing paragraphs only
- NO tables — write all specs as descriptive sentences
- Use <h2> for main sections
- Use <h3> for sub sections
- Every paragraph wrapped in <p> tags
- Clean HTML only — no markdown, no code fences
- Add meta description as first hidden paragraph

MANDATORY SECTIONS (each minimum 4 paragraphs):
1. Opening Introduction — 3 paragraphs before first h2 heading
2. Design and Build Quality — materials, dimensions, colors, feel in hand
3. Display Technology Explained — panel, size, resolution, refresh rate simply explained
4. Camera System Complete Guide — every lens, real world photos, video
5. Processor Performance and Gaming — chip, speed, gaming, multitasking, heating
6. Battery Life and Charging — capacity, real usage, charging speed, longevity
7. Software and AI Features — OS, unique features, AI tools, updates
8. India Price and Value Analysis — price, EMI, variants, value for money
9. Who Should Buy and Who Should Not — honest advice for different buyers
10. Top 3 Alternatives — honest comparison with competitors
11. Final Verdict — clear recommendation with specific reasons
12. Frequently Asked Questions — 7 questions with detailed 3 sentence answers each"""


def write_post(story):
    print("\n  Writing HIGH QUALITY article with Groq...")
    client = Groq(api_key=GROQ_API_KEY)

    # Build comprehensive specs text
    specs_text = ""
    if story.get("specs"):
        specs_items = list(story["specs"].items())[:40]
        specs_text = "\n".join([f"  {k}: {v}" for k, v in specs_items])

    prompt = f"""Write a COMPREHENSIVE, HIGH QUALITY blog article about this device.
This article must be good enough for Google AdSense approval — minimum 2500 words.

DEVICE DETAILS:
Name    : {story['title']}
Brand   : {story.get('brand','Unknown')}
Source  : {story['source']}

REAL SPECIFICATIONS (use these — do not invent specs):
{specs_text if specs_text else "Specifications being compiled from official source"}

ADDITIONAL CONTEXT:
{story.get('description','')}
{story.get('content','')[:1000]}

WRITING REQUIREMENTS:
1. Minimum 2500 words — each section needs 3-4 detailed paragraphs
2. First h2 tag must be a catchy, SEO-friendly article title
3. Use real specs provided — explain what each spec means for real users
4. Include India pricing (estimate if not provided: search context clues)
5. Compare with Samsung, iPhone, and one Indian brand
6. Write 12 sections as instructed
7. Make every paragraph unique — no repetition
8. Add real world use cases and examples
9. Sound like a human expert, not a robot

Output clean HTML with h2, h3, p tags only. No html/head/body tags.
Write the complete article now:"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": prompt}
            ],
            max_tokens=7000,
            temperature=0.75,
        )
        raw = response.choices[0].message.content
        raw = re.sub(r"```html\s*", "", raw)
        raw = re.sub(r"```\s*", "", raw)
        raw = raw.strip()

        # Extract title
        title = story["title"]
        m = re.search(r"<h2[^>]*>(.*?)</h2>", raw, re.IGNORECASE | re.DOTALL)
        if m:
            title = re.sub(r"<[^>]+>", "", m.group(1)).strip()

        # Add footer
        footer = f"""
<hr>
<p><em><strong>Source:</strong> {story['source']} | <strong>Date:</strong> {story['published'][:10]}</em></p>
<p><em>For the latest tech news, phone reviews and laptop comparisons visit <a href="https://technewswithai.blogspot.com">Tech News With AI</a>. Follow us on <a href="https://www.instagram.com/mallikarjunr_8055">Instagram</a> and join our <a href="https://whatsapp.com/channel/0029VazWwdn0wajoizN5PY3Q">WhatsApp channel</a> for daily updates.</em></p>
"""
        words = len(re.sub(r"<[^>]+>", "", raw).split())
        print(f"    ✅ Done — {words} words")

        if words < 2000:
            print(f"    ⚠️  Article too short ({words} words)! Extending...")
            ext_response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system",    "content": SYSTEM_PROMPT},
                    {"role": "user",      "content": prompt},
                    {"role": "assistant", "content": raw},
                    {"role": "user",      "content": """The article needs more content for AdSense approval.
Please add detailed content to these sections:
1. Expand Camera section with 3 more paragraphs about photography tips
2. Expand Performance section with gaming benchmarks explanation
3. Expand Battery section with real world usage scenarios
4. Add 3 more FAQ answers
5. Expand Final Verdict with detailed reasoning
Add minimum 1000 more words. Output only the additional HTML content."""}
                ],
                max_tokens=3000,
                temperature=0.75,
            )
            extra = ext_response.choices[0].message.content
            extra = re.sub(r"```html|```", "", extra).strip()
            raw = raw + extra
            words = len(re.sub(r"<[^>]+>", "", raw).split())
            print(f"    ✅ Extended to {words} words")

        return title, raw + footer

    except Exception as e:
        print(f"    ❌ Groq error: {e}")
        raise


# ══════════════════════════════════════════════════════════════════════
#  MODULE 3 — POST VIA EMAIL
# ══════════════════════════════════════════════════════════════════════

def auto_labels(title, html):
    text = (title + " " + html[:300]).lower()
    labels = ["Tech News", "Specifications", "Review"]
    MAP = {
        "oppo":    ["OPPO","Android"],
        "honor":   ["Honor","Android"],
        "huawei":  ["Huawei","Android"],
        "iphone":  ["iPhone","Apple"],
        "samsung": ["Samsung","Android"],
        "macbook": ["MacBook","Laptop"],
        "oneplus": ["OnePlus","Android"],
        "realme":  ["Realme","Android"],
        "xiaomi":  ["Xiaomi","Android"],
        "nothing": ["Nothing Phone"],
        "pixel":   ["Google Pixel"],
        "laptop":  ["Laptop"],
        "vivo":    ["Vivo","Android"],
        "iqoo":    ["iQOO","Android"],
        "motorola":["Motorola"],
        "india":   ["Price in India"],
        "review":  ["Review"],
        "specs":   ["Specifications"],
    }
    for kw, tags in MAP.items():
        if kw in text:
            for t in tags:
                if t not in labels:
                    labels.append(t)
    labels.append(str(datetime.datetime.now().year))
    return list(set(labels))[:10]


def post_via_email(title, html, labels):
    print(f"  Posting to Blogger via email...")
    gmail_password = os.environ.get("GMAIL_APP_PASSWORD", GMAIL_APP_PASSWORD)
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = title
        msg["From"]    = GMAIL_ADDRESS
        msg["To"]      = BLOGGER_POST_EMAIL
        msg.attach(MIMEText(html, "html"))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_ADDRESS, gmail_password)
            server.sendmail(GMAIL_ADDRESS, BLOGGER_POST_EMAIL, msg.as_string())
        print(f"  ✅ Posted!")
        print(f"  🔗 https://technewswithai.blogspot.com")
        return "https://technewswithai.blogspot.com"
    except Exception as e:
        print(f"  ❌ Email error: {e}")
        raise


def post_article(title, html, labels):
    print(f"\n  Article: {title[:60]}...")
    return post_via_email(title, html, labels)


def save_log(title, url, words):
    log_file = "posted_articles.json"
    log = []
    if os.path.exists(log_file):
        try:
            with open(log_file) as f:
                log = json.load(f)
        except:
            log = []
    log.append({"title": title, "url": url, "words": words,
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
║    HIGH QUALITY — AdSense Ready                     ║
║    technewswithai.blogspot.com                      ║
╚══════════════════════════════════════════════════════╝""")

    success = 0
    for i in range(ARTICLES_PER_RUN):
        try:
            print(f"\n{'═'*54}")
            print(f"  Article {i+1} of {ARTICLES_PER_RUN}")
            print(f"{'═'*54}")

            story = pick_story()
            if not story:
                print("  No story found!")
                continue

            title, html = write_post(story)
            words  = len(re.sub(r"<[^>]+>", "", html).split())
            labels = auto_labels(title, html)
            url    = post_article(title, html, labels)
            save_log(title, url, words)
            success += 1

            if i < ARTICLES_PER_RUN - 1:
                print("  Waiting 30 seconds...")
                time.sleep(30)

        except KeyboardInterrupt:
            print("\nStopped.")
            break
        except Exception as e:
            print(f"\nFailed: {e}")
            continue

    print(f"""
╔══════════════════════════════════════════════════════╗
║  ✅ DONE! {success}/{ARTICLES_PER_RUN} article(s) posted!
║  Quality articles for AdSense approval!
║  technewswithai.blogspot.com
╚══════════════════════════════════════════════════════╝""")


if __name__ == "__main__":
    main()
            
