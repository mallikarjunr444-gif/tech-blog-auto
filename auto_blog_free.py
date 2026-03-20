# TECH NEWS WITH AI - AUTO BLOG v10.0 ADVANCED FINAL
# technewswithai.blogspot.com - Mallikarjun R, Bengaluru
# ================================================================
# SCHEDULE:
#   Daily   → 1 Smartphone/Laptop news + 2 Google search topics
#   Weekly  → Earphones Headphones AirPods PowerBank Smartwatch
#             (each once every 3 weeks rotation)
# ================================================================
# PROCESS:
#   Step 1: Fetch from 40+ official RSS feeds
#   Step 2: Groq writes 3000+ word technical draft
#   Step 3: Groq rewrites as human (Mallikarjun R voice)
#   Step 4: Post to Blogger via email
# ================================================================

GROQ_API_KEY       = "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"
NEWS_API_KEY       = "673bca5ceab54fa8bb7ed0344c8f6d13"
BLOGGER_POST_EMAIL = "mallikarjunr444.technewswithai6361@blogger.com"
GMAIL_ADDRESS      = "mallikarjunr444@gmail.com"
GMAIL_APP_PASSWORD = "oeirtosmlhuwntka"

# ================================================================
# ALL OFFICIAL + REVIEW RSS FEEDS (40+ sources)
# ================================================================
ALL_RSS = [
    # Official phone brands
    ("Samsung Newsroom",   "https://news.samsung.com/global/feed"),
    ("Apple Newsroom",     "https://www.apple.com/newsroom/rss-feed.rss"),
    ("Xiaomi Blog",        "https://blog.mi.com/en/feed/"),
    ("OnePlus Forum",      "https://forums.oneplus.com/forums/oneplus-announcements.15/index.rss"),
    ("Nothing Tech",       "https://nothing.tech/blogs/news.atom"),
    ("Honor News",         "https://www.hihonor.com/global/news/rss/"),
    ("Huawei News",        "https://consumer.huawei.com/en/press/news/rss/"),
    ("Google Pixel",       "https://blog.google/products/pixel/rss/"),
    # Official laptop brands
    ("Dell Blog",          "https://www.dell.com/en-us/blog/feed/"),
    ("HP Newsroom",        "https://press.hp.com/us/en/blogs.rss"),
    ("Lenovo News",        "https://news.lenovo.com/feed/"),
    ("Microsoft Blog",     "https://blogs.microsoft.com/feed/"),
    ("ASUS News",          "https://www.asus.com/in/news/rss/"),
    ("Acer Newsroom",      "https://acernewsroom.com/feed/"),
    # Official audio brands
    ("Boat Blog",          "https://www.boat-lifestyle.com/blogs/all.atom"),
    ("Noise Blog",         "https://www.gonoise.com/blogs/news.atom"),
    ("Sony Audio",         "https://presscentre.sony.eu/pressreleases/rss"),
    # India review sites
    ("GSMArena",           "https://www.gsmarena.com/rss-news-articles.php3"),
    ("91Mobiles",          "https://www.91mobiles.com/hub/feed/"),
    ("MySmartPrice",       "https://www.mysmartprice.com/feed/"),
    ("BGR India",          "https://www.bgr.in/feed/"),
    ("GadgetsNow",         "https://www.gadgetsnow.com/rssfeedstopstories.cms"),
    ("Pricebaba",          "https://pricebaba.com/blog/feed/"),
    ("Fonearena",          "https://www.fonearena.com/blog/feed"),
    # Global review sites
    ("AndroidAuthority",   "https://www.androidauthority.com/feed/"),
    ("XDA Developers",     "https://www.xda-developers.com/feed/"),
    ("9to5Google",         "https://9to5google.com/feed/"),
    ("9to5Mac",            "https://9to5mac.com/feed/"),
    ("MacRumors",          "https://feeds.macrumors.com/MacRumors-All"),
    ("SamMobile",          "https://www.sammobile.com/feed/"),
    ("GizmoChina",         "https://www.gizmochina.com/feed/"),
    ("PhoneArena",         "https://www.phonearena.com/phones/articles/rss"),
    ("The Verge",          "https://www.theverge.com/rss/index.xml"),
    ("TechCrunch",         "https://techcrunch.com/feed/"),
    ("Engadget",           "https://www.engadget.com/rss.xml"),
    ("CNET",               "https://www.cnet.com/rss/news/"),
    ("TechRadar",          "https://www.techradar.com/rss"),
    ("NotebookCheck",      "https://www.notebookcheck.net/News.rss"),
    ("SoundGuys",          "https://www.soundguys.com/feed/"),
    ("PCMag",              "https://www.pcmag.com/feeds/latest"),
    ("Wired",              "https://www.wired.com/feed/rss"),
]

# ================================================================
# CATEGORY STRUCTURES — Unique 12 sections per category
# ================================================================
CAT = {

    "smartphone": {
        "labels": ["Smartphones", "Mobile", "Tech News", "Price in India", "Review", "2026"],
        "detect": ["phone", "smartphone", "android", "iphone", "samsung", "oneplus",
                   "realme", "xiaomi", "oppo", "vivo", "nothing", "honor", "huawei",
                   "pixel", "motorola", "nokia", "infinix", "tecno", "poco", "redmi"],
        "news_topics": [
            "Samsung Galaxy launch India 2026",
            "iPhone launch specs India 2026",
            "OnePlus launch India 2026",
            "Xiaomi Redmi Poco launch India 2026",
            "OPPO Realme launch India 2026",
            "Vivo iQOO launch India 2026",
            "Nothing phone launch 2026",
            "Honor Huawei phone launch 2026",
            "Google Pixel launch India 2026",
            "Motorola Nokia launch India 2026",
        ],
        "search_topics": [
            {"t": "best phone under 10000 India 2026",         "k": ["budget phone", "10000"]},
            {"t": "best phone under 15000 India 2026",         "k": ["phone 15000", "India"]},
            {"t": "best phone under 20000 India 2026",         "k": ["phone 20000", "India"]},
            {"t": "best phone under 25000 India 2026",         "k": ["phone 25000", "India"]},
            {"t": "best phone under 30000 India 2026",         "k": ["phone 30000", "India"]},
            {"t": "best phone under 50000 India 2026",         "k": ["flagship phone", "India"]},
            {"t": "best 5G phone under 15000 India 2026",      "k": ["5G phone", "India"]},
            {"t": "best 5G phone under 20000 India 2026",      "k": ["5G phone 20000", "India"]},
            {"t": "Samsung Galaxy S26 vs iPhone 17 India",     "k": ["Samsung", "iPhone"]},
            {"t": "OnePlus 14 vs Samsung S26 India 2026",      "k": ["OnePlus", "Samsung"]},
            {"t": "Realme 14 Pro vs Redmi Note 14 Pro India",  "k": ["Realme", "Redmi"]},
            {"t": "Nothing Phone 3 vs OnePlus 14 India",       "k": ["Nothing Phone", "OnePlus"]},
            {"t": "best camera phone India 2026",              "k": ["camera phone", "India"]},
            {"t": "best battery life phone India 2026",        "k": ["battery phone", "India"]},
            {"t": "best gaming phone under 20000 India",       "k": ["gaming phone", "India"]},
            {"t": "best phone for students India 2026",        "k": ["student phone", "India"]},
            {"t": "best phone for photography India 2026",     "k": ["camera phone", "photography"]},
            {"t": "is iPhone 17 worth buying India 2026",      "k": ["iPhone 17", "India"]},
            {"t": "is Samsung S26 worth buying India 2026",    "k": ["Samsung S26", "India"]},
            {"t": "is OnePlus 14 worth buying India 2026",     "k": ["OnePlus 14", "India"]},
        ],
        "sections": [
            "1. Why This Smartphone Matters to Indian Buyers in 2026",
            "2. Design Build and First Impressions — materials colors dimensions weight feel",
            "3. Display Technology Explained Simply — panel resolution refresh rate brightness outdoor",
            "4. Camera System Complete Guide — every lens aperture features photography tips video",
            "5. Processor Performance and Gaming — chip speed gaming heat management multitasking",
            "6. Battery Life and Charging — real hours fast charge wireless reverse daily use",
            "7. Software and AI Features — Android version UI unique AI tools updates",
            "8. Connectivity and Extra Features — 5G WiFi Bluetooth NFC biometrics speakers IP",
            "9. India Price EMI and Where to Buy — variants Flipkart Amazon No Cost EMI deals",
            "10. Who Should Buy and Who Should Avoid — students gamers professionals photographers",
            "11. Top 3 Alternatives with India Prices — honest named comparison",
            "12. My Final Verdict and FAQ — clear recommendation + 7 questions Indians search",
        ]
    },

    "laptop": {
        "labels": ["Laptops", "Computers", "Tech News", "Price in India", "Review", "2026"],
        "detect": ["laptop", "macbook", "notebook", "ultrabook", "dell", "hp", "lenovo",
                   "asus", "acer", "microsoft surface", "msi", "razer", "lg gram",
                   "intel", "amd", "m4", "m3", "m2", "gaming laptop"],
        "news_topics": [
            "MacBook launch price India 2026",
            "Dell laptop launch India 2026",
            "HP laptop launch specifications 2026",
            "Lenovo laptop launch India 2026",
            "ASUS laptop launch India 2026",
            "gaming laptop launch India 2026",
            "Microsoft Surface launch 2026",
        ],
        "search_topics": [
            {"t": "best laptop under 30000 India 2026",        "k": ["laptop 30000", "India"]},
            {"t": "best laptop under 40000 India 2026",        "k": ["laptop 40000", "India"]},
            {"t": "best laptop under 50000 India 2026",        "k": ["laptop 50000", "India"]},
            {"t": "best laptop under 60000 India 2026",        "k": ["laptop 60000", "India"]},
            {"t": "best laptop for students India 2026",       "k": ["student laptop", "India"]},
            {"t": "best laptop for programming India 2026",    "k": ["programming laptop", "India"]},
            {"t": "best gaming laptop under 70000 India",      "k": ["gaming laptop", "India"]},
            {"t": "best gaming laptop under 80000 India",      "k": ["gaming laptop 80000", "India"]},
            {"t": "MacBook Air M4 vs Dell XPS India 2026",     "k": ["MacBook Air", "Dell XPS"]},
            {"t": "best thin light laptop India 2026",         "k": ["thin laptop", "portable"]},
            {"t": "best laptop for video editing India 2026",  "k": ["video editing laptop", "India"]},
            {"t": "is MacBook Air M4 worth buying India",      "k": ["MacBook Air M4", "India"]},
        ],
        "sections": [
            "1. Why This Laptop Deserves Your Attention in 2026",
            "2. Design Build Quality Ports and Keyboard — chassis hinge weight port selection typing",
            "3. Display Color Accuracy Brightness — panel resolution refresh rate outdoor use",
            "4. Processor Performance Real World Speed — chip generation daily tasks multitasking",
            "5. Graphics Gaming and Creative Work — GPU frame rates video editing rendering",
            "6. RAM Storage and Upgrade Options — configs SSD speed future upgrade path",
            "7. Battery Life for Different Use Cases — coding streaming gaming standby real hours",
            "8. Thermal Management Fan Noise Sustained Performance — cooling throttling noise",
            "9. India Price All Variants EMI — Flipkart Amazon student discounts bank offers",
            "10. Who Should Buy This Laptop — students developers creators gamers professionals",
            "11. Top 3 Alternatives with India Prices — honest comparison by use case",
            "12. My Final Verdict and FAQ — clear recommendation + 7 questions Indians search",
        ]
    },

    "earphones": {
        "labels": ["Earphones", "TWS", "Audio", "Tech News", "Price in India"],
        "detect": ["earphone", "earbuds", "tws", "in-ear", "wireless earphone",
                   "boat", "noise earbuds", "oneplus buds", "nothing ear",
                   "realme buds", "samsung buds", "oppo enco"],
        "news_topics": [
            "Boat earphones launch India 2026",
            "Noise earbuds launch India 2026",
            "OnePlus Buds launch India 2026",
            "Samsung Galaxy Buds launch 2026",
            "best TWS earbuds India 2026",
        ],
        "search_topics": [
            {"t": "best earphones under 500 India 2026",       "k": ["earphones 500", "India"]},
            {"t": "best earphones under 1000 India 2026",      "k": ["earphones 1000", "India"]},
            {"t": "best earphones under 2000 India 2026",      "k": ["earphones 2000", "India"]},
            {"t": "best TWS earbuds under 2000 India 2026",    "k": ["TWS earbuds", "India"]},
            {"t": "Boat vs Noise earphones India 2026",        "k": ["Boat", "Noise", "India"]},
        ],
        "sections": [
            "1. Why These Earphones Are Worth Talking About in India",
            "2. Design Comfort and Build Quality — form factor materials fit tip sizes",
            "3. Sound Quality Deep Dive — bass mids highs soundstage non-audiophile explanation",
            "4. Active Noise Cancellation Test — ANC strength transparency mode real environments",
            "5. Call Quality and Microphone — clarity noise rejection wind conference real test",
            "6. Battery Life and Charging Case — earbuds hours case charges total speed",
            "7. Bluetooth Connectivity and Latency — version multipoint gaming video lag codec",
            "8. Smart Features and App — EQ auto-pause voice assistant touch controls",
            "9. Comfort for Long Sessions — gym commute office all day experience",
            "10. India Price Variants and Value — colors EMI Flipkart Amazon best buy",
            "11. Who Should Buy and Who Should Not — music lovers commuters gym users",
            "12. Top 3 Alternatives My Final Verdict and FAQ — comparison + 7 questions",
        ]
    },

    "headphones": {
        "labels": ["Headphones", "Over Ear", "Audio", "Tech News", "Price in India"],
        "detect": ["headphones", "over ear", "on ear", "sony wh", "bose qc",
                   "sennheiser", "jbl tune", "boat rockerz", "anker soundcore"],
        "news_topics": [
            "Sony WH headphones launch India 2026",
            "Bose headphones launch India 2026",
            "best headphones India 2026",
        ],
        "search_topics": [
            {"t": "best headphones under 3000 India 2026",     "k": ["headphones 3000", "India"]},
            {"t": "best headphones under 5000 India 2026",     "k": ["headphones 5000", "India"]},
            {"t": "Sony WH-1000XM6 review India 2026",         "k": ["Sony WH", "India"]},
        ],
        "sections": [
            "1. Why These Headphones Are Getting Attention in India",
            "2. Design Build Comfort — padding clamp force foldability weight",
            "3. Sound Signature — bass mids highs soundstage non-audiophile explanation",
            "4. ANC vs Passive Isolation — real world environments performance",
            "5. Call Quality Microphone WFH — clarity noise rejection online meetings",
            "6. Battery Life and Charging — hours ANC on off quick charge wired backup",
            "7. Multipoint and Connectivity — two devices wired mode Bluetooth version",
            "8. Smart Controls and App — touch buttons EQ app voice assistant",
            "9. Portability and Travel — folding case airline adapter commute",
            "10. India Price Variants and Value — EMI Flipkart Amazon deals",
            "11. Who Should Buy — audiophiles WFH workers travellers students",
            "12. Top 3 Alternatives My Final Verdict and FAQ — comparison + 7 questions",
        ]
    },

    "airpods": {
        "labels": ["AirPods", "Apple Audio", "TWS", "iPhone Accessories", "Tech News"],
        "detect": ["airpods", "airpods pro", "airpods max", "apple earbuds", "apple audio"],
        "news_topics": [
            "AirPods launch specs India 2026",
            "AirPods Pro review India 2026",
        ],
        "search_topics": [
            {"t": "AirPods Pro 3 review India 2026",           "k": ["AirPods Pro", "India"]},
            {"t": "AirPods vs Samsung Galaxy Buds India",      "k": ["AirPods", "Galaxy Buds"]},
            {"t": "are AirPods worth buying India 2026",       "k": ["AirPods", "worth", "India"]},
        ],
        "sections": [
            "1. Are These AirPods Worth Buying in India in 2026",
            "2. Design Fit and Color Options — form factor comfort ear tip sizes",
            "3. Sound Quality and Apple Spatial Audio — real listening experience",
            "4. ANC and Transparency Mode — comparison with Sony Bose Samsung",
            "5. Apple Ecosystem Integration — iPhone iPad Mac seamless switching",
            "6. Call Quality and Siri — mic clarity wind noise India Siri accuracy",
            "7. Battery Life Case and Charging — hours MagSafe wireless quick charge",
            "8. H2 Chip Smart Features — adaptive audio conversation awareness",
            "9. Comfort for Indian Ears Long Sessions — gym commute daily wear",
            "10. India Price Is It Worth It — vs Noise Boat Sony OnePlus comparison",
            "11. Should You Buy AirPods or Android Alternative — honest India advice",
            "12. My Final Verdict and FAQ — buy or skip + 7 questions Indians ask",
        ]
    },

    "powerbank": {
        "labels": ["Power Bank", "Accessories", "Tech News", "Price in India"],
        "detect": ["power bank", "powerbank", "portable charger", "20000mah", "10000mah",
                   "anker", "mi powerbank", "realme powerbank", "boat powerbank", "ambrane"],
        "news_topics": [
            "best power bank India 2026",
            "fast charging power bank India 2026",
        ],
        "search_topics": [
            {"t": "best power bank under 1000 India 2026",     "k": ["power bank 1000", "India"]},
            {"t": "best 20000mAh power bank India 2026",       "k": ["20000mAh", "India"]},
            {"t": "Anker vs Mi power bank India 2026",         "k": ["Anker", "Mi power bank"]},
        ],
        "sections": [
            "1. Why You Actually Need This Power Bank in India",
            "2. Design Build and Portability — size weight pocket fit finish",
            "3. Capacity Real World Charging — mAh devices charged how many times",
            "4. Charging Speed Input Output — wattage PD QC protocols real test",
            "5. Number of Ports Cable Support — USB-A USB-C simultaneous charging",
            "6. Safety Features Temperature Control — overcharge protection auto cut",
            "7. Display and Indicators — LED dots percentage display status",
            "8. Device Compatibility — phone laptop tablet earbuds watch",
            "9. India Price Variants Best Buy — EMI Flipkart Amazon value variant",
            "10. Who Should Buy — travellers students professionals commuters",
            "11. Top 3 Alternatives with India Prices — Anker Mi Realme Boat compared",
            "12. My Final Verdict and FAQ — recommendation + 7 questions about power banks",
        ]
    },

    "smartwatch": {
        "labels": ["Smartwatch", "Wearables", "Fitness", "Tech News", "Price in India"],
        "detect": ["smartwatch", "smart watch", "wearable", "fitness band", "apple watch",
                   "galaxy watch", "garmin", "boat watch", "noise watch", "oneplus watch"],
        "news_topics": [
            "Apple Watch launch India 2026",
            "Samsung Galaxy Watch launch India 2026",
            "smartwatch launch India 2026",
            "fitness band launch India 2026",
        ],
        "search_topics": [
            {"t": "best smartwatch under 2000 India 2026",     "k": ["smartwatch 2000", "India"]},
            {"t": "best smartwatch under 5000 India 2026",     "k": ["smartwatch 5000", "India"]},
            {"t": "Apple Watch vs Samsung Galaxy Watch India",  "k": ["Apple Watch", "Samsung Watch"]},
            {"t": "best fitness band India 2026",              "k": ["fitness band", "India"]},
        ],
        "sections": [
            "1. Why This Smartwatch Is Getting Attention in India 2026",
            "2. Design Build Colors Strap Options — case material size weight",
            "3. Display Quality Always On Outdoor — type size brightness resolution",
            "4. Health Fitness Tracking Accuracy — heart rate SpO2 sleep stress ECG",
            "5. Smart Notifications Calls Daily Use — reply notifications quick actions",
            "6. Battery Life and Charging — days per charge AOD on off quick charge",
            "7. GPS Sports Tracking Accuracy — built-in GPS route auto detect sports",
            "8. App Ecosystem Compatibility — Android iPhone app quality third party",
            "9. Water Resistance and Durability — ATM rating swim shower dust",
            "10. India Price Variants and Value — sizes colors EMI Flipkart Amazon",
            "11. Who Should Buy — fitness lovers professionals casual users students",
            "12. Top 3 Alternatives My Final Verdict and FAQ — comparison + 7 questions",
        ]
    },
}

# ================================================================
# ROTATION SCHEDULE
# Day counter stored in posted_articles.json
# Phones/Laptops: every day
# Others: once every 3 weeks (21 days) rotation
# ================================================================
ROTATION_DAYS = {
    "earphones":  7,    # every 7 days
    "headphones": 14,   # every 14 days
    "airpods":    14,   # every 14 days
    "powerbank":  21,   # every 21 days
    "smartwatch": 10,   # every 10 days
}

import os, sys, json, time, random, requests, datetime, re
import smtplib
import xml.etree.ElementTree as ET
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
    from groq import Groq
except ImportError:
    print("Run: pip install groq")
    sys.exit(1)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
}

# ================================================================
# FETCH
# ================================================================
def fetch_rss(name, url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=8)
        if r.status_code != 200:
            return []
        root = ET.fromstring(r.content)
        items = root.findall(".//item")
        if not items:
            items = root.findall(".//{http://www.w3.org/2005/Atom}entry")
        out = []
        for item in items[:5]:
            t = item.find("title")
            title = t.text.strip() if t is not None and t.text else ""
            if len(title) < 20:
                continue
            d = item.find("description")
            if d is None:
                d = item.find("{http://www.w3.org/2005/Atom}summary")
            desc = ""
            if d is not None and d.text:
                desc = re.sub(r"<[^>]+>", "", d.text)[:500]
            l = item.find("link")
            link = l.text.strip() if l is not None and l.text else url
            out.append({"title": title, "description": desc,
                        "url": link, "source": name,
                        "published": datetime.datetime.now().isoformat()})
        return out[:2]
    except Exception:
        return []

def fetch_newsapi(query):
    try:
        r = requests.get("https://newsapi.org/v2/everything",
            params={"q": query, "language": "en", "sortBy": "publishedAt",
                    "pageSize": 5, "apiKey": NEWS_API_KEY}, timeout=10)
        data = r.json()
        if data.get("status") != "ok":
            return []
        return [{"title": a["title"], "description": a.get("description","") or "",
                 "url": a["url"], "source": a["source"]["name"],
                 "published": a["publishedAt"]}
                for a in data.get("articles", []) if a.get("title") and a.get("description")]
    except Exception:
        return []

def get_specs(device):
    try:
        q = device.replace(" ", "+")
        r = requests.get("https://www.gsmarena.com/search.php3?sQuickSearch=" + q,
                        headers=HEADERS, timeout=8)
        links = re.findall(r'href="([a-z0-9_]+-\d+\.php)"', r.text)
        if not links:
            return ""
        r2 = requests.get("https://www.gsmarena.com/" + links[0], headers=HEADERS, timeout=8)
        pairs = re.findall(
            r'<td class="ttl">.*?<a[^>]*>([^<]+)</a>.*?</td>\s*<td class="nfo">([^<]+)',
            r2.text, re.DOTALL)
        return "\n".join([k.strip() + ": " + v.strip() for k, v in pairs[:25]])
    except Exception:
        return ""

def detect_cat(title):
    tl = title.lower()
    for cat, data in CAT.items():
        if any(kw in tl for kw in data["detect"]):
            return cat
    return "smartphone"

def get_rss_context(keywords):
    ctx = []
    feeds = ALL_RSS[:]
    random.shuffle(feeds)
    for name, url in feeds[:15]:
        for a in fetch_rss(name, url):
            if any(kw.lower() in a["title"].lower() for kw in keywords):
                ctx.append("FROM " + a["source"] + ": " + a["title"] + " — " + a["description"][:150])
            if len(ctx) >= 6:
                break
        if len(ctx) >= 6:
            break
    return "\n".join(ctx[:6])

def load_log():
    if os.path.exists("posted_articles.json"):
        try:
            with open("posted_articles.json") as f:
                return json.load(f)
        except Exception:
            pass
    return []

def days_since_cat(log, cat):
    for entry in reversed(log):
        if entry.get("category") == cat:
            try:
                posted = datetime.datetime.fromisoformat(entry["posted_at"])
                delta  = datetime.datetime.now() - posted
                return delta.days
            except Exception:
                pass
    return 999

def should_post_cat(log, cat):
    if cat in ("smartphone", "laptop"):
        return True
    days_needed = ROTATION_DAYS.get(cat, 21)
    return days_since_cat(log, cat) >= days_needed

# ================================================================
# STORY PICKERS
# ================================================================
def pick_news_story(log):
    print("\n[News] Searching RSS feeds...")
    feeds = ALL_RSS[:]
    random.shuffle(feeds)

    used_titles = {e.get("title","") for e in log}

    # Prefer smartphone/laptop first
    priority = ["smartphone", "laptop"]
    for pcat in priority:
        data = CAT[pcat]
        random.shuffle(feeds)
        for name, url in feeds[:10]:
            arts = fetch_rss(name, url)
            for a in arts:
                if a["title"] not in used_titles:
                    if any(kw in a["title"].lower() for kw in data["detect"]):
                        a["specs"]    = get_specs(a["title"])
                        a["category"] = pcat
                        print("Found [" + pcat + "]: " + a["title"][:60])
                        return a

    # Fallback to any category that is due
    for cat, data in CAT.items():
        if not should_post_cat(log, cat):
            continue
        for topic in random.sample(data["news_topics"], min(3, len(data["news_topics"]))):
            arts = fetch_newsapi(topic)
            if arts and arts[0]["title"] not in used_titles:
                a = arts[0]
                a["specs"]    = get_specs(a["title"])
                a["category"] = cat
                print("Found [" + cat + "]: " + a["title"][:60])
                return a
    return None

def pick_search_story(log, used_in_run):
    print("\n[Search] Picking Google trending topic...")
    used_titles = {e.get("title","") for e in log} | used_in_run

    # Always prioritize smartphone and laptop search topics
    priority_cats = ["smartphone", "laptop"]
    all_options   = []
    for pcat in priority_cats:
        for t in CAT[pcat]["search_topics"]:
            if t["t"] not in used_titles:
                all_options.append((pcat, t))

    # Add other cats if due
    for cat, data in CAT.items():
        if cat in priority_cats:
            continue
        if not should_post_cat(log, cat):
            continue
        for t in data.get("search_topics", []):
            if t["t"] not in used_titles:
                all_options.append((cat, t))

    if not all_options:
        return None

    random.shuffle(all_options)
    chosen_cat, chosen_t = all_options[0]
    topic = chosen_t["t"]
    used_in_run.add(topic)
    print("Topic [" + chosen_cat + "]: " + topic)

    ctx  = get_rss_context(chosen_t["k"])
    arts = fetch_newsapi(topic)
    extra = arts[0].get("description","") if arts else ""

    return {"title": topic, "description": extra,
            "url": "https://technewswithai.blogspot.com",
            "source": "Tech News With AI Research",
            "published": datetime.datetime.now().isoformat(),
            "specs": "", "search_topic": topic,
            "keywords": chosen_t["k"], "rss_context": ctx,
            "category": chosen_cat}

def fix_bold(text):
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*",     r"<em>\1</em>",          text)
    text = re.sub(r"```html",       "",                       text)
    text = re.sub(r"```",           "",                       text)
    return text.strip()

# ================================================================
# STEP 1: GROQ TECHNICAL DRAFT
# ================================================================
def groq_draft(story, is_search):
    client   = Groq(api_key=GROQ_API_KEY)
    cat      = story.get("category", "smartphone")
    struct   = CAT.get(cat, CAT["smartphone"])
    sections = "\n".join(struct["sections"])

    if is_search:
        topic = story["search_topic"]
        ctx   = story.get("rss_context", "")
        if " vs " in topic.lower():
            mode = "HEAD TO HEAD COMPARISON — compare both side by side in every section."
        elif "under" in topic.lower() or "best" in topic.lower():
            mode = "BUYING GUIDE — list 5 real products with full specs India price pros cons each."
        else:
            mode = "EXPERT GUIDE — answer the search question completely and practically."
        prompt = (
            "Write comprehensive guide for Indians searching: " + topic + "\n\n"
            "REAL DATA FROM OFFICIAL SOURCES AND REVIEW SITES:\n"
            + (ctx or "Use your India market 2026 knowledge") + "\n\n"
            "ARTICLE TYPE: " + mode + "\n\n"
            "H1 TITLE: Use exact search keywords. Example:\n"
            "'Best Phone Under 20000 India 2026 — Top 7 Picks Ranked and Reviewed'\n\n"
            "WRITE 12 SECTIONS (4 paragraphs each 5 sentences each):\n" + sections + "\n\n"
            "RULES:\n"
            "- Minimum 3000 words\n"
            "- Exact search keywords in title headings paragraphs\n"
            "- Real India rupee prices Flipkart Amazon EMI\n"
            "- Real product names honest pros AND cons\n"
            "- h1 h2 h3 p tags only HTML — NEVER markdown\n"
            "- FAQ first question must be exact search query\n"
            "Write now:"
        )
    else:
        prompt = (
            "Write detailed technical article about: " + story["title"] + "\n"
            "CATEGORY: " + cat.upper() + "\n"
            "SOURCE: " + story["source"] + "\n"
            "REAL SPECS:\n" + (story.get("specs") or "Not available") + "\n"
            "DESCRIPTION: " + story.get("description", "") + "\n\n"
            "WRITE 12 SECTIONS (4 paragraphs each 5 sentences each):\n" + sections + "\n\n"
            "RULES:\n"
            "- Minimum 3000 words\n"
            "- Explain every tech term simply in brackets\n"
            "- Real India rupee prices\n"
            "- h1 h2 h3 p tags HTML only — NEVER markdown\n"
            "- Bold specs with <strong> tags\n"
            "Write now:"
        )
    r = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=6000, temperature=0.7,
    )
    return r.choices[0].message.content

# ================================================================
# STEP 2: HUMAN REWRITE — Fixes "Tool-generated no human value"
# ================================================================
def human_rewrite(draft, story):
    client = Groq(api_key=GROQ_API_KEY)
    cat    = story.get("category", "smartphone")
    today  = datetime.datetime.now().strftime("%B %d, %Y")
    labels = ", ".join(CAT.get(cat, CAT["smartphone"])["labels"])

    author_bio = (
        '<div style="border-top:3px solid #1a73e8;margin-top:40px;padding:20px;'
        'background:#f0f7ff;border-radius:12px;">'
        "<table><tr>"
        '<td style="width:85px;vertical-align:top;padding-right:15px;">'
        '<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-wLca38wMPYMxl6rUWuHdG4URpnvheiobu7pae1axqNvcUCX-wvsh3G_s25wiIefihtQ-hLmQxvnU6FsqEppxpOm03g4MBZ5XzX48sfkkcI4D83jPpkdgb9XoMZPCt1fsUyp5cf0nNTYHNQB20bKMAp3RMBWaZBH4D85YRrkXAm2afcE/s1600/0a737a69-7fa3-4dd5-a4b6-534dedca97be.jfif"'
        ' width="75" height="75" style="border-radius:50%;border:3px solid #1a73e8;" alt="Mallikarjun R"/>'
        "</td><td style='vertical-align:top;'>"
        '<p style="margin:0;font-size:18px;font-weight:bold;color:#1a73e8;">Mallikarjun R</p>'
        '<p style="margin:4px 0;font-size:13px;color:#666;">CSE Student &amp; Tech Blogger &bull; Bengaluru, India</p>'
        '<p style="margin:10px 0;font-size:14px;color:#333;line-height:1.7;">'
        "Passionate about smartphones, laptops and everything tech. "
        "Honest reviews for Indian buyers. Follow for daily updates!</p>"
        '<p style="margin:8px 0;">'
        '<a href="https://www.instagram.com/mallikarjunr_8055" target="_blank" style="color:#e4405f;margin-right:15px;font-weight:bold;">&#128247; Instagram</a>'
        '<a href="https://whatsapp.com/channel/0029VazWwdn0wajoizN5PY3Q" target="_blank" style="color:#25d366;margin-right:15px;font-weight:bold;">&#128172; WhatsApp</a>'
        '<a href="https://www.linkedin.com/in/mallikarjun-r-a85685367" target="_blank" style="color:#0077b5;font-weight:bold;">&#128188; LinkedIn</a>'
        "</p>"
        '<p style="font-size:12px;color:#999;"><em>Published: ' + today + ' &bull; technewswithai.blogspot.com</em></p>'
        "</td></tr></table></div>"
    )

    prompt = (
        "You are Mallikarjun R — real 19-year-old CSE student and tech blogger from Bengaluru India.\n"
        "Writing for category: " + cat.upper() + "\n\n"

        "PROBLEM TO FIX: This article is tool-generated with low explanation and zero human value.\n"
        "SOLUTION: Rewrite every single section to sound like YOU personally wrote it.\n\n"

        "FOR EVERY SECTION MUST DO ALL 5:\n"
        "1. PERSONAL OPENING — start with your own observation or experience\n"
        "   Phone: 'I have been testing phones in this range for months...'\n"
        "   Laptop: 'After a week of coding sessions and binge watching on this...'\n"
        "   Earphones: 'I wore these for my entire Bengaluru metro commute and noticed...'\n"
        "   Power bank: 'My phone died during an important exam call and that is why I tested this...'\n"
        "   Watch: 'I wore this for 2 weeks tracking my morning runs and here is what happened...'\n\n"
        "2. REAL INDIA EXPLANATION — explain WHY this matters for Indian daily life\n"
        "   NOT: '5000mAh battery'\n"
        "   YES: '5000mAh means you get through a full IPL match, 6 hours of college lectures,\n"
        "   and still have 30 percent charge for your evening Bengaluru commute home'\n\n"
        "3. HONEST REACTION — your genuine feeling\n"
        "   'This genuinely blew me away for the price'\n"
        "   'Honestly I was disappointed here — expected better'\n"
        "   'This is where it gets interesting'\n\n"
        "4. SPECIFIC INDIA ADVICE — practical buying tips\n"
        "   'Buy during Flipkart Big Billion Days for extra Rs 2000 off'\n"
        "   'The 8GB variant is worth Rs 1500 extra — trust me on this'\n"
        "   'Amazon generally has better exchange offers for this model'\n\n"
        "5. ONE LIKE + ONE DISLIKE — honest every section\n"
        "   'What I love: the AMOLED display is stunning at any brightness'\n"
        "   'What bothers me: the plastic back feels cheap for this price'\n\n"

        "WRITING STYLE:\n"
        "- First person always: I think, honestly, in my experience, trust me\n"
        "- Indian English: value for money, decent enough, quite good, not bad at all\n"
        "- Short punchy sentences mixed with long detailed ones\n"
        "- Natural connectors: look, here is the thing, and honestly, but wait, the catch is\n"
        "- Rhetorical questions: But does it hold up? Is it worth your hard earned money?\n"
        "- India scenarios: IPL cricket, college hostel WiFi, Bengaluru traffic, weddings, exams\n\n"

        "ADSENSE STRUCTURE RULES:\n"
        "- Strong hook in first 2 lines — must make reader want to continue\n"
        "- Add Table of Contents after introduction\n"
        "- Add this internal link somewhere: <a href='https://technewswithai.blogspot.com' "
        "target='_blank'>latest tech news on Tech News With AI</a>\n"
        "- External links to GSMArena and 91Mobiles where relevant\n"
        "- Suggested labels: " + labels + "\n"
        "- Every paragraph = new unique information — zero repetition\n"
        "- Minimum 3000 words\n\n"

        "ABSOLUTE NEVER:\n"
        "- NEVER **markdown** bold — ONLY <strong>HTML</strong> tags\n"
        "- NEVER say: In conclusion, To summarize, It is worth noting\n"
        "- NEVER write sentences that could apply to ANY product\n"
        "- NEVER start two consecutive paragraphs same way\n\n"

        "ADD AUTHOR BIO as the absolute last element:\n"
        + author_bio + "\n\n"

        "REWRITE EVERY WORD NOW — make it feel 100% human:\n\n"
        + draft
    )

    r = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=7000, temperature=0.88,
    )
    return r.choices[0].message.content

# ================================================================
# POST AND SAVE
# ================================================================
def post_email(title, html):
    print("Posting: " + title[:60])
    pw = os.environ.get("GMAIL_APP_PASSWORD", GMAIL_APP_PASSWORD)
    msg = MIMEMultipart("alternative")
    msg["Subject"] = title
    msg["From"]    = GMAIL_ADDRESS
    msg["To"]      = BLOGGER_POST_EMAIL
    msg.attach(MIMEText(html, "html"))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
        s.login(GMAIL_ADDRESS, pw)
        s.sendmail(GMAIL_ADDRESS, BLOGGER_POST_EMAIL, msg.as_string())
    print("Posted!")
    return "https://technewswithai.blogspot.com"

def save_log(log, title, url, words, atype, cat):
    log.append({"title": title, "url": url, "words": words,
                "type": atype, "category": cat,
                "posted_at": datetime.datetime.now().isoformat()})
    with open("posted_articles.json", "w") as f:
        json.dump(log, f, indent=2)
    print("Log: " + str(len(log)) + " total posts")

def run_article(story, is_search, label, atype, log):
    print("\n" + "="*55)
    print(label + " [" + story.get("category","?").upper() + "]")
    print("="*55)

    print("Step 1: Technical draft...")
    draft = groq_draft(story, is_search)
    w1    = len(re.sub(r"<[^>]+>","",draft).split())
    print("Draft: " + str(w1) + " words")

    print("Step 2: Human rewrite as Mallikarjun R...")
    human = human_rewrite(draft, story)
    final = fix_bold(human)

    title = story["title"]
    m = re.search(r"<h[12][^>]*>(.*?)</h[12]>", final, re.IGNORECASE|re.DOTALL)
    if m:
        title = re.sub(r"<[^>]+>","",m.group(1)).strip()

    words = len(re.sub(r"<[^>]+>","",final).split())
    print("Final: " + str(words) + " words | " + title[:55])

    footer = (
        "<hr/><p style='font-size:12px;color:#888;text-align:center;padding:10px;'>"
        "<em>Source: " + story["source"] +
        " | <a href='" + story["url"] + "' target='_blank' rel='noopener'>Original</a>"
        " | <a href='https://technewswithai.blogspot.com'>Tech News With AI</a></em></p>"
    )
    url = post_email(title, final + footer)
    save_log(log, title, url, words, atype, story.get("category","general"))
    return True

# ================================================================
# MAIN
# ================================================================
def main():
    print("================================================")
    print(" TECH NEWS WITH AI - AUTO BLOG v10.0 ADVANCED")
    print(" Daily: 1 News + 2 Search Topics")
    print(" Schedule: Phone/Laptop daily | Others rotated")
    print(" technewswithai.blogspot.com")
    print("================================================")

    log        = load_log()
    used_in_run = set()
    success    = 0

    # Article 1 — Latest News (phone/laptop priority)
    try:
        s1 = pick_news_story(log)
        if s1:
            run_article(s1, False, "ARTICLE 1: LATEST NEWS", "news", log)
            log = load_log()
            success += 1
            print("Waiting 30s...")
            time.sleep(30)
    except Exception as e:
        print("Article 1 failed: " + str(e))

    # Article 2 — Google Search Topic
    try:
        s2 = pick_search_story(log, used_in_run)
        if s2:
            run_article(s2, True, "ARTICLE 2: GOOGLE SEARCH", "search", log)
            log = load_log()
            success += 1
            print("Waiting 30s...")
            time.sleep(30)
    except Exception as e:
        print("Article 2 failed: " + str(e))

    # Article 3 — Google Search Topic (different category)
    try:
        s3 = pick_search_story(log, used_in_run)
        if s3:
            run_article(s3, True, "ARTICLE 3: GOOGLE SEARCH", "search", log)
            success += 1
    except Exception as e:
        print("Article 3 failed: " + str(e))

    print("\n================================================")
    print("DONE! " + str(success) + "/3 articles posted!")
    print("Visit: https://technewswithai.blogspot.com")
    print("================================================")

if __name__ == "__main__":
    main()
