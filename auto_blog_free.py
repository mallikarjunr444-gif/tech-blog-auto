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
            
