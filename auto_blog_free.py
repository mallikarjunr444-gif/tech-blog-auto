"""
╔══════════════════════════════════════════════════════════════════════╗
║   TECH NEWS WITH AI — COMPLETE AUTO BLOG SYSTEM (100% FREE)        ║
║   Blog: technewswithai.blogspot.com                                 ║
║   Covers: Phones, Laptops, Audio, Tablets, Wearables               ║
║   Sources: Official Sites + GSMArena + Rumor Sites + NewsAPI        ║
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
#  SETTINGS
# ══════════════════════════════════════════════════════════════════════

ARTICLES_PER_RUN = 1
POST_AS_DRAFT    = False

# ══════════════════════════════════════════════════════════════════════
#  CATEGORY DEFINITIONS — Each with official sources + rumor sites
# ══════════════════════════════════════════════════════════════════════

CATEGORIES = {

    # ── SMARTPHONES ─────────────────────────────────────────────────
    "smartphone": {
        "labels": ["Smartphones", "Mobile", "Tech News"],
        "official_sources": [
            ("Samsung Newsroom",   "https://news.samsung.com/global/"),
            ("Apple Newsroom",     "https://www.apple.com/newsroom/"),
            ("OnePlus Newsroom",   "https://www.oneplus.com/global/newsroom"),
            ("OPPO Newsroom",      "https://www.oppo.com/en/newsroom/"),
            ("Xiaomi Blog",        "https://blog.mi.com/en/"),
            ("Realme News",        "https://www.realme.com/in/info/news"),
            ("Vivo News",          "https://www.vivo.com/en/news"),
            ("Nothing Blog",       "https://nothing.tech/blogs/news"),
            ("Motorola Newsroom",  "https://newsroom.motorola.com/"),
            ("Honor News",         "https://www.hihonor.com/global/news/"),
            ("Huawei News",        "https://consumer.huawei.com/en/press/news/"),
            ("Google Pixel Blog",  "https://blog.google/products/pixel/"),
            ("Nokia News",         "https://www.nokia.com/phones/en_int/news/"),
            ("iQOO Newsroom",      "https://www.iqoo.com/in/newsroom.html"),
        ],
        "rumor_sources": [
            ("GSMArena News",      "https://www.gsmarena.com/news.php3"),
            ("91Mobiles",          "https://www.91mobiles.com/hub/feed/"),
            ("MySmartPrice",       "https://www.mysmartprice.com/feed/"),
            ("PhoneArena",         "https://www.phonearena.com/phones/articles/rss"),
            ("XDA Developers",     "https://www.xda-developers.com/feed/"),
            ("AndroidAuthority",   "https://www.androidauthority.com/feed/"),
            ("9to5Google",         "https://9to5google.com/feed/"),
            ("9to5Mac",            "https://9to5mac.com/feed/"),
            ("MacRumors",          "https://feeds.macrumors.com/MacRumors-All"),
            ("SamMobile",          "https://www.sammobile.com/feed/"),
            ("GizmoChina",         "https://www.gizmochina.com/feed/"),
        ],
        "search_topics": [
            "Samsung Galaxy launch specs India 2026",
            "iPhone launch specs price India 2026",
            "OnePlus launch specifications India 2026",
            "OPPO phone launch India 2026",
            "Xiaomi Redmi Poco launch India 2026",
            "Realme phone launch India 2026",
            "Vivo iQOO launch India 2026",
            "Nothing phone launch specs 2026",
            "Honor Huawei phone launch 2026",
            "Google Pixel launch India 2026",
            "Motorola phone launch India 2026",
        ],
        "writing_prompt": """Write a COMPLETE smartphone review/news article.
Cover these sections in detail (minimum 4 paragraphs each):
1. Opening Introduction (3 paragraphs before first heading — why this phone matters)
2. Design and Build Quality (materials, dimensions, colors, weight, feel)
3. Display Technology (type, size, resolution, refresh rate, brightness — explained simply)
4. Camera System Complete Guide (every lens, aperture, features, real world use, video)
5. Processor and Performance (chip name explained, gaming, multitasking, heating, benchmark context)
6. Battery Life and Charging (mAh, real world hours, charging speed, wireless charging)
7. Software and Features (Android version, UI, AI features, unique software)
8. Connectivity and Other Features (5G bands, WiFi, Bluetooth, NFC, speakers, biometrics)
9. India Price and Variants (all variants, EMI, launch offers, value analysis)
10. Who Should Buy This Phone (students, professionals, gamers, photographers)
11. Top 3 Alternatives (honest comparison with competitors)
12. Final Verdict (clear buy/wait/skip with specific reasons)
13. FAQ — 7 questions specific to this phone with detailed answers"""
    },

    # ── LAPTOPS ─────────────────────────────────────────────────────
    "laptop": {
        "labels": ["Laptops", "Computers", "Tech News"],
        "official_sources": [
            ("Apple MacBook News",   "https://www.apple.com/newsroom/"),
            ("Dell Newsroom",        "https://www.dell.com/en-us/blog/"),
            ("HP Press Room",        "https://press.hp.com/us/en/home.html"),
            ("Lenovo News",          "https://news.lenovo.com/"),
            ("ASUS Newsroom",        "https://www.asus.com/in/news/"),
            ("Acer Newsroom",        "https://acernewsroom.com/"),
            ("Microsoft Surface",    "https://blogs.microsoft.com/blog/"),
            ("Samsung Newsroom",     "https://news.samsung.com/global/"),
            ("LG Newsroom",          "https://www.lgnewsroom.com/"),
            ("Razer Blog",           "https://www.razer.com/blog/"),
            ("MSI News",             "https://www.msi.com/blog/"),
        ],
        "rumor_sources": [
            ("NotebookCheck",        "https://www.notebookcheck.net/News.rss"),
            ("LaptopMag",            "https://www.laptopmag.com/feeds/all"),
            ("Tom's Guide Laptops",  "https://www.tomsguide.com/feeds/all"),
            ("The Verge",            "https://www.theverge.com/rss/index.xml"),
            ("TechCrunch",           "https://techcrunch.com/feed/"),
            ("Engadget",             "https://www.engadget.com/rss.xml"),
            ("CNET",                 "https://www.cnet.com/rss/news/"),
            ("Wired",                "https://www.wired.com/feed/rss"),
        ],
        "search_topics": [
            "MacBook launch price India 2026",
            "Dell laptop launch India 2026",
            "HP laptop launch specifications 2026",
            "Lenovo laptop launch India 2026",
            "ASUS laptop launch India 2026",
            "Acer laptop launch India 2026",
            "Microsoft Surface launch 2026",
            "gaming laptop launch India 2026",
            "best laptop students India 2026",
        ],
        "writing_prompt": """Write a COMPLETE laptop review/news article.
Cover these sections in detail (minimum 4 paragraphs each):
1. Opening Introduction (3 paragraphs — who needs this laptop and why)
2. Design and Build (materials, chassis, hinge, weight, ports, keyboard quality)
3. Display Quality (type, size, resolution, refresh rate, color accuracy, brightness)
4. Performance and Benchmarks (processor generation, real world tasks, multitasking)
5. Graphics and Gaming (integrated/dedicated GPU, gaming performance, frame rates)
6. RAM and Storage (configurations, upgrade options, SSD speeds)
7. Battery Life (capacity, real world hours for different tasks, charging speed)
8. Keyboard, Trackpad and Ports (typing experience, trackpad precision, port selection)
9. Thermal Management (cooling system, fan noise, sustained performance)
10. India Price and Variants (all configs, EMI options, student discounts)
11. Who Should Buy This (students, professionals, content creators, gamers)
12. Top 3 Alternatives (honest comparison with similar laptops)
13. Final Verdict (clear buy/wait/skip recommendation)
14. FAQ — 7 laptop specific questions with detailed answers"""
    },

    # ── AUDIO (AirPods, Earphones, Headphones) ──────────────────────
    "audio": {
        "labels": ["Audio", "Earphones", "Headphones", "AirPods", "TWS", "Tech News"],
        "official_sources": [
            ("Apple AirPods News",   "https://www.apple.com/newsroom/"),
            ("Sony Newsroom",        "https://presscentre.sony.eu/pressreleases/"),
            ("Bose Newsroom",        "https://www.bose.com/en_us/about_bose.html"),
            ("Samsung Audio News",   "https://news.samsung.com/global/"),
            ("OnePlus Buds News",    "https://www.oneplus.com/global/newsroom"),
            ("Boat Audio News",      "https://www.boat-lifestyle.com/blogs/news"),
            ("JBL News",             "https://www.jbl.com/"),
            ("Noise Buds News",      "https://www.gonoise.com/blogs/"),
        ],
        "rumor_sources": [
            ("9to5Mac AirPods",      "https://9to5mac.com/feed/"),
            ("MacRumors Audio",      "https://feeds.macrumors.com/MacRumors-All"),
            ("The Verge Audio",      "https://www.theverge.com/rss/index.xml"),
            ("Engadget Audio",       "https://www.engadget.com/rss.xml"),
            ("CNET Audio",           "https://www.cnet.com/rss/news/"),
            ("91Mobiles Audio",      "https://www.91mobiles.com/hub/feed/"),
            ("MySmartPrice Audio",   "https://www.mysmartprice.com/feed/"),
        ],
        "search_topics": [
            "AirPods launch specs India 2026",
            "Sony WH headphones launch India 2026",
            "Samsung Galaxy Buds launch 2026",
            "OnePlus Buds launch India 2026",
            "Boat earphones launch India 2026",
            "best TWS earbuds India 2026",
            "noise cancelling headphones launch India 2026",
            "wireless earphones launch India 2026",
        ],
        "writing_prompt": """Write a COMPLETE audio product review/news article.
Cover these sections in detail (minimum 4 paragraphs each):
1. Opening Introduction (3 paragraphs — why these earphones matter)
2. Design and Build Quality (form factor, materials, colors, fit, comfort for long wear)
3. Sound Quality Deep Dive (bass, mids, highs, soundstage, explained simply for non-audiophiles)
4. Active Noise Cancellation (ANC strength, transparency mode, wind noise handling)
5. Call Quality and Microphones (mic clarity, noise rejection, conference call performance)
6. Battery Life (earbuds battery, case battery, charging speed, actual usage hours)
7. Connectivity (Bluetooth version, multipoint, latency for gaming/video, codec support)
8. Smart Features and App (EQ customization, touch controls, voice assistant, auto-pause)
9. Comfort and Fit (ear tip sizes, ear wing support, long session comfort, sports use)
10. India Price and Variants (price, colors available, EMI, value comparison)
11. Who Should Buy These (music lovers, commuters, gym users, gamers, professionals)
12. Top 3 Alternatives (honest comparison with similar priced options)
13. Final Verdict (clear buy/wait/skip with specific reasons)
14. FAQ — 7 audio specific questions with detailed answers"""
    },

    # ── TABLETS ─────────────────────────────────────────────────────
    "tablet": {
        "labels": ["Tablets", "iPad", "Tech News"],
        "official_sources": [
            ("Apple iPad News",      "https://www.apple.com/newsroom/"),
            ("Samsung Tab News",     "https://news.samsung.com/global/"),
            ("OnePlus Pad News",     "https://www.oneplus.com/global/newsroom"),
            ("Xiaomi Pad News",      "https://blog.mi.com/en/"),
            ("Lenovo Tab News",      "https://news.lenovo.com/"),
        ],
        "rumor_sources": [
            ("9to5Mac iPad",         "https://9to5mac.com/feed/"),
            ("MacRumors iPad",       "https://feeds.macrumors.com/MacRumors-All"),
            ("AndroidAuthority Tab", "https://www.androidauthority.com/feed/"),
            ("The Verge Tablets",    "https://www.theverge.com/rss/index.xml"),
        ],
        "search_topics": [
            "iPad launch specs India 2026",
            "Samsung Galaxy Tab launch India 2026",
            "OnePlus Pad launch India 2026",
            "Xiaomi Pad launch India 2026",
            "best tablet India 2026",
        ],
        "writing_prompt": """Write a COMPLETE tablet review/news article.
Cover these sections in detail (minimum 4 paragraphs each):
1. Opening Introduction (3 paragraphs — why this tablet matters)
2. Design and Build (materials, weight, thinness, ports, accessories)
3. Display Quality (size, resolution, refresh rate, color, brightness, outdoor use)
4. Performance (chip, RAM, real world tasks, creative work, gaming)
5. Camera System (rear and front cameras, video calling, document scanning)
6. Battery Life (capacity, hours for different tasks, charging speed)
7. Software and Productivity (OS, split screen, stylus support, keyboard support)
8. India Price and Variants (storage configs, 5G vs WiFi, accessories cost)
9. Who Should Buy This (students, artists, professionals, entertainment)
10. Top 3 Alternatives (honest comparison)
11. Final Verdict (clear recommendation)
12. FAQ — 7 tablet specific questions"""
    },

    # ── SMARTWATCHES AND WEARABLES ───────────────────────────────────
    "wearable": {
        "labels": ["Smartwatch", "Wearables", "Fitness Band", "Tech News"],
        "official_sources": [
            ("Apple Watch News",     "https://www.apple.com/newsroom/"),
            ("Samsung Watch News",   "https://news.samsung.com/global/"),
            ("OnePlus Watch News",   "https://www.oneplus.com/global/newsroom"),
            ("Xiaomi Watch News",    "https://blog.mi.com/en/"),
            ("Boat Watch News",      "https://www.boat-lifestyle.com/blogs/news"),
            ("Noise Watch News",     "https://www.gonoise.com/blogs/"),
            ("Garmin News",          "https://www.garmin.com/en-US/newsroom/"),
            ("Fitbit News",          "https://blog.fitbit.com/"),
        ],
        "rumor_sources": [
            ("9to5Mac Watch",        "https://9to5mac.com/feed/"),
            ("AndroidAuthority",     "https://www.androidauthority.com/feed/"),
            ("91Mobiles Watch",      "https://www.91mobiles.com/hub/feed/"),
            ("The Verge Wearables",  "https://www.theverge.com/rss/index.xml"),
        ],
        "search_topics": [
            "Apple Watch launch specs India 2026",
            "Samsung Galaxy Watch launch India 2026",
            "smartwatch launch India 2026",
            "fitness band launch India 2026",
            "best smartwatch under 5000 India 2026",
        ],
        "writing_prompt": """Write a COMPLETE smartwatch/wearable review/news article.
Cover these sections in detail (minimum 4 paragraphs each):
1. Opening Introduction (3 paragraphs — why this wearable matters)
2. Design and Build (case material, strap options, colors, weight, water resistance)
3. Display (type, size, brightness, always-on, readability outdoors)
4. Health and Fitness Features (heart rate, SpO2, sleep, stress, ECG, sports modes)
5. Smart Features (notifications, calls, apps, voice assistant, NFC payments)
6. Battery Life (days per charge, charging speed, battery saving modes)
7. Connectivity (Bluetooth, WiFi, LTE option, GPS accuracy, phone compatibility)
8. App Ecosystem (companion app, third party apps, data analysis)
9. India Price and Variants (strap options, sizes, EMI, value)
10. Who Should Buy This (fitness enthusiasts, professionals, casual users)
11. Top 3 Alternatives (honest comparison)
12. Final Verdict (clear recommendation)
13. FAQ — 7 wearable specific questions"""
    },

    # ── SMART TVs ────────────────────────────────────────────────────
    "tv": {
        "labels": ["Smart TV", "Television", "Tech News"],
        "official_sources": [
            ("Samsung TV News",      "https://news.samsung.com/global/"),
            ("LG TV News",           "https://www.lgnewsroom.com/"),
            ("Sony TV News",         "https://presscentre.sony.eu/pressreleases/"),
            ("Mi TV News",           "https://blog.mi.com/en/"),
            ("OnePlus TV News",      "https://www.oneplus.com/global/newsroom"),
        ],
        "rumor_sources": [
            ("FlatpanelsHD",         "https://www.flatpanelshd.com/"),
            ("The Verge TV",         "https://www.theverge.com/rss/index.xml"),
            ("CNET TV",              "https://www.cnet.com/rss/news/"),
            ("91Mobiles TV",         "https://www.91mobiles.com/hub/feed/"),
        ],
        "search_topics": [
            "Samsung QLED TV launch India 2026",
            "LG OLED TV launch India 2026",
            "Mi TV launch India 2026",
            "smart TV launch India 2026",
            "best smart TV under 50000 India",
        ],
        "writing_prompt": """Write a COMPLETE Smart TV review/news article.
Cover these sections in detail (minimum 4 paragraphs each):
1. Opening Introduction (3 paragraphs — why this TV matters)
2. Design and Build (bezels, stand, wall mount, materials, remote)
3. Display Technology (panel type, resolution, HDR, refresh rate, brightness)
4. Picture Quality (color accuracy, black levels, HDR performance, gaming mode)
5. Sound System (speaker watts, Dolby Atmos, bass, clarity)
6. Smart Features (OS, apps, voice control, casting, smart home)
7. Connectivity (HDMI, USB, Bluetooth, WiFi, gaming ports)
8. India Price and Variants (sizes, models, EMI, launch offers)
9. Who Should Buy This (movie lovers, gamers, sports fans, families)
10. Top 3 Alternatives (honest comparison)
11. Final Verdict (clear recommendation)
12. FAQ — 7 TV specific questions"""
    },
}

# ══════════════════════════════════════════════════════════════════════
#  DO NOT EDIT BELOW
# ══════════════════════════════════════════════════════════════════════

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
#  MODULE 1 — SCRAPE FROM SOURCES
# ══════════════════════════════════════════════════════════════════════

def scrape_rss(feed_name, feed_url, keyword=""):
    """Fetch articles from RSS feed."""
    try:
        import xml.etree.ElementTree as ET
        r = requests.get(feed_url, headers=HEADERS, timeout=8)
        if r.status_code != 200:
            return []
        root = ET.fromstring(r.content)
        items = root.findall(".//item") or root.findall(".//{http://www.w3.org/2005/Atom}entry")
        articles = []
        for item in items[:10]:
            title_el = item.find("title")
            title = title_el.text if title_el is not None else ""
            if not title or len(title) < 15:
                continue
            if keyword and keyword.lower() not in title.lower():
                continue
            desc_el = item.find("description") or item.find("{http://www.w3.org/2005/Atom}summary")
            description = ""
            if desc_el is not None and desc_el.text:
                description = re.sub(r"<[^>]+>", "", desc_el.text)[:400]
            link_el = item.find("link")
            link = link_el.text if link_el is not None else feed_url
            date_el = item.find("pubDate") or item.find("{http://www.w3.org/2005/Atom}published")
            published = date_el.text if date_el is not None else datetime.datetime.now().isoformat()
            articles.append({
                "title":       title.strip(),
                "description": description.strip(),
                "url":         link.strip() if link else feed_url,
                "source":      feed_name,
                "published":   published,
            })
        return articles[:3]
    except:
        return []


def scrape_official_site(name, url):
    """Scrape headline from official brand newsroom."""
    try:
        r = requests.get(url, headers=HEADERS, timeout=8)
        titles = re.findall(r'<h[123][^>]*>([^<]{20,120})</h[123]>', r.text)
        titles = [t.strip() for t in titles if
                  any(w in t.lower() for w in
                      ['launch','new','release','pro','series',
                       'phone','smart','buds','watch','pad','tab',
                       'book','announce','introduce','unveil'])]
        if titles:
            return {"title": titles[0], "source": name, "url": url,
                    "description": f"Latest news from {name}",
                    "published": datetime.datetime.now().isoformat()}
        return None
    except:
        return None


def scrape_full_page(url):
    """Get full text from a webpage."""
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        text = re.sub(r'<script[^>]*>.*?</script>', '', r.text, flags=re.DOTALL)
        text = re.sub(r'<style[^>]*>.*?</style>',  '', text, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text[:3000]
    except:
        return ""


def scrape_gsmarena_specs(device_name):
    """Get real specs from GSMArena."""
    try:
        query = device_name.replace(" ", "+")
        r = requests.get(
            f"https://www.gsmarena.com/search.php3?sQuickSearch={query}",
            headers=HEADERS, timeout=10)
        links = re.findall(r'href="([a-z0-9_]+-\d+\.php)"', r.text)
        if not links:
            return {}
        r2 = requests.get(f"https://www.gsmarena.com/{links[0]}",
                          headers=HEADERS, timeout=10)
        specs = {}
        pairs = re.findall(
            r'<td class="ttl">.*?<a[^>]*>([^<]+)</a>.*?</td>\s*<td class="nfo">([^<]+)',
            r2.text, re.DOTALL)
        for k, v in pairs:
            specs[k.strip()] = v.strip()
        specs['gsmarena_url'] = f"https://www.gsmarena.com/{links[0]}"
        return specs
    except:
        return {}


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
        return [{"title": a["title"],
                 "description": a.get("description","") or "",
                 "content": a.get("content","") or "",
                 "url": a["url"],
                 "source": a["source"]["name"],
                 "published": a["publishedAt"]}
                for a in data.get("articles",[])
                if a.get("title") and a.get("description")]
    except:
        return []


def pick_story():
    """Pick a story from any category — rotates through all."""
    print("\n  Finding latest tech news from all categories...")

    cat_names = list(CATEGORIES.keys())
    random.shuffle(cat_names)

    for cat_name in cat_names:
        cat = CATEGORIES[cat_name]
        print(f"\n  Trying category: {cat_name.upper()}")

        # Try official sources first
        official = cat["official_sources"].copy()
        random.shuffle(official)
        for name, url in official[:4]:
            story = scrape_official_site(name, url)
            if story:
                story["category"] = cat_name
                story["labels"]   = cat["labels"]
                story["writing_prompt"] = cat["writing_prompt"]
                story["specs"]    = scrape_gsmarena_specs(story["title"])
                story["extra"]    = scrape_full_page(url)[:1500]
                print(f"  ✅ Found from {name}: {story['title'][:60]}")
                return story

        # Try rumor/blog RSS feeds
        rumor = cat["rumor_sources"].copy()
        random.shuffle(rumor)
        for name, url in rumor[:4]:
            articles = scrape_rss(name, url)
            if articles:
                story = articles[0]
                story["category"] = cat_name
                story["labels"]   = cat["labels"]
                story["writing_prompt"] = cat["writing_prompt"]
                story["specs"]    = scrape_gsmarena_specs(story["title"])
                story["extra"]    = scrape_full_page(story["url"])[:1500]
                print(f"  ✅ Found from {name}: {story['title'][:60]}")
                return story

        # Try NewsAPI
        topics = cat["search_topics"].copy()
        random.shuffle(topics)
        for topic in topics[:3]:
            articles = fetch_newsapi(topic)
            if articles:
                a = articles[0]
                story = {
                    "title":    a["title"],
                    "description": a.get("description",""),
                    "url":      a["url"],
                    "source":   a["source"],
                    "published": a["publishedAt"],
                    "category": cat_name,
                    "labels":   cat["labels"],
                    "writing_prompt": cat["writing_prompt"],
                    "specs":    scrape_gsmarena_specs(a["title"]),
                    "extra":    scrape_full_page(a["url"])[:1500],
                }
                print(f"  ✅ Found via NewsAPI: {story['title'][:60]}")
                return story

    return None


# ══════════════════════════════════════════════════════════════════════
#  MODULE 2 — HIGH QUALITY AI WRITER
# ══════════════════════════════════════════════════════════════════════

BASE_SYSTEM_PROMPT = """You are Mallikarjun R, a real tech enthusiast and blogger from Bengaluru, India who runs technewswithai.blogspot.com.

WHO YOU ARE:
- A passionate 19-year-old tech lover who personally uses and tests devices
- You write from your own experience and perspective
- You have strong opinions and share them honestly
- You grew up in India and understand what Indian buyers care about most
- You write the way you talk to your college friends — natural, real, no corporate speak

HUMAN WRITING RULES — CRITICAL FOR ADSENSE:
- Write in first person sometimes: "I think", "in my opinion", "when I tested", "I noticed"
- Use Indian English naturally: "quite good", "value for money", "decent enough"
- Share personal opinions freely: "honestly this disappointed me", "this genuinely impressed me"
- Use conversational transitions: "now here is the interesting part", "but wait", "and honestly", "the thing is"
- Vary sentence length — mix short punchy sentences with longer detailed ones
- Use rhetorical questions: "But does it actually deliver?", "Is it worth your money?"
- Add personal anecdotes: "I was using this during my college commute and noticed..."
- Reference real India scenarios: "using Maps on Bengaluru roads", "watching cricket on it"
- Be honest about flaws — do not just praise everything
- Sound like a REAL PERSON not a product brochure

WHAT TO AVOID — MAKES IT SOUND LIKE AI:
- Never say "In conclusion" or "In summary" or "To summarize"
- Never say "It is worth noting" or "It is important to mention"
- Never start every section the same way
- Never use perfectly balanced sentences everywhere
- Never be overly formal or corporate
- Never list specs without personal opinion
- Avoid overusing "furthermore", "moreover", "additionally"

CONTENT QUALITY:
- MINIMUM 3000 words
- Every section minimum 4 paragraphs
- Each paragraph 4-5 sentences with YOUR personal take
- Use real specs provided — explain them like you are texting a friend
- Compare with real competitors you have actually heard of
- Give India-specific advice: EMI options, Flipkart/Amazon prices, local use cases
- Be specific about who should and should NOT buy this

FORMAT:
- 3 natural introduction paragraphs before first heading
- NO bullet points — only flowing paragraphs
- NO tables — write specs naturally in sentences
- <h2> for main sections, <h3> for sub sections
- Every paragraph in <p> tags
- Clean HTML only — no markdown"""


def write_post(story):
    print(f"\n  Writing {story['category'].upper()} article with Groq...")
    client = Groq(api_key=GROQ_API_KEY)

    # Build specs text
    specs_text = ""
    if story.get("specs"):
        items = list(story["specs"].items())[:40]
        specs_text = "\n".join([f"  {k}: {v}" for k, v in items])

    # Category specific writing prompt
    category_prompt = story.get("writing_prompt", "")

    full_prompt = f"""Write a COMPLETE, HIGH QUALITY tech article for Google AdSense approval.
Minimum 3000 words. Every section needs 4+ detailed paragraphs.

PRODUCT: {story['title']}
CATEGORY: {story['category'].upper()}
SOURCE: {story['source']}
URL: {story['url']}

REAL SPECIFICATIONS (use these — never invent specs):
{specs_text if specs_text else "Full specifications being compiled"}

ADDITIONAL CONTEXT FROM SOURCE:
{story.get('description', '')}
{story.get('extra', '')[:800]}

{category_prompt}

WRITING INSTRUCTIONS:
- Write as Mallikarjun R — a real Indian tech blogger, NOT an AI
- Start with 3 natural introduction paragraphs — share why YOU find this device interesting
- First h2 must be a catchy, curiosity-driven title
- Use real specs — explain them like you are explaining to your college friend
- Include India price with Flipkart/Amazon context and EMI breakdown
- Compare honestly with 3 real competitors — share your actual preference
- Minimum 3000 words — write naturally, do not pad artificially
- Add personal opinions, Indian use cases, honest pros and cons
- Vary your writing style — do not make every paragraph sound the same
- Write in HTML with h2, h3, p tags only — no markdown

Write the complete article now as a real human blogger:"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": BASE_SYSTEM_PROMPT},
                {"role": "user",   "content": full_prompt}
            ],
            max_tokens=7000,
            temperature=0.75,
        )
        raw = response.choices[0].message.content
        raw = re.sub(r"```html|```", "", raw).strip()

        # Get title from first h2
        title = story["title"]
        m = re.search(r"<h2[^>]*>(.*?)</h2>", raw, re.IGNORECASE | re.DOTALL)
        if m:
            title = re.sub(r"<[^>]+>", "", m.group(1)).strip()

        words = len(re.sub(r"<[^>]+>", "", raw).split())
        print(f"    {words} words written")

        # Extend if too short
        if words < 2000:
            print(f"    ⚠️  Too short! Extending...")
            ext = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system",    "content": BASE_SYSTEM_PROMPT},
                    {"role": "user",      "content": full_prompt},
                    {"role": "assistant", "content": raw},
                    {"role": "user",      "content": "Article is too short for AdSense. Add 1200 more words: expand Camera/Audio/Display section with 4 more paragraphs, add 3 more FAQ answers, expand Final Verdict. Output only additional HTML content."}
                ],
                max_tokens=3000,
                temperature=0.75,
            )
            extra = re.sub(r"```html|```", "", ext.choices[0].message.content).strip()
            raw   = raw + extra
            words = len(re.sub(r"<[^>]+>", "", raw).split())
            print(f"    ✅ Extended to {words} words")

        # Footer
        footer = f"""
<hr>
<p><em><strong>Source:</strong> {story['source']} | <strong>Date:</strong> {story['published'][:10]} | <a href="{story['url']}" target="_blank" rel="noopener">Original Article</a></em></p>
<p><em>Stay updated with the latest tech news at <a href="https://technewswithai.blogspot.com">Tech News With AI</a>. Follow us on <a href="https://www.instagram.com/mallikarjunr_8055">Instagram</a> and join our <a href="https://whatsapp.com/channel/0029VazWwdn0wajoizN5PY3Q">WhatsApp channel</a> for daily updates on phones, laptops, audio and more.</em></p>
"""
        print(f"    ✅ Final: {words} words | Category: {story['category']}")
        return title, raw + footer, words

    except Exception as e:
        print(f"    ❌ Groq error: {e}")
        raise


# ══════════════════════════════════════════════════════════════════════
#  MODULE 3 — POST VIA EMAIL
# ══════════════════════════════════════════════════════════════════════

def auto_labels(title, html, base_labels):
    text = (title + " " + html[:400]).lower()
    labels = list(base_labels)
    MAP = {
        "oppo":     ["OPPO"],    "honor":    ["Honor"],
        "huawei":   ["Huawei"],  "iphone":   ["iPhone","Apple"],
        "samsung":  ["Samsung"], "macbook":  ["MacBook"],
        "oneplus":  ["OnePlus"], "realme":   ["Realme"],
        "xiaomi":   ["Xiaomi"],  "nothing":  ["Nothing Phone"],
        "pixel":    ["Google Pixel"], "laptop": ["Laptop"],
        "vivo":     ["Vivo"],    "iqoo":     ["iQOO"],
        "motorola": ["Motorola"],"airpods":  ["AirPods"],
        "earbuds":  ["TWS Earbuds"], "headphone": ["Headphones"],
        "watch":    ["Smartwatch"], "tablet": ["Tablet"],
        "india":    ["Price in India"], "review": ["Review"],
        "2026":     ["2026"],    "launch":   ["New Launch"],
    }
    for kw, tags in MAP.items():
        if kw in text:
            for t in tags:
                if t not in labels:
                    labels.append(t)
    return list(set(labels))[:10]


def post_via_email(title, html):
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
        print(f"  ✅ Posted to Blogger!")
        print(f"  🔗 https://technewswithai.blogspot.com")
        return "https://technewswithai.blogspot.com"
    except Exception as e:
        print(f"  ❌ Email error: {e}")
        raise


def save_log(title, url, words, category):
    log_file = "posted_articles.json"
    log = []
    if os.path.exists(log_file):
        try:
            with open(log_file) as f:
                log = json.load(f)
        except:
            log = []
    log.append({
        "title":     title,
        "url":       url,
        "words":     words,
        "category":  category,
        "posted_at": datetime.datetime.now().isoformat()
    })
    with open(log_file, "w") as f:
        json.dump(log, f, indent=2)
    print(f"  Log saved (total: {len(log)} posts)")


# ══════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════════════╗
║    TECH NEWS WITH AI — COMPLETE AUTO BLOG (100% FREE)          ║
║    Covers: Phones | Laptops | Audio | Tablets | Wearables | TV ║
║    Sources: Official Sites + Rumor Blogs + GSMArena            ║
║    technewswithai.blogspot.com                                  ║
╚══════════════════════════════════════════════════════════════════╝""")

    success = 0
    for i in range(ARTICLES_PER_RUN):
        try:
            print(f"\n{'═'*60}")
            print(f"  Article {i+1} of {ARTICLES_PER_RUN}")
            print(f"{'═'*60}")

            story = pick_story()
            if not story:
                print("  No story found today!")
                continue

            title, html, words = write_post(story)
            labels = auto_labels(title, html, story.get("labels", ["Tech News"]))
            url    = post_via_email(title, html)
            save_log(title, url, words, story.get("category","general"))
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
╔══════════════════════════════════════════════════════════════════╗
║  ✅ DONE! {success}/{ARTICLES_PER_RUN} article(s) posted!
║  High quality content for AdSense approval!
║  technewswithai.blogspot.com
╚══════════════════════════════════════════════════════════════════╝""")


if __name__ == "__main__":
    main()
