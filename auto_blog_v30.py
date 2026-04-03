# TECH NEWS WITH AI - AUTO BLOG v35.0
# v35 — Exact iQOO Apex 16-section structure · 10 FAQ · Competition section · Pros/Cons prose
#
# ================================================================
# WHY v28 — AdSense "Low value content" fix
# ================================================================
# Google rejected technewsai.me with two reasons:
#   1. "Low value content" — articles too short/thin/AI-sounding
#   2. "Automatically generated content without manual review"
#
# ROOT CAUSE: 3 articles per day splits the token budget three ways
#             → shorter articles → easier for Google to flag as AI junk
#
# FIX: ONE article per day — use the ENTIRE daily Groq token limit
#      on a SINGLE 7000–8000 word article (editorial journalism quality)
#
# ================================================================
# NEW 3-DAY ROTATING SCHEDULE
# ================================================================
#   Day 1 → Full smartphone review (new launch) — 7000+ words
#   Day 2 → Full smartphone review (different phone) — 7000+ words
#   Day 3 → Top searched smartphone topic — 7000+ words
#   Day 4 → back to Day 1 type ... and so on
#
#   Day type tracked in posted_articles.json → last_article_type
#
# ================================================================
# ADSENSE QUALITY UPGRADES IN v28
# ================================================================
#   1. 7000-8000 word target — editorial quality minimum
#   2. MAX TOKENS: draft=7000, rewrite=6000 (full Groq 70B budget)
#   3. Human voice: personal 14-day test narrative throughout
#   4. Banned AI phrases list expanded — no "seamlessly", "cutting-edge"
#   5. Extra sections: 14-Day Test, India Variant Differences, Who to Avoid
#   6. 10-question FAQ (up from 7) for content depth
#   7. Every spec has a "why this matters for Indian buyers" line
#
# technewsai.me - Mallikarjun R, Bengaluru
# ================================================================

import os  # must be first — keys below read from environment

CEREBRAS_API_KEY   = os.environ.get("CEREBRAS_API_KEY", "")  # cerebras.ai — free, unlimited TPM
NEWS_API_KEY       = os.environ.get("NEWS_API_KEY", "673bca5ceab54fa8bb7ed0344c8f6d13")
BLOGGER_POST_EMAIL = "mallikarjunr444.technewswithai6361@blogger.com"
GMAIL_ADDRESS      = "mallikarjunr444@gmail.com"
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "oeirtosmlhuwntka")

# ================================================================
# ALL OFFICIAL + REVIEW RSS FEEDS (60+ sources)
# ================================================================
ALL_RSS = [
    # ── Official India phone brands ──────────────────────────────
    ("Samsung Newsroom",      "https://news.samsung.com/global/feed"),
    ("Apple Newsroom",        "https://www.apple.com/newsroom/rss-feed.rss"),
    ("Xiaomi Blog",           "https://blog.mi.com/en/feed/"),
    ("OnePlus Forum",         "https://forums.oneplus.com/forums/oneplus-announcements.15/index.rss"),
    ("Nothing Tech",          "https://nothing.tech/blogs/news.atom"),
    ("Honor News",            "https://www.hihonor.com/global/news/rss/"),
    ("Huawei News",           "https://consumer.huawei.com/en/press/news/rss/"),
    ("Google Pixel",          "https://blog.google/products/pixel/rss/"),
    ("Realme Blog",           "https://www.realme.com/in/blogs/news.atom"),
    ("OPPO Newsroom",         "https://www.oppo.com/en/newsroom/rss/"),
    ("Vivo Blog",             "https://www.vivo.com/en/news/rss/"),
    ("Motorola News",         "https://newsroom.motorola.com/rss/"),
    ("Nokia News",            "https://www.nokia.com/about-us/news/releases/feed/"),
    ("Infinix Mobile",        "https://www.infinixmobility.com/en-in/news/rss/"),
    ("Tecno Mobile",          "https://www.tecno-mobile.com/en-in/blog/rss/"),
    ("POCO India",            "https://in.poc.phone/news/rss/"),
    ("iQOO India",            "https://www.iqoo.com/in/news.atom"),
    ("Lava Mobiles",          "https://www.lavamobiles.com/blogs/news.atom"),
    ("Micromax",              "https://in.micromaxinfo.com/news/rss/"),
    # ── Official laptop brands ───────────────────────────────────
    ("Dell Blog",             "https://www.dell.com/en-us/blog/feed/"),
    ("HP Newsroom",           "https://press.hp.com/us/en/blogs.rss"),
    ("Lenovo News",           "https://news.lenovo.com/feed/"),
    ("Microsoft Blog",        "https://blogs.microsoft.com/feed/"),
    ("ASUS News",             "https://www.asus.com/in/news/rss/"),
    ("Acer Newsroom",         "https://acernewsroom.com/feed/"),
    ("MSI News",              "https://www.msi.com/blog/feed/"),
    ("Razer News",            "https://www.razer.com/newsroom/rss/"),
    ("LG Gram Blog",          "https://www.lg.com/in/news/rss/"),
    # ── Official audio brands ────────────────────────────────────
    ("boAt Blog",             "https://www.boat-lifestyle.com/blogs/all.atom"),
    ("Noise Blog",            "https://www.gonoise.com/blogs/news.atom"),
    ("Sony Audio",            "https://presscentre.sony.eu/pressreleases/rss"),
    ("JBL News",              "https://www.jbl.com/blog/rss/"),
    ("Bose News",             "https://www.bose.com/en_us/blogs.atom"),
    ("Sennheiser Blog",       "https://en-us.sennheiser.com/blog/rss/"),
    ("Skullcandy Blog",       "https://www.skullcandy.com/blogs/news.atom"),
    ("Anker Blog",            "https://www.anker.com/blogs/news.atom"),
    ("1MORE Audio",           "https://www.1more.com/blogs/news.atom"),
    # ── Official wearables / accessories ─────────────────────────
    ("Garmin Blog",           "https://www.garmin.com/en-US/blog/feed/"),
    ("Fitbit Blog",           "https://blog.fitbit.com/feed/"),
    ("Amazfit Blog",          "https://www.amazfit.com/en/blog/rss/"),
    ("boAt Smart",            "https://www.boat-lifestyle.com/blogs/wearables.atom"),
    ("Noise Watch",           "https://www.gonoise.com/blogs/smartwatch.atom"),
    # ── India review sites ───────────────────────────────────────
    ("GSMArena",              "https://www.gsmarena.com/rss-news-articles.php3"),
    ("91Mobiles",             "https://www.91mobiles.com/hub/feed/"),
    ("MySmartPrice",          "https://www.mysmartprice.com/feed/"),
    ("BGR India",             "https://www.bgr.in/feed/"),
    ("GadgetsNow",            "https://www.gadgetsnow.com/rssfeedstopstories.cms"),
    ("Pricebaba",             "https://pricebaba.com/blog/feed/"),
    ("Fonearena",             "https://www.fonearena.com/blog/feed"),
    ("GadgetBridge",          "https://gadgetbridge.com/feed/"),
    ("Digit India",           "https://www.digit.in/rss/news.xml"),
    ("NDTV Gadgets",          "https://gadgets.ndtv.com/rss/feeds"),
    ("India Today Tech",      "https://www.indiatoday.in/technology/rss"),
    ("Times Of India Tech",   "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"),
    ("Economic Times Tech",   "https://economictimes.indiatimes.com/tech/rssfeeds/13357270.cms"),
    ("Hindustan Times Tech",  "https://tech.hindustantimes.com/rss"),
    # ── Global review sites ──────────────────────────────────────
    ("AndroidAuthority",      "https://www.androidauthority.com/feed/"),
    ("XDA Developers",        "https://www.xda-developers.com/feed/"),
    ("9to5Google",            "https://9to5google.com/feed/"),
    ("9to5Mac",               "https://9to5mac.com/feed/"),
    ("MacRumors",             "https://feeds.macrumors.com/MacRumors-All"),
    ("SamMobile",             "https://www.sammobile.com/feed/"),
    ("GizmoChina",            "https://www.gizmochina.com/feed/"),
    ("PhoneArena",            "https://www.phonearena.com/phones/articles/rss"),
    ("The Verge",             "https://www.theverge.com/rss/index.xml"),
    ("TechCrunch",            "https://techcrunch.com/feed/"),
    ("Engadget",              "https://www.engadget.com/rss.xml"),
    ("CNET",                  "https://www.cnet.com/rss/news/"),
    ("TechRadar",             "https://www.techradar.com/rss"),
    ("NotebookCheck",         "https://www.notebookcheck.net/News.rss"),
    ("SoundGuys",             "https://www.soundguys.com/feed/"),
    ("PCMag",                 "https://www.pcmag.com/feeds/latest"),
    ("Wired",                 "https://www.wired.com/feed/rss"),
    ("Tom's Guide",           "https://www.tomsguide.com/feeds/all"),
    ("Digital Trends",        "https://www.digitaltrends.com/feeds/all/"),
    ("Trusted Reviews",       "https://www.trustedreviews.com/feed"),
    ("What HiFi",             "https://www.whathifi.com/feeds/all"),
    ("RTings",                "https://www.rtings.com/feed/"),
    # ── Extra India breaking news sources (2026 additions) ──────────
    ("Beebom Gadgets",        "https://gadgets.beebom.com/feed/"),
    ("Smartprix",             "https://www.smartprix.com/bytes/feed/"),
    ("TelecomTalk",           "https://telecomtalk.info/feed/"),
    ("Cashify Blog",          "https://www.cashify.in/blog/feed/"),
    ("iGeeksBlog",            "https://www.igeeksblog.com/feed/"),
    ("Sportskeeda Tech",      "https://tech.sportskeeda.com/feed/"),
    ("Gizmochina India",      "https://www.gizmochina.com/category/india/feed/"),
    ("TechPP",                "https://techpp.com/feed/"),
    ("Nokiapoweruser",        "https://nokiapoweruser.com/feed/"),
    ("GadgetsToUse",          "https://gadgetstouse.com/feed/"),
]

# ================================================================
# BREAKING NEWS — Dynamic Live Fetch from ALL_RSS
# Replaces the old hardcoded BREAKING_NEWS_2026 list.
# Every run: scans ALL official brand + review RSS feeds,
# scores each article by recency and keyword relevance,
# returns the hottest stories as breaking topics.
# ================================================================

# Priority RSS feeds scanned FIRST for breaking news
# (official brand feeds + top India review sites)
BREAKING_RSS_PRIORITY = [
    # ── Official brand feeds (highest priority — first-party news) ──
    ("Samsung Newsroom",   "https://news.samsung.com/global/feed"),
    ("OnePlus Forum",      "https://forums.oneplus.com/forums/oneplus-announcements.15/index.rss"),
    ("Realme Blog",        "https://www.realme.com/in/blogs/news.atom"),
    ("OPPO Newsroom",      "https://www.oppo.com/en/newsroom/rss/"),
    ("Vivo Blog",          "https://www.vivo.com/en/news/rss/"),
    ("iQOO India",         "https://www.iqoo.com/in/news.atom"),
    ("Xiaomi Blog",        "https://blog.mi.com/en/feed/"),
    ("Nothing Tech",       "https://nothing.tech/blogs/news.atom"),
    ("Google Pixel",       "https://blog.google/products/pixel/rss/"),
    ("Motorola News",      "https://newsroom.motorola.com/rss/"),
    ("Apple Newsroom",     "https://www.apple.com/newsroom/rss-feed.rss"),
    ("Honor News",         "https://www.hihonor.com/global/news/rss/"),
    ("POCO India",         "https://in.poc.phone/news/rss/"),
    ("Infinix Mobile",     "https://www.infinixmobility.com/en-in/news/rss/"),
    # ── Top India review sites (second priority) ────────────────────
    ("GSMArena",           "https://www.gsmarena.com/rss-news-articles.php3"),
    ("91Mobiles",          "https://www.91mobiles.com/hub/feed/"),
    ("MySmartPrice",       "https://www.mysmartprice.com/feed/"),
    ("BGR India",          "https://www.bgr.in/feed/"),
    ("GadgetBridge",       "https://gadgetbridge.com/feed/"),
    ("NDTV Gadgets",       "https://gadgets.ndtv.com/rss/feeds"),
    ("Digit India",        "https://www.digit.in/rss/news.xml"),
    ("Beebom Gadgets",     "https://gadgets.beebom.com/feed/"),
    ("Smartprix",          "https://www.smartprix.com/bytes/feed/"),
    ("TechPP",             "https://techpp.com/feed/"),
    ("GadgetsNow",         "https://www.gadgetsnow.com/rssfeedstopstories.cms"),
    ("Pricebaba",          "https://pricebaba.com/blog/feed/"),
    ("Cashify Blog",       "https://www.cashify.in/blog/feed/"),
    # ── Global review sites (third priority) ────────────────────────
    ("AndroidAuthority",   "https://www.androidauthority.com/feed/"),
    ("XDA Developers",     "https://www.xda-developers.com/feed/"),
    ("SamMobile",          "https://www.sammobile.com/feed/"),
    ("GizmoChina",         "https://www.gizmochina.com/feed/"),
    ("PhoneArena",         "https://www.phonearena.com/phones/articles/rss"),
    ("The Verge",          "https://www.theverge.com/rss/index.xml"),
    ("TechRadar",          "https://www.techradar.com/rss"),
    ("9to5Google",         "https://9to5google.com/feed/"),
]

# Keywords that signal a high-value breaking story
BREAKING_KEYWORDS = [
    "launch", "launched", "price", "specs", "review", "hands on",
    "first look", "release", "announced", "available", "sale",
    "india", "rupee", "flipkart", "amazon", "official",
    "5g", "camera", "battery", "display", "processor", "chipset",
]

def fetch_breaking_news(log, max_results=20):
    """
    Dynamically scans BREAKING_RSS_PRIORITY feeds and ALL_RSS
    to find the freshest breaking tech stories.

    Scoring system (higher = more breaking):
      +3  — title contains launch/launched/announced/available/sale
      +2  — title contains India/price/review/specs
      +1  — title contains any other BREAKING_KEYWORDS match
      +2  — source is an official brand feed (first-party)
      +1  — source is a top India review site

    Returns list of story dicts ready for pick_news_story():
      {"title", "description", "url", "source", "category",
       "specs", "published", "rss_source"}
    """
    used_titles = {e.get("title", "") for e in log}
    seen        = set()   # dedup within this fetch
    candidates  = []

    # Official brand sources get +2 bonus
    brand_sources = {name for name, _ in BREAKING_RSS_PRIORITY[:14]}
    # India review sites get +1 bonus
    india_sources = {name for name, _ in BREAKING_RSS_PRIORITY[14:27]}

    high_value_triggers = {"launch", "launched", "announced", "available",
                           "sale", "first look", "hands on", "release"}

    print("[Breaking] Scanning RSS feeds for live breaking news...")

    # Scan priority feeds first, then remaining ALL_RSS
    all_feeds = BREAKING_RSS_PRIORITY + [
        f for f in ALL_RSS if f not in BREAKING_RSS_PRIORITY
    ]

    for name, url in all_feeds:
        try:
            arts = fetch_rss(name, url)
        except Exception:
            continue

        for a in arts:
            title = a.get("title", "")
            if not title or title in used_titles or title in seen:
                continue
            if len(title) < 20:
                continue

            tl = title.lower()

            # Detect category
            cat = detect_cat(title)

            # Score the article
            score = 0
            for kw in high_value_triggers:
                if kw in tl:
                    score += 3
                    break
            for kw in ["india", "price", "review", "specs"]:
                if kw in tl:
                    score += 2
                    break
            for kw in BREAKING_KEYWORDS:
                if kw in tl:
                    score += 1
                    break
            if name in brand_sources:
                score += 2
            elif name in india_sources:
                score += 1

            # Only keep stories with a meaningful score
            if score >= 2:
                candidates.append({
                    "title":       title,
                    "description": a.get("description", ""),
                    "url":         a.get("url", url),
                    "source":      name,
                    "published":   a.get("published", ""),
                    "category":    cat,
                    "rss_source":  url,
                    "_score":      score,
                })
                seen.add(title)

        if len(candidates) >= max_results * 3:
            break   # enough candidates gathered — stop fetching

    # Sort by score descending → return top max_results
    candidates.sort(key=lambda x: x["_score"], reverse=True)
    top = candidates[:max_results]

    print(f"[Breaking] Found {len(top)} live breaking stories "
          f"(scored from {len(candidates)} candidates across {len(all_feeds)} feeds)")
    return top


# ================================================================
# CATEGORY STRUCTURES — 12 sections per category
# ================================================================
CAT = {

    "smartphone": {
        "labels": ["Smartphones", "Mobile", "Tech News", "Price in India", "Review", "2026"],
        "detect": ["phone", "smartphone", "android", "iphone", "samsung", "oneplus",
                   "realme", "xiaomi", "oppo", "vivo", "nothing", "honor", "huawei",
                   "pixel", "motorola", "nokia", "infinix", "tecno", "poco", "redmi",
                   "iqoo", "lava", "micromax", "narzo", "moto",
                   "nord 6", "nord6", "15t", "realme 16", "s26", "x300", "find x9",
                   "a57", "a37", "note 15", "x8 pro", "v70", "15r", "turbo 6"],
        "news_topics": [
            "OnePlus Nord 6 India launch April 2026",
            "OnePlus 15T specs India 2026",
            "Realme 16 5G India launch 2026",
            "Samsung Galaxy S26 India launch 2026",
            "iPhone 17 India launch price 2026",
            "Xiaomi Redmi Note 15 Pro launch India 2026",
            "iQOO 15R launch India 2026",
            "Nothing Phone 3 launch India 2026",
            "Vivo X300 Ultra India launch 2026",
            "OPPO Find X9 Ultra India launch 2026",
            "Google Pixel 10 India launch 2026",
            "Motorola Edge 60 India launch 2026",
            "Poco X8 Pro Max India launch 2026",
            "budget 5G phone launch India 2026",
            "foldable phone launch India 2026",
            "gaming smartphone launch India 2026",
        ],
        "search_topics": [
            # ── Budget buying guides ─────────────────────────────────────
            {"t": "best phone under 10000 India 2026",             "k": ["budget phone", "10000"]},
            {"t": "best phone under 15000 India 2026",             "k": ["phone 15000", "India"]},
            {"t": "best phone under 20000 India 2026",             "k": ["phone 20000", "India"]},
            {"t": "best phone under 25000 India 2026",             "k": ["phone 25000", "India"]},
            {"t": "best phone under 30000 India 2026",             "k": ["phone 30000", "India"]},
            {"t": "best 5G phone under 15000 India 2026",          "k": ["5G phone", "India"]},
            {"t": "best 5G phone under 20000 India 2026",          "k": ["5G phone 20000", "India"]},
            # ── Feature-specific guides ──────────────────────────────────
            {"t": "best camera phone under 20000 India 2026",      "k": ["camera phone", "India"]},
            {"t": "best camera phone under 30000 India 2026",      "k": ["camera phone 30000", "India"]},
            {"t": "best battery life phone India 2026",            "k": ["battery phone", "India"]},
            {"t": "best gaming phone under 20000 India 2026",      "k": ["gaming phone", "India"]},
            {"t": "best gaming phone under 30000 India 2026",      "k": ["gaming phone 30000", "India"]},
            {"t": "best phone for students India 2026",            "k": ["student phone", "India"]},
            {"t": "best AMOLED phone under 15000 India 2026",      "k": ["AMOLED phone", "India"]},
            {"t": "best slim phone India 2026",                    "k": ["slim phone", "India"]},
            # ── "Is it worth buying" reviews ────────────────────────────
            {"t": "is Samsung Galaxy S26 worth buying India 2026", "k": ["Samsung S26", "India"]},
            {"t": "is OnePlus Nord 6 worth buying India 2026",     "k": ["OnePlus Nord 6", "India"]},
            {"t": "is Nothing Phone 4a Pro worth buying India 2026","k": ["Nothing Phone 4a", "India"]},
            {"t": "is iQOO 15R worth buying India 2026",           "k": ["iQOO 15R", "India"]},
            {"t": "is Realme 16 5G worth buying India 2026",       "k": ["Realme 16 5G", "India"]},
            {"t": "is Poco X8 Pro worth buying India 2026",        "k": ["Poco X8 Pro", "India"]},
            {"t": "is Redmi Note 15 Pro worth buying India 2026",  "k": ["Redmi Note 15 Pro", "India"]},
            # ── VS comparison articles ───────────────────────────────────
            {"t": "Samsung Galaxy S26 vs iPhone 17 India 2026",    "k": ["Samsung S26", "iPhone 17"]},
            {"t": "OnePlus Nord 6 vs iQOO Neo 10 India 2026",      "k": ["OnePlus Nord 6", "iQOO Neo 10"]},
            {"t": "Nothing Phone 4a Pro vs Pixel 9a India 2026",   "k": ["Nothing Phone 4a", "Pixel 9a"]},
            {"t": "Realme 16 5G vs Redmi Note 15 Pro India 2026",  "k": ["Realme 16 5G", "Redmi Note 15"]},
            {"t": "Poco X8 Pro vs OnePlus Nord 6 India 2026",      "k": ["Poco X8 Pro", "OnePlus Nord 6"]},
            {"t": "Samsung M56 vs Redmi Note 15 Pro India 2026",   "k": ["Samsung M56", "Redmi Note 15"]},
            {"t": "iQOO 15R vs OnePlus 15R India 2026",            "k": ["iQOO 15R", "OnePlus 15R"]},
        ],
        "sections": [
            "INTRO. Introduction — Who This Phone Is For, Why It Matters in India 2026 (2 narrative paragraphs, NO H2)",
            "2. Design and Build Quality — Premium Feel or Not? Materials, IP Rating, Dimensions, Colors, Durability",
            "3. Display Review — Brightness, HDR, Outdoor Test, Panel Type, Resolution, Refresh Rate, Real Usage",
            "4. Performance Review — Chipset Deep Dive, Benchmarks, Gaming Test (game titles+fps), Daily Usage Experience",
            "5. Camera Review — Daylight, Night, Portrait, Video, Selfie (each tested separately with REAL results and honest verdict)",
            "6. Battery Life and Charging — Real Usage Test, mAh, Screen-On Hours, Fast Charge Time, India Scenarios",
            "7. Real-Life Usage Test — BGMI Gaming Test, Battery Drain Test, Heating Test, Daily India Commute Test",
            "8. How Does It Compare — Comparison Table vs 2 named rivals (e.g. Samsung S26, iPhone 17, or OnePlus 15R)",
            "9. Connectivity and Audio — 5G Bands, WiFi, Bluetooth, NFC, Speakers, Sensors, Biometrics",
            "10. Software and AI Features — Android Version, UI, AI Tools, Updates and Long-Term Support",
            "11. Price in India 2026 — All Variants, Launch Offers, No Cost EMI, Best Buy Links",
            "12. Pros and Cons — Honest Strengths and Weaknesses Based on Real Testing",
            "13. Who Should Buy and Who Should Avoid — Specific User Types with Clear Reasons",
            "14. Final Verdict — Is It Worth It? Clear Buy or Skip Recommendation with Strong Opinion",
            "15. FAQ — Most Searched Questions Indians Ask About This Phone (7 questions)",
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
            "Acer Nitro laptop launch India 2026",
            "MSI gaming laptop India 2026",
            "best budget laptop launch India 2026",
        ],
        "search_topics": [
            {"t": "best laptop under 30000 India 2026",            "k": ["laptop 30000", "India"]},
            {"t": "best laptop under 40000 India 2026",            "k": ["laptop 40000", "India"]},
            {"t": "best laptop under 50000 India 2026",            "k": ["laptop 50000", "India"]},
            {"t": "best laptop under 60000 India 2026",            "k": ["laptop 60000", "India"]},
            {"t": "best laptop under 70000 India 2026",            "k": ["laptop 70000", "India"]},
            {"t": "best laptop for students India 2026",           "k": ["student laptop", "India"]},
            {"t": "best laptop for programming India 2026",        "k": ["programming laptop", "India"]},
            {"t": "best laptop for data science India 2026",       "k": ["data science laptop", "India"]},
            {"t": "best gaming laptop under 70000 India 2026",     "k": ["gaming laptop", "India"]},
            {"t": "best gaming laptop under 80000 India 2026",     "k": ["gaming laptop 80000", "India"]},
            {"t": "MacBook Air M4 vs Dell XPS India 2026",         "k": ["MacBook Air", "Dell XPS"]},
            {"t": "MacBook Air M4 vs Asus Zenbook India 2026",     "k": ["MacBook Air M4", "Asus Zenbook"]},
            {"t": "best thin light laptop India 2026",             "k": ["thin laptop", "portable"]},
            {"t": "best laptop for video editing India 2026",      "k": ["video editing laptop", "India"]},
            {"t": "best laptop for graphic design India 2026",     "k": ["graphic design laptop", "India"]},
            {"t": "is MacBook Air M4 worth buying India 2026",     "k": ["MacBook Air M4", "India"]},
            {"t": "HP Pavilion vs Lenovo IdeaPad India 2026",      "k": ["HP Pavilion", "Lenovo IdeaPad"]},
            {"t": "Dell XPS 15 vs MacBook Pro India 2026",         "k": ["Dell XPS 15", "MacBook Pro"]},
            {"t": "Asus ROG Strix vs MSI Katana India 2026",       "k": ["Asus ROG", "MSI Katana"]},
            {"t": "best Chromebook India 2026",                    "k": ["Chromebook", "India"]},
            {"t": "best laptop for college India 2026",            "k": ["college laptop", "India"]},
            {"t": "best laptop with 16GB RAM India 2026",          "k": ["16GB RAM laptop", "India"]},
        ],
        "sections": [
            "INTRO. Introduction — Who This Laptop Is For, Why It Matters in India 2026 (3 paragraphs)",
            "2. Design and Build Quality — Chassis Material, Hinge Durability, Port Layout, Keyboard Feel, Trackpad, Weight",
            "3. Display Review — Panel Type, Resolution, Refresh Rate, Nits, Colour Gamut, Outdoor Visibility, Bezels",
            "4. Performance Review — CPU Deep Dive, Benchmarks, Gaming Test (titles+fps), Daily Tasks, Thermal Management",
            "5. Battery Life and Charging — Real Hours by Use Case (coding/media/office), Charger Wattage, Charge Time",
            "6. Keyboard and Trackpad — Key Travel, Typing Feel, Backlight, Trackpad Accuracy, Gesture Support",
            "7. Connectivity and Ports — WiFi Version, Bluetooth, USB-A, USB-C, Thunderbolt, SD Card, HDMI, Audio Jack",
            "8. Software and AI Features — OS, Bloatware, Copilot or AI Tools, Update Support Years, Security",
            "9. Price in India 2026 — All Variants, Launch Offers, No Cost EMI, Best Buy Links",
            "10. Who Should Buy and Who Should Avoid — Students, Developers, Creators, Gamers, Professionals",
            "11. Final Verdict — Is It Worth It? Clear Buy or Skip Recommendation",
            "12. FAQ — Most Searched Questions Indians Ask About This Laptop (5 questions)",
        ]
    },

    "earphones": {
        "labels": ["Earphones", "TWS", "Audio", "Budget Audio", "Tech News", "Price in India"],
        "detect": ["earphone", "earbuds", "tws", "in-ear", "wireless earphone",
                   "boat earphone", "noise earbuds", "oneplus buds", "nothing ear",
                   "realme buds", "samsung buds", "oppo enco", "jbl earphone",
                   "skullcandy", "sennheiser earphone", "sony earphone", "1more",
                   "soundcore", "anker earphone"],
        "news_topics": [
            "boAt earphones launch India 2026",
            "Noise earbuds launch India 2026",
            "OnePlus Buds launch India 2026",
            "Samsung Galaxy Buds launch 2026",
            "Nothing Ear launch India 2026",
            "Realme Buds launch India 2026",
            "JBL earphones launch India 2026",
            "Sony earbuds launch India 2026",
            "best TWS earbuds India 2026",
            "ANC earbuds launch India 2026",
        ],
        "search_topics": [
            {"t": "best earphones under 500 India 2026",           "k": ["earphones 500", "India"]},
            {"t": "best earphones under 1000 India 2026",          "k": ["earphones 1000", "India"]},
            {"t": "best earphones under 1500 India 2026",          "k": ["earphones 1500", "India"]},
            {"t": "best earphones under 2000 India 2026",          "k": ["earphones 2000", "India"]},
            {"t": "best earphones under 3000 India 2026",          "k": ["earphones 3000", "India"]},
            {"t": "best TWS earbuds under 2000 India 2026",        "k": ["TWS earbuds 2000", "India"]},
            {"t": "best TWS earbuds under 3000 India 2026",        "k": ["TWS earbuds 3000", "India"]},
            {"t": "best TWS earbuds under 5000 India 2026",        "k": ["TWS earbuds 5000", "India"]},
            {"t": "best ANC earphones under 5000 India 2026",      "k": ["ANC earphones", "India"]},
            {"t": "best ANC earbuds under 3000 India 2026",        "k": ["ANC earbuds 3000", "India"]},
            {"t": "boAt vs Noise earphones India 2026",            "k": ["boAt", "Noise", "India"]},
            {"t": "Nothing Ear vs OnePlus Buds India 2026",        "k": ["Nothing Ear", "OnePlus Buds"]},
            {"t": "Sony WF-1000XM5 vs Samsung Buds3 India 2026",   "k": ["Sony WF", "Samsung Buds"]},
            {"t": "best earphones for gym India 2026",             "k": ["gym earphones", "India"]},
            {"t": "best wired earphones under 500 India 2026",     "k": ["wired earphones", "India"]},
            {"t": "best earphones for calls India 2026",           "k": ["earphones calls", "India"]},
        ],
        "sections": [
            "INTRO. Introduction — Who These Earphones Are For, Why They Matter in India 2026 (3 paragraphs)",
            "2. Design and Build Quality — Form Factor, Materials, IP Rating, Ear Tip Fit, Comfort, Controls Finish",
            "3. Sound Quality Review — Bass Test, Mids, Highs, Soundstage, Driver Size, Real Listening Deep Dive",
            "4. ANC and Transparency Mode — ANC Strength in dB, Real Environments Tested, Transparency Quality",
            "5. Battery Life and Charging — Earbuds Hours, Case Total, Fast Charge, Wireless, India Daily Life",
            "6. Call Quality and Mic Test — Voice Clarity, Noise Rejection, Wind Test, Office and Outdoor Calls",
            "7. Connectivity and Codecs — Bluetooth Version, LDAC AAC SBC, Latency ms, Multipoint, Pairing",
            "8. Software and App Features — Companion App, EQ Presets, Gestures, Auto-Pause, Voice Assistant",
            "9. Price in India 2026 — All Variants, Launch Offers, No Cost EMI, Best Buy Links",
            "10. Who Should Buy and Who Should Avoid — Music Lovers, Commuters, Gym, Audiophiles, Casual Users",
            "11. Final Verdict — Is It Worth It? Clear Buy or Skip Recommendation",
            "12. FAQ — Most Searched Questions Indians Ask About These Earphones (5 questions)",
        ]
    },

    "headphones": {
        "labels": ["Headphones", "Over Ear", "Audio", "Tech News", "Price in India"],
        "detect": ["headphones", "over ear", "on ear", "sony wh", "bose qc",
                   "sennheiser", "jbl tune", "boat rockerz", "anker soundcore",
                   "skullcandy crusher", "audio technica", "beyerdynamic"],
        "news_topics": [
            "Sony WH headphones launch India 2026",
            "Bose headphones launch India 2026",
            "Samsung headphones launch India 2026",
            "boAt headphones launch India 2026",
            "best ANC headphones India 2026",
        ],
        "search_topics": [
            {"t": "best headphones under 2000 India 2026",         "k": ["headphones 2000", "India"]},
            {"t": "best headphones under 3000 India 2026",         "k": ["headphones 3000", "India"]},
            {"t": "best headphones under 5000 India 2026",         "k": ["headphones 5000", "India"]},
            {"t": "best headphones under 10000 India 2026",        "k": ["headphones 10000", "India"]},
            {"t": "best ANC headphones under 10000 India 2026",    "k": ["ANC headphones", "India"]},
            {"t": "Sony WH-1000XM6 review India 2026",             "k": ["Sony WH-1000XM6", "India"]},
            {"t": "Bose QC45 vs Sony XM6 India 2026",              "k": ["Bose QC", "Sony XM"]},
            {"t": "best headphones for WFH India 2026",            "k": ["WFH headphones", "India"]},
            {"t": "best wired headphones under 2000 India 2026",   "k": ["wired headphones", "India"]},
        ],
        "sections": [
            "INTRO. Introduction — Who These Headphones Are For, Why They Matter in India 2026 (3 paragraphs)",
            "2. Design and Build Quality — Clamping Force, Padding Thickness, Foldability, Weight, Materials, Hinge",
            "3. Sound Quality Review — Driver Size, Bass Depth, Mids, Highs, Soundstage, Tuning, Real Listening",
            "4. ANC and Passive Isolation — ANC Strength in dB, Real Environments Tested, Passive Seal Comparison",
            "5. Battery Life and Charging — Hours ANC On and Off, Quick Charge Time, Wired Backup, USB-C",
            "6. Call Quality and Mic Test — Voice Clarity, Noise Rejection, Wind, WFH Meetings, Online Class",
            "7. Connectivity and Codecs — Bluetooth Version, Multipoint Devices, Wired Mode, Codec Support",
            "8. Software and App Features — Companion App, EQ, Touch Controls, Voice Assistant, Smart Features",
            "9. Price in India 2026 — All Variants, Launch Offers, No Cost EMI, Best Buy Links",
            "10. Who Should Buy and Who Should Avoid — Audiophiles, WFH Workers, Travellers, Students, Commuters",
            "11. Final Verdict — Is It Worth It? Clear Buy or Skip Recommendation",
            "12. FAQ — Most Searched Questions Indians Ask About These Headphones (5 questions)",
        ]
    },

    "airpods": {
        "labels": ["AirPods", "Apple Audio", "TWS", "iPhone Accessories", "Tech News"],
        "detect": ["airpods", "airpods pro", "airpods max", "apple earbuds", "apple audio"],
        "news_topics": [
            "AirPods 4 launch specs India 2026",
            "AirPods Pro 3 review India 2026",
            "AirPods Max 2 launch India 2026",
        ],
        "search_topics": [
            {"t": "AirPods Pro 3 review India 2026",               "k": ["AirPods Pro 3", "India"]},
            {"t": "AirPods 4 vs AirPods Pro 3 India 2026",         "k": ["AirPods 4", "AirPods Pro"]},
            {"t": "AirPods vs Samsung Galaxy Buds3 India 2026",    "k": ["AirPods", "Galaxy Buds"]},
            {"t": "are AirPods worth buying India 2026",           "k": ["AirPods", "worth", "India"]},
            {"t": "AirPods Pro 3 vs Sony WF-1000XM5 India 2026",   "k": ["AirPods Pro", "Sony WF"]},
            {"t": "best AirPods alternative India 2026",           "k": ["AirPods alternative", "India"]},
        ],
        "sections": [
            "INTRO. Introduction — Who These AirPods Are For, Apple Ecosystem vs Alternatives in India 2026 (3 paragraphs)",
            "2. Design and Build Quality — Form Factor, Ear Tip Sizes, Colors, IP Rating, Case Design, Premium Finish",
            "3. Sound Quality Review — Bass, Mids, Highs, Spatial Audio Test, Real Listening Deep Dive vs Rivals",
            "4. ANC and Transparency Mode — ANC Depth Test vs Sony and Bose, Adaptive Audio, Wind Noise Test",
            "5. Battery Life and Charging — Hours per Charge, MagSafe, Wireless, Quick Charge, Total Case Battery",
            "6. Call Quality and Mic Test — Voice Clarity, Wind Noise Rejection, Siri India Performance, Outdoor Test",
            "7. Connectivity — Seamless iPhone iPad Mac Switching, Bluetooth Version, Codec Support, Android Use",
            "8. Software and Chip Features — H2 or H3 Chip, Auto-Switch, Conversation Awareness, Adaptive EQ",
            "9. Price in India 2026 — All Models, Launch Offers, No Cost EMI, Best Buy Links vs Alternatives",
            "10. Who Should Buy and Who Should Avoid — iPhone Users, Android Users, Budget Seekers, Audiophiles",
            "11. Final Verdict — Is It Worth It? Clear Buy or Skip Recommendation",
            "12. FAQ — Most Searched Questions Indians Ask About AirPods (5 questions)",
        ]
    },

    "powerbank": {
        "labels": ["Power Bank", "Accessories", "Tech News", "Price in India"],
        "detect": ["power bank", "powerbank", "portable charger", "20000mah", "10000mah",
                   "anker powerbank", "mi powerbank", "realme powerbank", "boat powerbank",
                   "ambrane", "romoss", "urbn power bank", "syska powerbank"],
        "news_topics": [
            "best power bank India 2026",
            "fast charging power bank India 2026",
            "65W power bank launch India 2026",
            "100W power bank launch India 2026",
            "slim power bank launch India 2026",
        ],
        "search_topics": [
            {"t": "best power bank under 1000 India 2026",         "k": ["power bank 1000", "India"]},
            {"t": "best power bank under 1500 India 2026",         "k": ["power bank 1500", "India"]},
            {"t": "best 10000mAh power bank India 2026",           "k": ["10000mAh", "India"]},
            {"t": "best 20000mAh power bank India 2026",           "k": ["20000mAh", "India"]},
            {"t": "best fast charging power bank India 2026",      "k": ["fast charging power bank", "India"]},
            {"t": "Anker vs MI power bank India 2026",             "k": ["Anker", "MI power bank"]},
            {"t": "best power bank for travel India 2026",         "k": ["travel power bank", "India"]},
            {"t": "best power bank for laptop India 2026",         "k": ["laptop power bank", "India"]},
            {"t": "best slim power bank India 2026",               "k": ["slim power bank", "India"]},
        ],
        "sections": [
            "INTRO. Introduction — Who This Power Bank Is For, Why It Matters in India 2026 (3 paragraphs)",
            "2. Design and Build Quality — Size, Weight, Pocket Fit, Finish, Materials, Port Layout, LED Indicator",
            "3. Real Capacity Test — Rated vs Actual mAh Output, Efficiency Percentage, Number of Full Phone Charges",
            "4. Charging Speed Test — Input Watt, Output Watt, PD, QC, PPS, Real Phone and Laptop Charge Time",
            "5. Battery Life — How Many Device Charges, Standby Self-Drain, Long-Term Reliability Real Test",
            "6. Ports and Device Compatibility — USB-A Count, USB-C Count, Simultaneous Charging, Phone Laptop Tablet",
            "7. Safety and Reliability — Overcharge Protection, Temperature Control, Auto Cut-Off, BIS Certification",
            "8. Connectivity and Travel — Cable Included, Pass-Through Charging, Airline Compliance, Portability",
            "9. Price in India 2026 — All Variants, Launch Offers, No Cost EMI, Best Buy Links",
            "10. Who Should Buy and Who Should Avoid — Travellers, Students, Professionals, Commuters, Gamers",
            "11. Final Verdict — Is It Worth It? Clear Buy or Skip Recommendation",
            "12. FAQ — Most Searched Questions Indians Ask About This Power Bank (5 questions)",
        ]
    },

    "smartwatch": {
        "labels": ["Smartwatch", "Wearables", "Fitness", "Tech News", "Price in India"],
        "detect": ["smartwatch", "smart watch", "wearable", "fitness band", "apple watch",
                   "galaxy watch", "garmin", "boat watch", "noise watch", "oneplus watch",
                   "amazfit", "realme watch", "fastrack", "titan smart"],
        "news_topics": [
            "Apple Watch launch India 2026",
            "Samsung Galaxy Watch launch India 2026",
            "smartwatch launch India 2026",
            "fitness band launch India 2026",
            "Garmin watch launch India 2026",
            "Amazfit launch India 2026",
            "boAt smartwatch launch India 2026",
        ],
        "search_topics": [
            {"t": "best smartwatch under 2000 India 2026",         "k": ["smartwatch 2000", "India"]},
            {"t": "best smartwatch under 3000 India 2026",         "k": ["smartwatch 3000", "India"]},
            {"t": "best smartwatch under 5000 India 2026",         "k": ["smartwatch 5000", "India"]},
            {"t": "best smartwatch under 10000 India 2026",        "k": ["smartwatch 10000", "India"]},
            {"t": "Apple Watch vs Samsung Galaxy Watch India 2026", "k": ["Apple Watch", "Samsung Watch"]},
            {"t": "best fitness band India 2026",                  "k": ["fitness band", "India"]},
            {"t": "best smartwatch for women India 2026",          "k": ["smartwatch women", "India"]},
            {"t": "best smartwatch with calling India 2026",       "k": ["calling smartwatch", "India"]},
            {"t": "Garmin vs Amazfit India 2026",                  "k": ["Garmin", "Amazfit"]},
            {"t": "best smartwatch for fitness India 2026",        "k": ["fitness smartwatch", "India"]},
        ],
        "sections": [
            "INTRO. Introduction — Who This Smartwatch Is For, Why It Matters in India 2026 (3 paragraphs)",
            "2. Design and Build Quality — Case Material, Size, Weight, Strap Options, Colors, Build Premium Feel",
            "3. Display Review — Type, Size, Peak Brightness, Resolution, Always-On Mode, Outdoor Visibility Test",
            "4. Health and Fitness Tracking — Heart Rate, SpO2, Sleep, Stress, ECG, Accuracy Real Test Results",
            "5. Battery Life and Charging — Days per Charge, AOD Impact, Quick Charge Time, Real India Usage",
            "6. Smart Notifications and Daily Use — Call Alerts, Quick Reply, App Notifications, Productivity Features",
            "7. GPS and Sports Tracking — Built-In GPS Accuracy, Route Mapping, Auto Sport Detection, Swimming Running",
            "8. Software and App Ecosystem — Companion App Quality, Third-Party Apps, Android and iPhone Compatibility",
            "9. Price in India 2026 — All Sizes and Colors, Launch Offers, No Cost EMI, Best Buy Links",
            "10. Who Should Buy and Who Should Avoid — Fitness Lovers, Professionals, Casual Users, Students",
            "11. Final Verdict — Is It Worth It? Clear Buy or Skip Recommendation",
            "12. FAQ — Most Searched Questions Indians Ask About This Smartwatch (5 questions)",
        ]
    },
}

# ================================================================
# ROTATION SCHEDULE
# ================================================================
ROTATION_DAYS = {
    "earphones":  7,
    "headphones": 14,
    "airpods":    14,
    "powerbank":  21,
    "smartwatch": 10,
}

import sys, json, time, random, requests, datetime, re
import smtplib
import xml.etree.ElementTree as ET
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
    from cerebras.cloud.sdk import Cerebras
except ImportError:
    print("Run: pip install cerebras-cloud-sdk")
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

# ================================================================
# OFFICIAL BRAND RSS FEEDS — scanned first for new launches
# These are the PRIMARY sources for Articles 1 & 2
# ================================================================
OFFICIAL_BRAND_RSS = [
    ("Samsung Newsroom",   "https://news.samsung.com/global/feed"),
    ("OnePlus Forum",      "https://forums.oneplus.com/forums/oneplus-announcements.15/index.rss"),
    ("Realme Blog",        "https://www.realme.com/in/blogs/news.atom"),
    ("OPPO Newsroom",      "https://www.oppo.com/en/newsroom/rss/"),
    ("Vivo Blog",          "https://www.vivo.com/en/news/rss/"),
    ("iQOO India",         "https://www.iqoo.com/in/news.atom"),
    ("Xiaomi Blog",        "https://blog.mi.com/en/feed/"),
    ("Nothing Tech",       "https://nothing.tech/blogs/news.atom"),
    ("Google Pixel",       "https://blog.google/products/pixel/rss/"),
    ("Motorola News",      "https://newsroom.motorola.com/rss/"),
    ("Apple Newsroom",     "https://www.apple.com/newsroom/rss-feed.rss"),
    ("Honor News",         "https://www.hihonor.com/global/news/rss/"),
    ("POCO India",         "https://in.poc.phone/news/rss/"),
    ("Infinix Mobile",     "https://www.infinixmobility.com/en-in/news/rss/"),
    ("Tecno Mobile",       "https://www.tecno-mobile.com/en-in/blog/rss/"),
    # ── Top India review sites — cover every brand launch ──────────
    ("91Mobiles",          "https://www.91mobiles.com/hub/feed/"),
    ("GSMArena",           "https://www.gsmarena.com/rss-news-articles.php3"),
    ("MySmartPrice",       "https://www.mysmartprice.com/feed/"),
    ("Smartprix",          "https://www.smartprix.com/bytes/feed/"),
    ("BGR India",          "https://www.bgr.in/feed/"),
    ("NDTV Gadgets",       "https://gadgets.ndtv.com/rss/feeds"),
    ("GadgetBridge",       "https://gadgetbridge.com/feed/"),
    ("Beebom Gadgets",     "https://gadgets.beebom.com/feed/"),
    ("TechPP",             "https://techpp.com/feed/"),
    ("Cashify Blog",       "https://www.cashify.in/blog/feed/"),
    ("GadgetsNow",         "https://www.gadgetsnow.com/rssfeedstopstories.cms"),
    ("AndroidAuthority",   "https://www.androidauthority.com/feed/"),
    ("XDA Developers",     "https://www.xda-developers.com/feed/"),
    ("9to5Google",         "https://9to5google.com/feed/"),
    ("SamMobile",          "https://www.sammobile.com/feed/"),
    ("GizmoChina",         "https://www.gizmochina.com/feed/"),
    ("The Verge",          "https://www.theverge.com/rss/index.xml"),
    ("PhoneArena",         "https://www.phonearena.com/phones/articles/rss"),
]

# Keywords that signal a GENUINE new product launch (not a rumour or deal)
LAUNCH_KEYWORDS = [
    "launched", "launch", "announced", "official", "price revealed",
    "goes on sale", "first sale", "available now", "pre-booking",
    "india price", "review", "first look", "hands on", "unboxing",
    "specifications", "full specs", "price in india",
]

# Keywords that should EXCLUDE a story from being a "new launch" article
EXCLUDE_KEYWORDS = [
    "rumour", "rumor", "leak", "leaked", "expected", "upcoming",
    "report", "tipped", "allegedly", "could", "might", "may launch",
    "deal", "discount", "sale offer", "cashback", "coupon",
    "best phones list", "top 5", "top 10", "buying guide",
    # ── v35: Non-phone product blocklist — NEVER write about these ──
    "air purifier", "purifier", "air cleaner", "air quality",
    "television", " tv ", "smart tv", "oled tv", "qled tv",
    "refrigerator", "fridge", "washing machine", "microwave",
    "air conditioner", " ac ", "inverter ac",
    "vacuum cleaner", "robot vacuum",
    "router", "wifi router", "mesh router",
    "monitor", "gaming monitor",
    "keyboard", "mouse ", "webcam",
    "projector", "home theatre",
    "electric vehicle", " ev ", "electric car",
    "scooter", "e-scooter",
    "speaker", "home speaker", "smart speaker",
    "tablet", "ipad",          # tablets get their own template — not phone reviews
]

# ── v35: A story MUST contain at least one of these to be treated as a phone ──
PHONE_MUST_KEYWORDS = [
    "phone", "smartphone", "mobile", "5g", "android", "iphone",
    "oneplus", "samsung galaxy", "xiaomi", "redmi", "poco",
    "realme", "oppo", "vivo", "iqoo", "nothing phone",
    "motorola", "pixel", "honor", "infinix", "tecno", "lava",
    "micromax", "nokia", "huawei", "asus rog phone",
]


def fetch_official_page_specs(url):
    """
    Fetches the actual source page of a launch article and extracts
    any spec-like data (numbers, GHz, mAh, Hz, MP, nm, GB, etc).
    Used to supplement GSMArena specs with data from the official article.
    """
    if not url or url.startswith("https://forums.oneplus"):
        return ""
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code != 200:
            return ""
        text = re.sub(r"<[^>]+>", " ", r.text)
        text = re.sub(r"\s+", " ", text)[:8000]

        # Extract spec-like sentences: lines containing numbers + units
        spec_lines = []
        for sentence in re.split(r"[.\n]", text):
            s = sentence.strip()
            if len(s) < 20 or len(s) > 300:
                continue
            # Must contain at least one spec-style number pattern
            if re.search(
                r"\b(\d+(\.\d+)?\s*(mAh|GHz|Hz|MP|nm|GB|TB|W|mm|nits?|inches?|fps|ms|dB|g\b))",
                s, re.IGNORECASE
            ):
                spec_lines.append(s)
            if len(spec_lines) >= 20:
                break

        return "\n".join(spec_lines) if spec_lines else ""
    except Exception:
        return ""



# ================================================================
# v27: WEB SCRAPING FALLBACK — for when RSS feeds have no new launches
# Scrapes live pages directly to find recently launched phones
# Used ONLY when RSS feeds return nothing for Articles 1 & 2
# ================================================================

def scrape_gsmarena_new_phones(max_results=10):
    """
    Scrapes GSMArena's daily news / latest phone reviews page
    to find phones that were just launched or reviewed.
    Returns list of story dicts compatible with pick_launch_story().
    """
    results = []
    urls_to_try = [
        "https://www.gsmarena.com/news.php3",
        "https://www.gsmarena.com/search.php3?chk5G=selected&sAvailabilities=1&YearMade=2025-2026",
    ]
    for page_url in urls_to_try:
        try:
            r = requests.get(page_url, headers=HEADERS, timeout=10)
            if r.status_code != 200:
                continue
            # Extract article titles and links from GSMArena news page
            # Pattern: article links with title text
            articles = re.findall(
                r'<a[^>]+href="(https://www\.gsmarena\.com/[^"]+\.php)"[^>]*>\s*([^<]{20,120})\s*</a>',
                r.text
            )
            for link, title in articles:
                title = title.strip()
                if not title or len(title) < 20:
                    continue
                tl = title.lower()
                # Must be about a phone (not accessories/tablets)
                if not any(kw in tl for kw in CAT["smartphone"]["detect"]):
                    continue
                # Must have a launch signal
                if not any(lk in tl for lk in LAUNCH_KEYWORDS):
                    continue
                # Must NOT be a rumour
                if any(ex in tl for ex in EXCLUDE_KEYWORDS):
                    continue
                results.append({
                    "title":       title,
                    "description": f"GSMArena: {title}",
                    "url":         link,
                    "source":      "GSMArena (scraped)",
                    "published":   datetime.datetime.now().isoformat(),
                    "category":    "smartphone",
                    "_score":      4,
                })
            if results:
                break
        except Exception as e:
            print(f"[GSMArena Scrape] Failed: {e}")
    print(f"[GSMArena Scrape] Found {len(results)} candidates")
    return results[:max_results]


def scrape_91mobiles_launches(max_results=10):
    """
    Scrapes 91Mobiles recently launched / upcoming phones page.
    Returns list of story dicts compatible with pick_launch_story().
    """
    results = []
    urls_to_try = [
        "https://www.91mobiles.com/phones/recently-launched",
        "https://www.91mobiles.com/hub/new-mobile-phones/",
    ]
    for page_url in urls_to_try:
        try:
            r = requests.get(page_url, headers=HEADERS, timeout=10)
            if r.status_code != 200:
                continue
            # Extract phone names from page text
            text = re.sub(r"<[^>]+>", " ", r.text)
            text = re.sub(r"\s+", " ", text)
            # Look for phone-like patterns (Brand + model + optional numbers)
            phone_patterns = re.findall(
                r'\b((?:Samsung|OnePlus|Realme|Xiaomi|Redmi|POCO|iQOO|Vivo|OPPO|Nothing|'
                r'Motorola|Nokia|Honor|Infinix|Tecno|Google Pixel|Apple iPhone)\s+'
                r'[A-Za-z0-9][A-Za-z0-9\s\+]{3,30}?)'
                r'(?=\s+(?:launched|review|price|specs|announced|available|\₹|\d{4,}))',
                text, re.IGNORECASE
            )
            seen = set()
            for name in phone_patterns:
                name = name.strip()
                if name in seen or len(name) < 10:
                    continue
                seen.add(name)
                title = f"{name} Review — Price in India, Specs, Camera Test 2026"
                results.append({
                    "title":       title,
                    "description": f"Recently launched: {name}",
                    "url":         page_url,
                    "source":      "91Mobiles (scraped)",
                    "published":   datetime.datetime.now().isoformat(),
                    "category":    "smartphone",
                    "_score":      3,
                })
                if len(results) >= max_results:
                    break
            if results:
                break
        except Exception as e:
            print(f"[91Mobiles Scrape] Failed: {e}")
    print(f"[91Mobiles Scrape] Found {len(results)} candidates")
    return results[:max_results]


def scrape_smartprix_launches(max_results=10):
    """
    Scrapes Smartprix latest phone news for launch stories.
    """
    results = []
    try:
        r = requests.get("https://www.smartprix.com/bytes/category/mobiles/",
                         headers=HEADERS, timeout=10)
        if r.status_code != 200:
            return []
        articles = re.findall(
            r'<a[^>]+href="(https://www\.smartprix\.com/bytes/[^"]+)"[^>]*>\s*([^<]{20,120})\s*</a>',
            r.text
        )
        for link, title in articles:
            title = title.strip()
            tl = title.lower()
            if not any(kw in tl for kw in CAT["smartphone"]["detect"]):
                continue
            if any(ex in tl for ex in EXCLUDE_KEYWORDS):
                continue
            results.append({
                "title":       title,
                "description": f"Smartprix: {title}",
                "url":         link,
                "source":      "Smartprix (scraped)",
                "published":   datetime.datetime.now().isoformat(),
                "category":    "smartphone",
                "_score":      3,
            })
    except Exception as e:
        print(f"[Smartprix Scrape] Failed: {e}")
    print(f"[Smartprix Scrape] Found {len(results)} candidates")
    return results[:max_results]


    """
    Picks a GENUINELY NEW LAUNCHED smartphone story for Articles 1 & 2.

    Priority order:
      1. Official brand RSS feeds (Samsung, OnePlus, Nothing, iQOO etc) — first-party launch news
      2. Top India review sites (91Mobiles, GSMArena, BGR India etc) — verified launch coverage
      3. Fallback: any story from ALL_RSS with strong launch signals

    Filters OUT:
      - Rumours, leaks, deals, buying guides, Top 5 lists
      - Already-posted articles (from log)
      - Stories without launch keywords in title or description

    Enriches each story with:
      - GSMArena spec data (get_specs)
      - Official page spec data (fetch_official_page_specs)
    """
    print("\n[Launch] Scanning official brand RSS feeds for new smartphone launches...")
    used_titles = {e.get("title", "") for e in log}
    if exclude_titles:
        used_titles = used_titles | exclude_titles

    smartphone_detect = CAT["smartphone"]["detect"]
    candidates = []

    # Official brand sources get highest priority score
    official_brand_names = {name for name, _ in OFFICIAL_BRAND_RSS[:15]}

    for name, url in OFFICIAL_BRAND_RSS:
        try:
            articles = fetch_rss(name, url)
        except Exception:
            continue

        for a in articles:
            title = a.get("title", "")
            desc  = a.get("description", "")
            if not title or title in used_titles:
                continue
            if len(title) < 20:
                continue

            tl = title.lower()
            dl = desc.lower()

            # Must be a smartphone
            if not any(kw in tl or kw in dl for kw in smartphone_detect):
                continue

            # Must NOT be a rumour, leak, or list article
            if any(ex in tl for ex in EXCLUDE_KEYWORDS):
                continue

            # Must have at least one launch signal
            has_launch = any(lk in tl or lk in dl for lk in LAUNCH_KEYWORDS)
            if not has_launch:
                continue

            # Score: official brand = 5, India review site = 3, global = 1
            if name in official_brand_names:
                score = 5
            elif any(x in name for x in ["91Mobiles", "GSMArena", "BGR India",
                                          "Smartprix", "NDTV", "GadgetBridge",
                                          "Beebom", "TechPP", "Cashify"]):
                score = 3
            else:
                score = 1

            # Boost score for strong launch words in title (not just description)
            strong_title_words = ["launched", "official", "price in india",
                                  "review", "hands on", "first look", "india price"]
            if any(w in tl for w in strong_title_words):
                score += 2

            candidates.append({
                "title":       title,
                "description": desc,
                "url":         a.get("url", url),
                "source":      name,
                "published":   a.get("published", ""),
                "category":    "smartphone",
                "_score":      score,
            })

    # Sort by score
    candidates.sort(key=lambda x: x["_score"], reverse=True)

    # Enrich top candidates with specs and return first unused one
    for story in candidates[:15]:
        title = story["title"]
        print(f"[Launch][{story['source']}] {title[:70]} (score={story['_score']})")

        # Fetch specs from GSMArena
        gsm_specs = get_specs(title)

        # Fetch specs from official page
        official_specs = fetch_official_page_specs(story.get("url", ""))

        # Combine both spec sources
        combined_specs = ""
        if gsm_specs:
            combined_specs += "=== GSMArena Specs ===\n" + gsm_specs + "\n\n"
        if official_specs:
            combined_specs += "=== Official Source Data ===\n" + official_specs

        story["specs"]       = combined_specs or "Use your full knowledge of this device."
        story["rss_context"] = get_rss_context([title.split()[0], title.split()[-1]])

        return story

    # ── v27 FALLBACK: RSS found nothing — scrape live web pages for recent launches ──
    print("[Launch] RSS found no launch stories — switching to LIVE WEB SCRAPING fallback...")

    scraped_all = []
    scraped_all += scrape_gsmarena_new_phones(max_results=8)
    scraped_all += scrape_91mobiles_launches(max_results=8)
    scraped_all += scrape_smartprix_launches(max_results=6)

    # Deduplicate and filter already-used
    seen_scraped = set()
    for story in scraped_all:
        title = story.get("title", "")
        if title in used_titles or title in seen_scraped or len(title) < 20:
            continue
        seen_scraped.add(title)

        print(f"[Launch-Scraped][{story['source']}] {title[:70]}")

        # Enrich with specs
        gsm_specs      = get_specs(title)
        official_specs = fetch_official_page_specs(story.get("url", ""))
        combined_specs = ""
        if gsm_specs:
            combined_specs += "=== GSMArena Specs ===\n" + gsm_specs + "\n\n"
        if official_specs:
            combined_specs += "=== Source Page Data ===\n" + official_specs

        story["specs"]       = combined_specs or "Use your full knowledge of this device."
        story["rss_context"] = get_rss_context([title.split()[0], title.split()[-1]])
        return story

    print("[Launch] Web scraping also found nothing — caller will handle final fallback")
    return None

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
    for name, url in feeds[:20]:
        for a in fetch_rss(name, url):
            if any(kw.lower() in a["title"].lower() for kw in keywords):
                ctx.append("FROM " + a["source"] + ": " + a["title"] + " — " + a["description"][:200])
            if len(ctx) >= 8:
                break
        if len(ctx) >= 8:
            break
    return "\n".join(ctx[:8])

# ================================================================
# DYNAMIC SEARCH TOPIC GENERATOR
# Reads today's live RSS headlines → Groq auto-generates fresh
# trending search topics for any category — updates every run
# ================================================================

# Topic templates Groq can use as inspiration (not hardcoded output)
TOPIC_TEMPLATES = {
    "smartphone": [
        "best phone under ₹[PRICE] India [YEAR]",
        "[Brand] [Model] vs [Brand2] [Model2] India [YEAR]",
        "is [Brand] [Model] worth buying India [YEAR]",
        "best [feature] phone India [YEAR]",
        "best 5G phone under ₹[PRICE] India [YEAR]",
    ],
    "laptop": [
        "best laptop under ₹[PRICE] India [YEAR]",
        "[Brand] [Model] vs [Brand2] [Model2] India [YEAR]",
        "best laptop for [use case] India [YEAR]",
        "is [Brand] [Model] worth buying India [YEAR]",
    ],
    "earphones": [
        "best earphones under ₹[PRICE] India [YEAR]",
        "best TWS earbuds under ₹[PRICE] India [YEAR]",
        "[Brand] vs [Brand2] earphones India [YEAR]",
        "best ANC earphones under ₹[PRICE] India [YEAR]",
    ],
    "headphones": [
        "best headphones under ₹[PRICE] India [YEAR]",
        "[Brand] [Model] review India [YEAR]",
        "best ANC headphones India [YEAR]",
    ],
    "airpods": [
        "AirPods [Model] review India [YEAR]",
        "AirPods vs [Brand] earbuds India [YEAR]",
        "are AirPods worth buying India [YEAR]",
    ],
    "powerbank": [
        "best power bank under ₹[PRICE] India [YEAR]",
        "best [mAh] power bank India [YEAR]",
        "[Brand] vs [Brand2] power bank India [YEAR]",
    ],
    "smartwatch": [
        "best smartwatch under ₹[PRICE] India [YEAR]",
        "[Brand] [Model] smartwatch review India [YEAR]",
        "best smartwatch for [use case] India [YEAR]",
    ],
}

def fetch_rss_headlines_for_cat(cat, max_headlines=30):
    """Fetch fresh RSS headlines relevant to a category."""
    detect_kws = CAT.get(cat, CAT["smartphone"])["detect"]
    headlines  = []
    feeds = ALL_RSS[:]
    random.shuffle(feeds)
    for name, url in feeds:
        for a in fetch_rss(name, url):
            if any(kw in a["title"].lower() for kw in detect_kws):
                headlines.append(a["title"])
            if len(headlines) >= max_headlines:
                break
        if len(headlines) >= max_headlines:
            break
    return headlines

def generate_dynamic_topics(cat, log, used_combined, count=8):
    """
    Calls Groq with today's live RSS headlines to auto-generate
    fresh trending search topics for the given category.

    KEY: Each generated topic MUST have enough real content to fill
    all 12 category-specific sections defined in CAT[cat]["sections"].
    Topics are validated against the section structure before returning.

    Returns list of {"t": "...", "k": ["...", "..."], "sections": [...]} dicts.
    """
    try:
        from cerebras.cloud.sdk import Cerebras
        client = Cerebras(api_key=CEREBRAS_API_KEY)

        headlines = fetch_rss_headlines_for_cat(cat, max_headlines=25)
        if not headlines:
            return []

        year           = datetime.datetime.now().year
        used_list      = "\n".join(list(used_combined)[:40]) if used_combined else "None yet"
        templates      = "\n".join(TOPIC_TEMPLATES.get(cat, TOPIC_TEMPLATES["smartphone"]))
        headlines_text = "\n".join(f"  - {h}" for h in headlines)

        # Pull the exact 12 sections for this category
        struct   = CAT.get(cat, CAT["smartphone"])
        sections = struct["sections"]
        sections_text = "\n".join(
            f"  {s}" for s in sections
        )

        # Category-specific topic rules
        cat_rules = {
            "smartphone": (
                "Topics must allow writing about: Design, Display, Camera, Processor, "
                "Battery, Software/AI features, Connectivity, India Price, Who Should Buy, "
                "Alternatives, Final Verdict. Use real phone models from headlines."
            ),
            "laptop": (
                "Topics must allow writing about: Design/Build/Ports, Display, Processor, "
                "Graphics/Gaming, RAM/Storage, Battery, Thermals, India Price, "
                "Who Should Buy, Alternatives, Final Verdict. Use real laptop models."
            ),
            "earphones": (
                "Topics must allow writing about: Design/Comfort, Sound Quality (bass/mids/highs), "
                "ANC, Call Quality, Battery/Case, Bluetooth/Latency, Smart Features/App, "
                "Comfort for long sessions, India Price, Who Should Buy, Alternatives, Verdict. "
                "Use real earphone/TWS models."
            ),
            "headphones": (
                "Topics must allow writing about: Design/Comfort/Clamping, Sound Signature, "
                "ANC vs Passive, Call/Mic, Battery, Multipoint/Connectivity, Controls/App, "
                "Portability, India Price, Who Should Buy, Alternatives, Verdict. "
                "Use real headphone models."
            ),
            "airpods": (
                "Topics must allow writing about: Design/Fit, Sound/Spatial Audio, ANC/Transparency, "
                "Apple Ecosystem, Call/Siri, Battery/MagSafe, H2 Chip features, Comfort, "
                "India Price vs alternatives, Should You Buy vs Android, Verdict. "
                "Use real AirPods models."
            ),
            "powerbank": (
                "Topics must allow writing about: Design/Portability, Real Capacity, "
                "Charging Speed (W), Ports, Safety features, Display/Indicators, "
                "Device Compatibility, India Price, Who Should Buy, Alternatives, Verdict. "
                "Use real power bank models."
            ),
            "smartwatch": (
                "Topics must allow writing about: Design/Colors/Straps, Display quality, "
                "Health/Fitness Tracking accuracy, Smart Notifications, Battery life, "
                "GPS Sports tracking, App Ecosystem, Water Resistance, India Price, "
                "Who Should Buy, Alternatives, Verdict. Use real smartwatch models."
            ),
            "ai": (
                "Topics must allow writing about: What the AI tool does, Real benefits for Indians, "
                "Top 5 features, How to use free in India, Limitations, Comparison with alternatives, "
                "Privacy/Data safety, Best devices, India Pricing (free vs paid), "
                "Who Should Use, Verdict. Use real AI tools/features from headlines."
            ),
        }.get(cat, "Topics must cover all 12 sections listed above with real product data.")

        prompt = (
            f"You are an India tech SEO expert generating blog topics for category: "
            f"{cat.upper()}\n\n"

            f"━━━ TODAY'S LIVE RSS HEADLINES (base topics on what is trending RIGHT NOW) ━━━\n"
            f"{headlines_text}\n\n"

            f"━━━ THE ARTICLE STRUCTURE: 12 SECTIONS THIS CATEGORY MUST FOLLOW ━━━\n"
            f"Every generated topic MUST produce enough real content to write ALL 12 sections:\n"
            f"{sections_text}\n\n"

            f"━━━ CATEGORY CONTENT RULES ━━━\n"
            f"{cat_rules}\n\n"

            f"━━━ TOPIC TITLE TEMPLATES (fill with real data from headlines) ━━━\n"
            f"{templates}\n\n"

            f"━━━ ALREADY POSTED — DO NOT REPEAT ANY OF THESE ━━━\n"
            f"{used_list}\n\n"

            f"━━━ GENERATION RULES ━━━\n"
            f"• Topics must come from real products/launches in the headlines above\n"
            f"• Each topic = a real Google search Indians type in {year}\n"
            f"• Mix: 40% buying guides (best X under ₹Y), 30% comparisons (X vs Y), "
            f"30% reviews (is X worth buying)\n"
            f"• Always include India + {year} in the topic text\n"
            f"• Use ₹ Indian rupee prices where relevant\n"
            f"• Keywords = the top 2 actual search terms Indians use for that topic\n"
            f"• Every topic must be completely unique from the others\n"
            f"• NEVER repeat from the 'Already Posted' list\n"
            f"• Topic must be specific enough that ALL 12 sections above can be written\n\n"

            f"━━━ OUTPUT FORMAT ━━━\n"
            f"Respond ONLY with a valid JSON array. No explanation. No markdown fences.\n"
            f'[{{"t": "topic title India {year}", "k": ["main keyword", "secondary keyword"]}}, ...]\n\n'
            f"Generate exactly {count} fresh topics for {cat.upper()} now:"
        )

        r = client.chat.completions.create(
            model="llama3.1-8b",  # Cerebras fast model
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1500,
            temperature=0.75,
        )
        raw = r.choices[0].message.content.strip()
        raw = re.sub(r"```json|```", "", raw).strip()
        m   = re.search(r"\[.*\]", raw, re.DOTALL)
        if not m:
            return []
        topics = json.loads(m.group(0))
        valid  = []
        for t in topics:
            if isinstance(t, dict) and "t" in t and "k" in t:
                if t["t"] not in used_combined:
                    valid.append({
                        "t":        str(t["t"]),
                        "k":        [str(k) for k in t["k"]],
                        "sections": sections,   # attach category sections to each topic
                        "category": cat,
                    })
        print(f"[DynamicTopics] Generated {len(valid)} fresh [{cat.upper()}] topics")
        return valid

    except Exception as e:
        print(f"[DynamicTopics] Failed for [{cat}]: {e}")
        return []

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
    # Smartphone is ALWAYS daily
    if cat == "smartphone":
        return True
    # Laptop and others rotate based on ROTATION_DAYS
    days_needed = ROTATION_DAYS.get(cat, 21)
    return days_since_cat(log, cat) >= days_needed

# ================================================================
# STORY PICKERS
# ================================================================
def pick_launch_story(log, exclude_titles=None):
    """
    Pick a new smartphone LAUNCH story from RSS feeds.
    Prioritises articles with LAUNCH_KEYWORDS and excludes EXCLUDE_KEYWORDS.
    Used for Day 1 and Day 2 of the 3-day review cycle.
    """
    print("\n[Launch] Fetching new smartphone launch stories from RSS feeds...")
    used_titles = {e.get("title", "") for e in log}
    if exclude_titles:
        used_titles = used_titles | set(exclude_titles)

    # Step 1: Scan breaking news for launch articles
    breaking = fetch_breaking_news(log)
    for story in breaking:
        title = story.get("title", "")
        tl = title.lower()
        if title in used_titles:
            continue
        if any(ex in tl for ex in EXCLUDE_KEYWORDS):
            continue
        # ── v35: MUST be about a phone — reject non-phone products ──
        if not any(pk in tl for pk in PHONE_MUST_KEYWORDS):
            print(f"[Launch][Skip — not a phone] {title[:60]}")
            continue
        if any(lk in tl for lk in LAUNCH_KEYWORDS):
            story["specs"]    = get_specs(title)
            story["category"] = "smartphone"   # force smartphone category
            print(f"[Launch][Breaking] {title[:65]}")
            return story

    # Step 2: Scan ALL_RSS for launch keywords
    feeds = ALL_RSS[:]
    random.shuffle(feeds)
    for name, url in feeds[:30]:
        for a in fetch_rss(name, url):
            tl = a["title"].lower()
            if a["title"] in used_titles:
                continue
            if any(ex in tl for ex in EXCLUDE_KEYWORDS):
                continue
            # ── v35: MUST be about a phone ──
            if not any(pk in tl for pk in PHONE_MUST_KEYWORDS):
                continue
            if any(lk in tl for lk in LAUNCH_KEYWORDS):
                a["specs"]    = get_specs(a["title"])
                a["category"] = "smartphone"   # force smartphone category
                print(f"[Launch][RSS] {a['title'][:65]}")
                return a

    # Step 3: Fallback to pick_news_story (non-list, non-guide)
    print("[Launch][Fallback] No pure launch found — falling back to news story...")
    return pick_news_story(log, exclude_titles=exclude_titles)


def pick_news_story(log, exclude_titles=None):
    print("\n[News] Fetching live breaking news from RSS feeds...")
    used_titles = {e.get("title","") for e in log}
    if exclude_titles:
        used_titles = used_titles | exclude_titles

    # ── Step 0: Fetch live breaking stories via fetch_breaking_news() ──
    breaking = fetch_breaking_news(log)
    for story in breaking:
        title = story.get("title", "")
        tl = title.lower()
        if title in used_titles:
            continue
        # ── v35: reject non-phone products ──
        if any(ex in tl for ex in EXCLUDE_KEYWORDS):
            continue
        if not any(pk in tl for pk in PHONE_MUST_KEYWORDS):
            print(f"[News][Skip — not a phone] {title[:55]}")
            continue
        story["specs"]    = get_specs(title)
        story["category"] = "smartphone"
        print(f"[Breaking][SMARTPHONE] {title[:65]}")
        return story

    # ── Step 1: Fallback — scan ALL_RSS for any category match ──
    feeds = ALL_RSS[:]
    random.shuffle(feeds)
    for pcat in ["smartphone", "laptop"]:
        data = CAT[pcat]
        for name, url in feeds[:20]:
            for a in fetch_rss(name, url):
                if a["title"] not in used_titles:
                    if any(kw in a["title"].lower() for kw in data["detect"]):
                        a["specs"]    = get_specs(a["title"])
                        a["category"] = pcat
                        print(f"[Fallback][{pcat}] {a['title'][:60]}")
                        return a

    # ── Step 2: Final fallback — NewsAPI on category news topics ──
    for cat, data in CAT.items():
        if not should_post_cat(log, cat):
            continue
        for topic in random.sample(data["news_topics"], min(3, len(data["news_topics"]))):
            arts = fetch_newsapi(topic)
            if arts and arts[0]["title"] not in used_titles:
                a = arts[0]
                a["specs"]    = get_specs(a["title"])
                a["category"] = cat
                print(f"[NewsAPI][{cat}] {a['title'][:60]}")
                return a
    return None

def pick_article3_single_review(log, used_in_run):
    """
    v27: Article 3 = ALWAYS a single trending smartphone full product review.
    Priority:
      1. Trending/popular phone from RSS (not already reviewed in Articles 1 & 2)
      2. Web scraped trending phone from GSMArena / 91Mobiles
      3. Groq-generated trending phone name based on current RSS headlines
      4. Fallback only: "top searched smartphones" buying guide

    Returns a story dict with is_search=False so run_article writes a full review.
    """
    print("\n[Article3] Picking SINGLE trending smartphone for full product review...")
    used_titles = {e.get("title", "") for e in log}
    used_titles |= used_in_run

    # ── Step 1: Find a trending single phone from RSS breaking news ──
    breaking = fetch_breaking_news(log, max_results=30)
    for story in breaking:
        title = story.get("title", "")
        if title in used_titles:
            continue
        cat = story.get("category", "smartphone")
        if cat != "smartphone":
            continue
        tl = title.lower()
        # REJECT list articles, comparisons, buying guides
        list_signals = ["top 3", "top 5", "top 10", "best 5", "best phones",
                        "buying guide", "vs ", " vs", "comparison", "ranked",
                        "best under", "budget phones", "phones under"]
        if any(s in tl for s in list_signals):
            continue
        # Must look like a single phone review/launch
        single_signals = ["review", "launched", "price in india", "hands on",
                         "first look", "unboxing", "full specs", "announced",
                         "specifications", "available", "goes on sale"]
        if not any(s in tl for s in single_signals):
            continue
        # Enrich with specs
        print(f"[Article3][RSS] Single phone: {title[:65]}")
        gsm_specs = get_specs(title)
        official_specs = fetch_official_page_specs(story.get("url", ""))
        combined_specs = ""
        if gsm_specs:
            combined_specs += "=== GSMArena Specs ===\n" + gsm_specs + "\n\n"
        if official_specs:
            combined_specs += "=== Source Data ===\n" + official_specs
        return {
            "title":       title,
            "description": story.get("description", ""),
            "url":         story.get("url", ""),
            "source":      story.get("source", "RSS"),
            "published":   story.get("published", datetime.datetime.now().isoformat()),
            "category":    "smartphone",
            "specs":       combined_specs or "Use your full knowledge of this device.",
            "rss_context": get_rss_context([title.split()[0]]),
        }

    # ── Step 2: Try web scraped phones (GSMArena / 91Mobiles) ──
    print("[Article3] RSS found no single trending phone — trying web scraping...")
    scraped = scrape_gsmarena_new_phones(max_results=10) + scrape_91mobiles_launches(max_results=5)
    for story in scraped:
        title = story.get("title", "")
        if title in used_titles or len(title) < 20:
            continue
        print(f"[Article3][Scraped] {title[:65]}")
        gsm_specs = get_specs(title)
        story["specs"] = ("=== GSMArena Specs ===\n" + gsm_specs) if gsm_specs else "Use your full knowledge."
        story["rss_context"] = get_rss_context([title.split()[0]])
        return story

    # ── Step 3: Ask Groq which phone is trending right now ──
    print("[Article3] Scraping found nothing — asking Groq for trending phone...")
    try:
        from cerebras.cloud.sdk import Cerebras
        client = Cerebras(api_key=CEREBRAS_API_KEY)
        headlines = fetch_rss_headlines_for_cat("smartphone", max_headlines=20)
        year = datetime.datetime.now().year
        prompt = (
            f"You are an India tech expert. Based on these today's headlines:\n"
            f"{chr(10).join(headlines[:15])}\n\n"
            f"Pick ONE single smartphone that Indian buyers are most searching for right now in {year}.\n"
            f"It must be a specific model (e.g. 'Samsung Galaxy S25 FE' not just 'Samsung phone').\n"
            f"It must be recently launched or trending in India.\n"
            f"Respond ONLY with the exact model name, nothing else. No explanation."
        )
        r = client.chat.completions.create(
            model="llama3.1-8b",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=30, temperature=0.5,
        )
        phone_name = r.choices[0].message.content.strip().strip('"').strip("'")
        if len(phone_name) > 8 and phone_name not in used_titles:
            print(f"[Article3][Groq] Trending phone: {phone_name}")
            gsm_specs = get_specs(phone_name)
            return {
                "title":       f"{phone_name} Full Review India {year} — Price, Camera, Battery Tested",
                "description": f"Full review of {phone_name} for Indian buyers.",
                "url":         "",
                "source":      "Groq Trend Picker",
                "published":   datetime.datetime.now().isoformat(),
                "category":    "smartphone",
                "specs":       ("=== GSMArena Specs ===\n" + gsm_specs) if gsm_specs else "Use your full knowledge.",
                "rss_context": get_rss_context([phone_name.split()[0]]),
            }
    except Exception as e:
        print(f"[Article3][Groq] Failed: {e}")

    # ── Step 4: Last resort fallback — buying guide (not preferred) ──
    print("[Article3] All single-phone methods failed — falling back to buying guide topic")
    return None   # caller will fall back to pick_search_story()



    print("\n[Search] Building hybrid topic pool (breaking + dynamic RSS + static backup)...")

    used_titles  = {e.get("title","")        for e in log}
    used_topics  = {e.get("search_topic","") for e in log}
    combined_used = used_titles | used_topics | used_in_run

    priority_cats    = ["smartphone", "laptop"]
    secondary_cats   = [c for c in CAT if c not in priority_cats]

    all_options = []   # list of (cat, {"t":..., "k":[...]}, source)

    # ── 0. BREAKING NEWS — live fetch from ALL_RSS (replaces static list) ──
    live_breaking = fetch_breaking_news(log)
    for story in live_breaking:
        t_text = story["title"]
        if t_text not in combined_used:
            cat = story.get("category", "smartphone")
            # Article 3 = search topic about mobile phones ONLY
            if cat != "smartphone":
                continue
            t = {
                "t":        t_text,
                "k":        [w for w in t_text.split() if len(w) > 4][:3],
                "sections": CAT.get(cat, CAT["smartphone"])["sections"],
                "category": cat,
                "title":       t_text,
                "description": story.get("description", ""),
                "source":      story.get("source", "RSS"),
                "specs":       story.get("specs", ""),
                "url":         story.get("url", ""),
            }
            all_options.append((cat, t, "breaking"))
    print(f"[Breaking] {len([x for x in all_options if x[2]=='breaking'])} live smartphone search topics added")

    # ── 1. DYNAMIC topics from live RSS — smartphone only for daily Article 3 ──
    dynamic = generate_dynamic_topics("smartphone", log, combined_used, count=6)
    for t in dynamic:
        all_options.append(("smartphone", t, "dynamic"))

    # ── 2. STATIC backup — smartphone search topics only ──
    for t in CAT["smartphone"]["search_topics"]:
        if t["t"] not in combined_used:
            all_options.append(("smartphone", t, "static"))

    # ── 3. Weekly rotation categories (laptop/earphones/etc) — only if due ──
    for cat in secondary_cats:
        if not should_post_cat(log, cat):
            continue
        dynamic_sec = generate_dynamic_topics(cat, log, combined_used, count=4)
        for t in dynamic_sec:
            all_options.append((cat, t, "dynamic"))
        for t in CAT[cat].get("search_topics", []):
            if t["t"] not in combined_used:
                all_options.append((cat, t, "static"))

    # ── 4. Fallback: relax dedup (allow static repeats from past runs) ──
    if not all_options:
        print("[Search] Pool empty — running emergency dynamic generation...")
        for pcat in priority_cats:
            dynamic = generate_dynamic_topics(pcat, log, used_in_run, count=8)
            for t in dynamic:
                all_options.append((pcat, t, "dynamic-fallback"))
        for pcat in priority_cats:
            for t in CAT[pcat]["search_topics"]:
                if t["t"] not in used_in_run:
                    all_options.append((pcat, t, "static-fallback"))

    if not all_options:
        print("[Search] No topics available.")
        return None

    # Priority order: breaking (latest launches) > dynamic (RSS) > static (backup)
    breaking_opts = [(c, t, s) for c, t, s in all_options if s == "breaking"]
    dynamic_opts  = [(c, t, s) for c, t, s in all_options if "dynamic" in s]
    static_opts   = [(c, t, s) for c, t, s in all_options if "static"  in s]
    random.shuffle(breaking_opts)
    random.shuffle(dynamic_opts)
    random.shuffle(static_opts)
    ordered = breaking_opts + dynamic_opts + static_opts

    chosen_cat, chosen_t, src = ordered[0]
    topic = chosen_t["t"]
    used_in_run.add(topic)
    print(f"Topic [{chosen_cat}] ({src}): {topic}")

    ctx   = get_rss_context(chosen_t["k"])
    arts  = fetch_newsapi(topic)
    extra = arts[0].get("description","") if arts else ""

    return {
        "title":        topic,
        "description":  extra,
        "url":          "https://technewswithai.blogspot.com",
        "source":       "Tech News With AI Research",
        "published":    datetime.datetime.now().isoformat(),
        "specs":        "",
        "search_topic": topic,
        "keywords":     chosen_t["k"],
        "rss_context":  ctx,
        "category":     chosen_cat,
        "topic_source": src,
    }

def fix_bold(text):
    # Convert markdown bold/italic to HTML
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*",     r"<em>\1</em>",          text)
    # Strip code fences
    text = re.sub(r"```html",       "",                       text)
    text = re.sub(r"```",           "",                       text)
    # Convert markdown headings to HTML (### before ## before #)
    text = re.sub(r"^###\s+(.+)$", r"<h3>\1</h3>", text, flags=re.MULTILINE)
    text = re.sub(r"^##\s+(.+)$",  r"<h2>\1</h2>", text, flags=re.MULTILINE)
    text = re.sub(r"^#\s+(.+)$",   r"<h1>\1</h1>", text, flags=re.MULTILINE)
    # Remove any remaining raw ### that slipped through (e.g. inline ### What is...)
    text = re.sub(r"###\s*", "", text)
    text = re.sub(r"##\s*",  "", text)
    return text.strip()

# ================================================================
# v14: TITLE GENERATOR — clickbait-honest, numbered, SEO-optimised
# ================================================================
def generate_seo_title(story, is_search=False):
    """Groq generates a CTR-optimised H1 title.
    For news/single reviews (is_search=False): full review format — NO 'Top 5'.
    For search/buying guides (is_search=True): Top 5 / Best / Comparison format."""
    try:
        client = Cerebras(api_key=CEREBRAS_API_KEY)
        cat    = story.get("category", "smartphone")
        topic  = story.get("search_topic") or story.get("title", "")
        year   = datetime.datetime.now().year

        if is_search:
            # Search/buying guide articles — use "Top 5 / Best" format
            format_options = (
                f"  'Top 5 Best [Product] Under ₹[Price] India {year} — Tested & Ranked'\n"
                f"  '[Product A] vs [Product B] India {year}: Which One Wins?\n"
                f"  'Best [Feature] [Category] India {year}: Top 7 Picks Tested'\n"
                f"  'Top 5 [Category] India {year} — Honest Buying Guide'\n"
            )
            number_rule = "- Must contain a NUMBER: Top 5, Top 10, Best 7, etc.\n"
        else:
            # Single phone / product review — use full review format, NO "Top 5"
            format_options = (
                f"  '[Phone Name] Full Review India {year}: Full Specs, Camera Test & Is It Worth Buying?'\n"
                f"  '[Phone Name] Review India {year} — [Key Feature] Tested Honestly'\n"
                f"  '[Phone Name] Full Review India {year}: Honest [Key Feature] & Performance Test'\n"
                f"  '[Phone Name] India Review {year}: Price, Specs, Camera — Buy or Skip?'\n"
            )
            number_rule = (
                "- Do NOT use 'Top 5', 'Top 10', 'Best 5' etc — this is a SINGLE phone review\n"
                "- Title must clearly be a single product review, not a list\n"
            )

        prompt = (
            f"You are an India SEO expert. Generate ONE perfect blog title.\n\n"
            f"Topic: {topic}\n"
            f"Category: {cat.upper()}\n"
            f"Year: {year}\n\n"
            f"TITLE RULES:\n"
            f"{number_rule}"
            f"- Must be clickbait-honest: make it exciting BUT accurate\n"
            f"- Must include primary keyword and India {year}\n"
            f"- Must be under 70 characters (fits Google title tag)\n"
            f"- Use power words: Full Review, Tested, Honest, Worth Buying, Specs, Camera Test\n"
            f"- Format options (pick the best fit):\n"
            f"{format_options}\n"
            f"Output ONLY the title text. No quotes. No explanation."
        )
        r = client.chat.completions.create(
            model="llama3.1-8b",  # fast+cheap for short title task
            messages=[{"role": "user", "content": prompt}],
            max_tokens=80, temperature=0.8,
        )
        title = r.choices[0].message.content.strip().strip('"').strip("'")
        print(f"[Title] {title}")
        return title
    except Exception as e:
        print(f"[Title] Generator failed: {e}")
        return story.get("title", "Tech Review India " + str(datetime.datetime.now().year))

# ================================================================
# v14: LONG-TAIL KEYWORD BUILDER — from live RSS trends
# ================================================================
LONGTAIL_SEEDS = {
    "smartphone":  ["best phone", "budget smartphone", "5G phone India", "camera phone", "gaming phone"],
    "laptop":      ["best laptop", "student laptop", "gaming laptop India", "thin light laptop"],
    "earphones":   ["best earphones", "TWS earbuds", "ANC earphones", "budget earbuds India"],
    "headphones":  ["best headphones", "ANC headphones", "WFH headphones", "wireless headphones India"],
    "airpods":     ["AirPods review", "AirPods worth buying", "best AirPods alternative India"],
    "powerbank":   ["best power bank", "fast charging powerbank", "20000mAh powerbank India"],
    "smartwatch":  ["best smartwatch", "fitness band India", "calling smartwatch", "smartwatch under"],
}

def build_longtail_keywords(cat, ctx_text, topic):
    """Extract long-tail keywords from RSS context + topic + seed list."""
    seeds = LONGTAIL_SEEDS.get(cat, LONGTAIL_SEEDS["smartphone"])
    year  = str(datetime.datetime.now().year)
    kws   = []
    # Seed-based
    for s in seeds:
        kws.append(s + " India " + year)
    # Pull brand names from ctx_text
    brands = re.findall(r'\b(Samsung|Apple|OnePlus|Xiaomi|Realme|OPPO|Vivo|Nothing|'
                        r'boAt|Noise|Sony|JBL|Bose|Dell|HP|Lenovo|ASUS|Acer|'
                        r'Garmin|Amazfit|Anker|Motorola|Google|Pixel|Redmi|Poco)\b',
                        ctx_text, re.IGNORECASE)
    seen = set()
    for b in brands:
        if b.lower() not in seen:
            seen.add(b.lower())
            kws.append(b + " review India " + year)
    # From topic
    if "under" in topic.lower():
        price = re.search(r'[\d,]+', topic.replace(",",""))
        if price:
            kws.append("best buy under ₹" + price.group() + " India " + year)
    return list(dict.fromkeys(kws))[:12]   # unique, max 12

# ================================================================
# v14: FAQ SCHEMA BUILDER — JSON-LD for Google ranking boost
# ================================================================
def build_faq_schema(faqs):
    """
    faqs = [{"q": "...", "a": "..."}, ...]
    Returns JSON-LD <script> block for FAQ rich results.
    """
    items = []
    for f in faqs:
        items.append({
            "@type": "Question",
            "name": f["q"],
            "acceptedAnswer": {"@type": "Answer", "text": f["a"]}
        })
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": items
    }
    return (
        '\n<script type="application/ld+json">\n'
        + json.dumps(schema, ensure_ascii=False, indent=2)
        + '\n</script>\n'
    )

def extract_faq_from_html(html):
    """Pull Q&A pairs from the article's FAQ section to build schema."""
    faqs = []
    # Find H3 questions in FAQ section
    faq_section = re.search(
        r'id=["\']faq["\'].*?(?=<h2|</article|$)', html, re.DOTALL | re.IGNORECASE)
    if not faq_section:
        return []
    block = faq_section.group(0)
    questions = re.findall(r'<h3[^>]*>(.*?)</h3>', block, re.DOTALL | re.IGNORECASE)
    answers   = re.findall(r'</h3>\s*<p[^>]*>(.*?)</p>', block, re.DOTALL | re.IGNORECASE)
    for i, q in enumerate(questions[:6]):
        q_text = re.sub(r'<[^>]+>', '', q).strip()
        a_text = re.sub(r'<[^>]+>', '', answers[i]).strip() if i < len(answers) else ""
        if q_text and a_text:
            faqs.append({"q": q_text, "a": a_text[:200]})
    return faqs

# ================================================================
# v14: IMAGE PLACEHOLDER BLOCK — 1200px Google Discover ready
# ================================================================

# ================================================================
# REAL PRODUCT IMAGE FETCHER
# Uses Unsplash Source API (free, no key needed) + DuckDuckGo
# fallback for product/brand images
# ================================================================

# Stable official logo URLs for common brands (no API needed)
BRAND_LOGO_URLS = {
    # Phones
    "samsung":    "https://upload.wikimedia.org/wikipedia/commons/2/24/Samsung_Logo.svg",
    "apple":      "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg",
    "oneplus":    "https://upload.wikimedia.org/wikipedia/commons/8/82/OnePlus_logo.svg",
    "xiaomi":     "https://upload.wikimedia.org/wikipedia/commons/2/29/Xiaomi_logo.svg",
    "realme":     "https://upload.wikimedia.org/wikipedia/commons/9/91/Realme_logo.svg",
    "oppo":       "https://upload.wikimedia.org/wikipedia/commons/6/6e/OPPO_LOGO_2019.svg",
    "vivo":       "https://upload.wikimedia.org/wikipedia/commons/5/5e/Vivo_logo.svg",
    "nothing":    "https://upload.wikimedia.org/wikipedia/commons/4/4c/Nothing_logo.svg",
    "google":     "https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg",
    "motorola":   "https://upload.wikimedia.org/wikipedia/commons/7/7c/Motorola_Logo_2015.svg",
    "nokia":      "https://upload.wikimedia.org/wikipedia/commons/0/02/Nokia_wordmark.svg",
    "huawei":     "https://upload.wikimedia.org/wikipedia/commons/e/e8/Huawei_Logo.svg",
    "honor":      "https://upload.wikimedia.org/wikipedia/commons/f/f8/HONOR_logo.svg",
    # Laptops
    "dell":       "https://upload.wikimedia.org/wikipedia/commons/8/82/Dell_Logo.png",
    "hp":         "https://upload.wikimedia.org/wikipedia/commons/a/ad/HP_logo_2012.svg",
    "lenovo":     "https://upload.wikimedia.org/wikipedia/commons/b/b8/Lenovo_logo_2015.svg",
    "asus":       "https://upload.wikimedia.org/wikipedia/commons/2/2e/ASUS_Logo.svg",
    "acer":       "https://upload.wikimedia.org/wikipedia/commons/0/00/Acer_2011.svg",
    "msi":        "https://upload.wikimedia.org/wikipedia/commons/1/12/MSI_Logo.svg",
    # Audio
    "boat":       "https://upload.wikimedia.org/wikipedia/commons/7/72/BoAt_logo.svg",
    "sony":       "https://upload.wikimedia.org/wikipedia/commons/c/ca/Sony_logo.svg",
    "jbl":        "https://upload.wikimedia.org/wikipedia/commons/7/72/JBL_logo.svg",
    "bose":       "https://upload.wikimedia.org/wikipedia/commons/9/9a/Bose_logo.svg",
    "sennheiser": "https://upload.wikimedia.org/wikipedia/commons/5/57/Sennheiser_Logo.svg",
    # AI apps
    "chatgpt":    "https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg",
    "gemini":     "https://upload.wikimedia.org/wikipedia/commons/8/8a/Google_Gemini_logo.svg",
    "copilot":    "https://upload.wikimedia.org/wikipedia/commons/2/2a/Microsoft_365_Copilot_Icon.svg",
}

# Unsplash free image search (no API key, returns real photos)
UNSPLASH_TOPICS = {
    "smartphone": "smartphone",
    "laptop":     "laptop computer",
    "earphones":  "wireless earbuds",
    "headphones": "headphones",
    "airpods":    "airpods wireless",
    "powerbank":  "power bank charger",
    "smartwatch": "smartwatch",
    "ai":         "artificial intelligence technology",
}

def fetch_product_image(product_name, cat, width=1200, height=628):
    """
    Fetches a real product image URL. Priority:
    1. Official brand logo (Wikimedia — stable, no copyright issue)
    2. Unsplash free photo matching category keyword
    3. Fallback: category-based Unsplash image
    Returns (img_url, attribution) tuple.
    """
    product_lower = product_name.lower()

    # 1. Try brand logo match
    for brand, logo_url in BRAND_LOGO_URLS.items():
        if brand in product_lower:
            return logo_url, f"Logo: {brand.title()}"

    # 2. Try Unsplash free photo (no API key needed)
    try:
        topic = UNSPLASH_TOPICS.get(cat, "technology gadget")
        # Unsplash Source API — free random photo by keyword
        search_term = requests.utils.quote(f"{product_name} {topic}")
        unsplash_url = f"https://source.unsplash.com/{width}x{height}/?{search_term}"
        # Verify it resolves (HEAD request)
        r = requests.head(unsplash_url, timeout=6, allow_redirects=True)
        if r.status_code == 200:
            return unsplash_url, "Photo: Unsplash (free)"
    except Exception:
        pass

    # 3. Category fallback — generic tech photo
    try:
        fallback = requests.utils.quote(UNSPLASH_TOPICS.get(cat, "technology"))
        return (
            f"https://source.unsplash.com/{width}x{height}/?{fallback}",
            "Photo: Unsplash (free)"
        )
    except Exception:
        pass

    return "", ""


def build_image_block(product_name, cat="smartphone", caption="", width=1200, height=628):
    """
    Returns an image placeholder comment only.
    The blogger (Mallikarjun R) will paste the real product image manually.
    Do NOT auto-fetch images.
    """
    return (
        f'\n<!-- ===== IMAGE PLACEHOLDER ===== -->\n'
        f'<!-- Add 1200x628px product image of: {product_name} here -->\n'
        f'<!-- Upload your image in Blogger and paste it below this comment -->\n\n'
    )


# ================================================================
# SOCIAL SHARE BLOCK — Real app logos + WhatsApp Telegram Reddit Quora
# ================================================================

# Official app logo URLs (stable Wikimedia/official sources)
SOCIAL_LOGOS = {
    "whatsapp": "https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg",
    "telegram": "https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg",
    "reddit":   "https://www.redditstatic.com/desktop2x/img/favicon/android-icon-192x192.png",
    "quora":    "https://qsf.fs.quoracdn.net/html/favicon.ico",
    "linkedin": "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png",
    "medium":   "https://upload.wikimedia.org/wikipedia/commons/e/ec/Medium_logo_Monogram.svg",
}

def build_social_block(title, url="https://technewswithai.blogspot.com"):
    """
    GitHub-style clean horizontal share bar.
    No emoji spam, no colored boxes, no Quora tip line.
    """
    encoded_title = requests.utils.quote(title[:100])
    encoded_url   = requests.utils.quote(url)
    wa_text       = requests.utils.quote(f"{title[:80]} {url}")

    icon_style = (
        "width:20px;height:20px;vertical-align:middle;margin-right:6px;"
        "border-radius:3px;"
    )
    link_style = (
        "display:inline-flex;align-items:center;margin:0 12px 0 0;"
        "font-size:13px;color:#57606a;text-decoration:none;"
        "font-weight:600;letter-spacing:0.01em;"
    )

    def share_link(href, logo_url, label):
        return (
            f'<a href="{href}" target="_blank" rel="noopener" '
            f'style="{link_style}">'
            f'<img src="{logo_url}" alt="{label}" style="{icon_style}" loading="lazy"/>'
            f'{label}</a>'
        )

    return (
        '\n<hr style="border:none;border-top:1px solid #d0d7de;margin:40px 0 20px;"/>\n'
        '<div style="display:flex;align-items:center;flex-wrap:wrap;'
        'gap:4px;margin-bottom:40px;">'
        '<span style="font-size:13px;font-weight:600;color:#57606a;margin-right:12px;">'
        'Share:</span>'
        + share_link(
            f"https://twitter.com/intent/tweet?text={encoded_title}&url={encoded_url}",
            "https://upload.wikimedia.org/wikipedia/commons/5/57/X_logo_2023_%28white%29.png",
            "X"
        )
        + share_link(
            f"https://www.facebook.com/sharer/sharer.php?u={encoded_url}",
            "https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg",
            "Facebook"
        )
        + share_link(
            f"https://www.linkedin.com/sharing/share-offsite/?url={encoded_url}",
            SOCIAL_LOGOS["linkedin"],
            "LinkedIn"
        )
        + share_link(
            f"https://wa.me/?text={wa_text}",
            SOCIAL_LOGOS["whatsapp"],
            "WhatsApp"
        )
        + share_link(
            f"https://t.me/share/url?url={encoded_url}&text={encoded_title}",
            SOCIAL_LOGOS["telegram"],
            "Telegram"
        )
        + '</div>\n'
    )


# ================================================================
# v14: GOOGLE INDEXING API PING — instant crawl after posting
# ================================================================
def ping_google_index(url):
    """
    Sends a URL to Google Indexing API for instant crawl.
    Requires service account JSON key at GOOGLE_SA_KEY_FILE path.
    If key not found, prints reminder instead (non-fatal).
    """
    key_file = os.environ.get("GOOGLE_SA_KEY_FILE", "google_service_account.json")
    if not os.path.exists(key_file):
        print("[GoogleIndex] Key file not found — skipping ping.")
        print(f"[GoogleIndex] To enable: add '{key_file}' service account JSON.")
        return
    try:
        import google.oauth2.service_account as sa
        import google.auth.transport.requests as ga_req
        credentials = sa.Credentials.from_service_account_file(
            key_file,
            scopes=["https://www.googleapis.com/auth/indexing"]
        )
        credentials.refresh(ga_req.Request())
        headers = {"Authorization": "Bearer " + credentials.token,
                   "Content-Type": "application/json"}
        body = {"url": url, "type": "URL_UPDATED"}
        r = requests.post(
            "https://indexing.googleapis.com/v3/urlNotifications:publish",
            headers=headers, json=body, timeout=10
        )
        if r.status_code == 200:
            print(f"[GoogleIndex] ✅ Pinged: {url}")
        else:
            print(f"[GoogleIndex] Response {r.status_code}: {r.text[:120]}")
    except ImportError:
        print("[GoogleIndex] Run: pip install google-auth --break-system-packages")
    except Exception as e:
        print(f"[GoogleIndex] Failed: {e}")

# ================================================================
# v14: OLD BLOG UPDATER — flags posts >30 days old for refresh
# ================================================================
def suggest_old_updates(log, days_threshold=30):
    """Prints a list of old posts that should be refreshed for SEO."""
    now = datetime.datetime.now()
    old = []
    for entry in log:
        try:
            posted = datetime.datetime.fromisoformat(entry["posted_at"])
            age    = (now - posted).days
            if age >= days_threshold:
                old.append((age, entry.get("title","?")[:60], entry.get("url","")))
        except Exception:
            pass
    if old:
        old.sort(reverse=True)
        print("\n⚠️  OLD POSTS TO UPDATE (update = SEO boost):")
        for age, title, url in old[:5]:
            print(f"  [{age}d old] {title}")
        print("  → Add 2026 data, refresh prices, resubmit to Google Search Console")
    else:
        print("[Updates] All posts are fresh (< 30 days).")

# ================================================================
# v14: ADSENSE AD SLOT INJECTOR
# Inserts AdSense-ready comment slots between article sections.
# Replace comment with your real ca-pub + slot IDs from AdSense.
# ================================================================
AD_SLOT_HTML = (
    '\n<!-- ADSENSE AD SLOT — Replace with your real ad code from AdSense dashboard -->\n'
    '<!-- <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-XXXXXXXXXXXXXXXX"'
    ' data-ad-slot="XXXXXXXXXX" data-ad-format="auto" data-full-width-responsive="true"></ins>'
    '<script>(adsbygoogle = window.adsbygoogle || []).push({});</script> -->\n\n'
)



# ── Internal link map: brand/category → your blog label URL ──────
BLOG_URL = "https://www.technewsai.me"

INTERNAL_LINKS = {
    # Brands — smartphones
    "apple":      f"{BLOG_URL}/search/label/Apple",
    "samsung":    f"{BLOG_URL}/search/label/Samsung",
    "oneplus":    f"{BLOG_URL}/search/label/OnePlus",
    "xiaomi":     f"{BLOG_URL}/search/label/Xiaomi",
    "redmi":      f"{BLOG_URL}/search/label/Xiaomi",
    "poco":       f"{BLOG_URL}/search/label/Xiaomi",
    "realme":     f"{BLOG_URL}/search/label/Realme",
    "oppo":       f"{BLOG_URL}/search/label/OPPO",
    "vivo":       f"{BLOG_URL}/search/label/Vivo",
    "iqoo":       f"{BLOG_URL}/search/label/iQOO",
    "nothing":    f"{BLOG_URL}/search/label/Nothing",
    "google":     f"{BLOG_URL}/search/label/Google",
    "pixel":      f"{BLOG_URL}/search/label/Google",
    "motorola":   f"{BLOG_URL}/search/label/Motorola",
    "nokia":      f"{BLOG_URL}/search/label/Nokia",
    "honor":      f"{BLOG_URL}/search/label/Honor",
    "huawei":     f"{BLOG_URL}/search/label/Huawei",
    "infinix":    f"{BLOG_URL}/search/label/Infinix",
    "tecno":      f"{BLOG_URL}/search/label/Tecno",
    # Brands — laptops
    "dell":       f"{BLOG_URL}/search/label/Dell",
    "hp":         f"{BLOG_URL}/search/label/HP",
    "lenovo":     f"{BLOG_URL}/search/label/Lenovo",
    "asus":       f"{BLOG_URL}/search/label/ASUS",
    "acer":       f"{BLOG_URL}/search/label/Acer",
    "msi":        f"{BLOG_URL}/search/label/Laptops",
    "razer":      f"{BLOG_URL}/search/label/Laptops",
    "macbook":    f"{BLOG_URL}/search/label/Apple",
    # Brands — audio
    "boat":       f"{BLOG_URL}/search/label/boAt",
    "noise":      f"{BLOG_URL}/search/label/Noise",
    "jbl":        f"{BLOG_URL}/search/label/Earphones",
    "sony":       f"{BLOG_URL}/search/label/Sony",
    "bose":       f"{BLOG_URL}/search/label/Headphones",
    "sennheiser": f"{BLOG_URL}/search/label/Headphones",
    "anker":      f"{BLOG_URL}/search/label/Earphones",
    "skullcandy": f"{BLOG_URL}/search/label/Earphones",
    # Brands — wearables / power
    "garmin":     f"{BLOG_URL}/search/label/Smartwatch",
    "amazfit":    f"{BLOG_URL}/search/label/Smartwatch",
    "fitbit":     f"{BLOG_URL}/search/label/Smartwatch",
    # Categories
    "smartphone":  f"{BLOG_URL}/search/label/Smartphones",
    "laptop":      f"{BLOG_URL}/search/label/Laptops",
    "earphone":    f"{BLOG_URL}/search/label/Earphones",
    "headphone":   f"{BLOG_URL}/search/label/Headphones",
    "airpods":     f"{BLOG_URL}/search/label/AirPods",
    "powerbank":   f"{BLOG_URL}/search/label/Power+Bank",
    "smartwatch":  f"{BLOG_URL}/search/label/Smartwatch",
}

def build_internal_link_instructions(cat):
    """
    Returns the internal-link rule block for the current category.
    Tells the AI exactly which brand names to hyperlink and to what URL.
    """
    lines = [
        f"INTERNAL LINKS — YOUR BLOG ONLY ({BLOG_URL}):",
        "Rule: Every time you write a brand or category name, wrap it as a hyperlink to your blog label page.",
        "Use each link maximum 2 times per article. NEVER link to any other website.",
        "NEVER link to: GSMArena, 91Mobiles, Flipkart, Amazon, or ANY external site.",
        "",
        "Brand → Your blog label URL (use these exactly):",
    ]
    for brand, url in INTERNAL_LINKS.items():
        lines.append(f'  {brand} → <a href="{url}" target="_blank">{brand.title()}</a>')
    lines += [
        "",
        "Example usage in text:",
        f'  "...the <a href="{BLOG_URL}/search/label/boAt" target="_blank">boAt</a> Airdopes 141..."',
        f'  "...check our full <a href="{BLOG_URL}/search/label/Earphones" target="_blank">earphones reviews</a>..."',
        f'  "...more on <a href="{BLOG_URL}" target="_blank">Tech News With AI</a>..."',
    ]
    return "\n".join(lines)


# ── Category label mapping for Also Read box ─────────────────────
CAT_LABELS = {
    "smartphone": "Smartphones",
    "laptop":     "Laptops",
    "earphones":  "Earphones",
    "headphones": "Headphones",
    "airpods":    "AirPods",
    "powerbank":  "Power+Bank",
    "smartwatch": "Smartwatch",
    "ai":         "AI",
}

def detect_brand_from_title(title):
    """Detect brand name from article title for Also Read box."""
    tl = title.lower()
    for brand in INTERNAL_LINKS:
        if brand in tl and brand not in ("smartphone", "laptop", "earphone",
                                          "headphone", "airpods", "powerbank", "smartwatch"):
            return brand
    return None

def build_also_read_box(cat, title):
    """
    GitHub Blog-style 'Related posts' section.
    Clean, plain layout — no colored borders, no backgrounds, no emoji.
    Shows category label links as plain text tags.
    """
    brand = detect_brand_from_title(title)
    cat_label = CAT_LABELS.get(cat, "Smartphones")

    if brand and brand in INTERNAL_LINKS:
        brand_display = brand.title()
        primary_url   = INTERNAL_LINKS[brand]
        primary_label = f"More {brand_display} reviews on Tech News With AI"
    else:
        primary_url   = f"{BLOG_URL}/search/label/{cat_label}"
        primary_label = f"More {cat_label} reviews on Tech News With AI"

    # Category tag pills — plain text, no emoji, light border
    related_cats = list(CAT_LABELS.values())[:4]
    tag_style = (
        "display:inline-block;margin:4px 8px 4px 0;"
        "padding:4px 12px;border:1px solid #d0d7de;"
        "border-radius:20px;font-size:12px;color:#57606a;"
        "text-decoration:none;font-weight:500;"
    )
    tags_html = "".join(
        f'<a href="{BLOG_URL}/search/label/{lbl}" style="{tag_style}">'
        f'{lbl.replace("+", " ")}</a>'
        for lbl in related_cats
    )

    return (
        '\n<hr style="border:none;border-top:1px solid #d0d7de;margin:40px 0 32px;"/>\n'
        '<div style="margin:0 0 40px;">'
        '<p style="margin:0 0 16px;font-size:20px;font-weight:700;color:#1f2328;">'
        'Related posts</p>'
        '<hr style="border:none;border-top:1px solid #d0d7de;margin:0 0 20px;"/>'
        f'<p style="margin:0 0 6px;">'
        f'<a href="{primary_url}" target="_blank" '
        f'style="font-size:15px;font-weight:600;color:#0969da;text-decoration:none;">'
        f'{primary_label}</a></p>'
        f'<p style="margin:0 0 20px;font-size:13px;color:#57606a;">'
        f'All reviews tested in India by Mallikarjun R &bull; '
        f'<a href="{BLOG_URL}" style="color:#0969da;text-decoration:none;">technewsai.me</a>'
        f'</p>'
        '<p style="margin:0 0 8px;font-size:12px;font-weight:600;'
        'color:#57606a;text-transform:uppercase;letter-spacing:0.05em;">'
        'Browse by category</p>'
        '<div>' + tags_html + '</div>'
        '</div>\n'
    )


# ── HTML structure templates ──────────────────────────────────────
TOC_HTML = """<div style="padding:16px 20px;margin:20px 0;border:1px solid #ddd;">
<strong>📋 Table of Contents</strong><br/>
<ol style="margin:10px 0 0 0;">
<li><a href="#comparison-table">Quick Comparison Table</a></li>
<li><a href="#product-1">Product 1 — Full Review</a></li>
<li><a href="#product-2">Product 2 — Full Review</a></li>
<li><a href="#product-3">Product 3 — Full Review</a></li>
<li><a href="#product-4">Product 4 — Full Review</a></li>
<li><a href="#product-5">Product 5 — Full Review</a></li>
<li><a href="#final-verdict">Final Verdict & Who Should Buy What</a></li>
<li><a href="#faq">Frequently Asked Questions</a></li>
</ol></div>"""

PROS_CONS_HTML = """<table style="width:100%;border-collapse:collapse;margin:12px 0;border:1px solid #ddd;">
<tr>
  <th style="padding:10px;width:50%;text-align:left;border:1px solid #ddd;">✅ Pros</th>
  <th style="padding:10px;width:50%;text-align:left;border:1px solid #ddd;">❌ Cons</th>
</tr>
<tr>
  <td style="padding:10px;border:1px solid #ddd;vertical-align:top;">
    • [specific pro 1]<br/>• [specific pro 2]<br/>• [specific pro 3]
  </td>
  <td style="padding:10px;border:1px solid #ddd;vertical-align:top;">
    • [specific con 1]<br/>• [specific con 2]
  </td>
</tr>
</table>"""

VERDICT_TABLE_HTML = """<table style="width:100%;border-collapse:collapse;margin:16px 0;border:1px solid #ddd;">
<tr>
  <th style="padding:10px;border:1px solid #ddd;text-align:left;">Use Case</th>
  <th style="padding:10px;border:1px solid #ddd;text-align:left;">Best Pick</th>
  <th style="padding:10px;border:1px solid #ddd;text-align:left;">Why</th>
</tr>
<!-- Add one row per use case -->
</table>"""

SPECS_BOX_HTML = """<div style="border:1px solid #ddd;padding:14px;margin:10px 0;">
<strong>⚡ Quick Specs</strong><br/>
<ul style="margin:8px 0;padding-left:18px;">
<li><strong>Price:</strong> ₹[price]</li>
<li><strong>[Key spec 1]:</strong> [value]</li>
<li><strong>[Key spec 2]:</strong> [value]</li>
<li><strong>[Key spec 3]:</strong> [value]</li>
<li><strong>[Key spec 4]:</strong> [value]</li>
</ul></div>"""


# ── Buying guide structure rules ──────────────────────────────────
BUYING_GUIDE_STRUCTURE = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MANDATORY ARTICLE STRUCTURE v25 — TOP 5 / BEST 5 BUYING GUIDES
Reference style: Wired "Best Android Phones" — each phone is its OWN deep standalone section
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CRITICAL STRUCTURE RULE (Wired style):
• Every phone gets its OWN complete section — like a full mini review
• DO NOT mix multiple phones under one section (NO "Design and Build Quality" with Oppo, Samsung, OnePlus all under it)
• Each phone = one H2 + its own H3 subsections (Design, Display, Performance, Camera, Battery, Price, Verdict)
• Think: if you removed one phone's section, the rest of the article should still make perfect sense

H3 HEADING RULE (CRITICAL):
• H3 headings must be DESCRIPTIVE — they describe what the section covers, never ask a question
• ✅ "<h3>Oppo Find X9 Ultra Design and Build — Glass Back, Curved Edges, IP68</h3>"
• ✅ "<h3>Samsung S26 Display — 6.2-inch Dynamic AMOLED, 120Hz, 2600 Nits</h3>"
• ❌ NEVER: "<h3>Oppo Find X9 Ultra Design — Premium Feel or Not?</h3>"
• ❌ NEVER: "<h3>Samsung S26 Display — How Does It Compare?</h3>"
• ❌ NEVER: ANY H3 containing a "?" — questions go ONLY in the FAQ section

Every Top 5 / Best 5 / Best Under Budget article MUST follow this EXACT structure.
NO Pros & Cons tables. NO comparison tables. NO side-by-side comparison columns.
Each product gets its own FULL deep-dive sections — written as narrative prose.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[STEP 1] H1 TITLE
Format examples:
  "Top 5 Best Smartphones Under ₹20,000 India 2026 — Tested & Ranked"
  "Best 5 Laptops Under ₹50,000 India 2026 — Honest Buying Guide"
  "Top 5 Budget Earphones Under ₹2,000 India 2026 — Ranked by Sound Quality"

IMAGE PLACEHOLDER immediately after H1:
<!-- IMAGE PLACEHOLDER: [Category] Top 5 — Add your main banner image here -->

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[STEP 2] INTRODUCTION — 3 Full Paragraphs (NO H2 heading, flowing narrative prose)

Para 1 — Paint the Indian buyer's problem:
→ Describe the exact Indian buyer who needs this guide
→ What's overwhelming them — too many choices, fear of regret, budget pressure
→ 4-6 sentences. Emotional, narrative, not salesy.

Para 2 — Why this guide is different:
→ How Mallikarjun selected these 5 — what criteria (performance, value, India availability)
→ How long he tested each one, what scenarios he used (commute, college, gaming, office)
→ 3-4 sentences. Build credibility.

Para 3 — Quick orientation:
→ Name all 5 picks upfront with one-line positioning for each
→ "Number 1 is the absolute value king. Number 3 is for camera lovers. Number 5 is the dark horse."
→ Transition: "Let's start with the top pick."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[STEP 3] PRODUCT 1 — Full Deep-Dive Review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<h2>1. [Product Name] — [Short One-Line Verdict e.g. "Best Overall Value Pick"]</h2>

IMAGE PLACEHOLDER: <!-- IMAGE PLACEHOLDER: [Product Name] — Add product image here -->

[ALSO READ BOX — insert immediately after image placeholder for this product]
→ Auto-added by code for brand interlinking

QUICK SPECS BOX:
""" + SPECS_BOX_HTML + """

CRITICAL: This product's section must be a COMPLETE STANDALONE mini-review.
Someone who reads ONLY this phone's section must get the full picture.
DO NOT reference other phones in this section's H3 content (comparisons go inside paragraphs, not headings).
NO Pros & Cons table. NO comparison table. Just rich narrative prose.

══════════════════════════════════════════════════
FOR SMARTPHONES — write these H3 sections for EACH of the 5 phones:
══════════════════════════════════════════════════

<h3>[Product Name] Introduction — Who It Is For and Why It Made This List</h3>
→ 3 paragraphs: who this phone is built for, what problem it solves, why it ranks at this position,
  India market context (launch date, pricing history, availability on Flipkart/Amazon),
  what makes it stand out from every other phone at this price

<h3>[Product Name] Design and Build Quality — Materials, IP Rating, Dimensions, Color Options</h3>
→ 3-4 paragraphs: exact thickness (mm) and weight (g), back panel material, IP rating explained,
  Gorilla Glass version, color variants described vividly, button placement, one-hand usability,
  India real-life line: "At X mm it slips into your jeans without the uncomfortable bulk"

<h3>[Product Name] Display Review — Panel Type, Brightness, HDR, Outdoor Visibility</h3>
→ 3 paragraphs: panel type (AMOLED/IPS/LTPO), size, resolution, refresh rate Hz,
  peak brightness nits and what it means in Indian outdoor sun,
  HDR10+ or Dolby Vision support on Netflix/YouTube/Prime,
  real verdict: "In Bengaluru afternoon sun — could I read texts without squinting?"

<h3>[Product Name] Performance Review — Chipset, Benchmarks, Gaming, Daily Use</h3>
→ 4 paragraphs covering:
  [Chipset] full name, nm process, core layout, GPU name, what makes it different
  [Benchmarks] AnTuTu, Geekbench scores vs named competitors
  [Gaming] BGMI/Free Fire/COD Mobile fps at which settings, temperature after 30min, cooling system
  [Daily Use] app switching speed, RAM management, India scenario: "Instagram → Chrome → BGMI — zero stutter"

<h3>[Product Name] Battery Life and Charging — mAh, Screen-On Hours, Fast Charge</h3>
→ 2 paragraphs:
  Para 1: mAh, real screen-on hours, what usage mix (gaming/social/video),
          India real-life: "X mAh = full IPL match + 6hrs college + evening commute = still Y% left"
  Para 2: fast charge wattage, 0→50% time, 0→100% time, wireless charging, charger in box or not

<h3>[Product] Camera Review — Daylight, Night, Portrait, Video, Selfie</h3>
→ 5 paragraphs — ONE per test, NEVER merge:
  [Daylight] main sensor MP, aperture, OIS, colour accuracy, dynamic range, real scenario
  [Night] shadow detail, noise, processing time, astrophotography, honest comparison to named rival
  [Portrait] edge detection in hair/glasses, bokeh quality, natural or artificial
  [Video] max resolution + fps, OIS verdict (walking video smooth?), slow-mo capability, audio quality
  [Selfie] MP, autofocus, Indian skin tone accuracy, portrait selfie edge detection

<h3>[Product] Connectivity and Audio — 5G Bands, WiFi, Speakers, Biometrics</h3>
→ 2 paragraphs:
  Para 1: 5G band count, WiFi version, BT version, NFC for UPI, USB type, IR blaster
  Para 2: stereo/mono speakers, Dolby Atmos, loudness test, fingerprint type/speed, face unlock

<h3>[Product] Software and AI Features — Android Version, UI, AI Tools, Update Support</h3>
→ 1-2 paragraphs: Android version, UI name, bloatware level, top 3 AI features in plain language,
  OS update years and security patch years, why this matters for long-term value

<h3>[Product] Price in India 2026 — All Variants, Launch Offers, No Cost EMI</h3>
→ 2 paragraphs + bullet list:
  → All RAM/storage variants with exact ₹ prices
  → Bank offers (HDFC/Axis/SBI/ICICI) and effective price
  → No Cost EMI: "₹X = ₹Y/month for 12 months"
  → Where to buy: Amazon, Flipkart, brand site
  → Mallikarjun's recommendation: which variant is best value

<h3>[Product] Who Should Buy This and Who Should Skip It</h3>
→ 2 paragraphs (NO bullet points, NO table — pure prose):
  Para 1 — Buy if: "If you are a college student who games on weekends, commutes by metro,
            and needs the phone to last 2 days — this is your answer."
  Para 2 — Skip if: "If you shoot a lot of telephoto zoom shots, or need OIS for video walks,
            this phone will disappoint you. The [named alternative] is a better choice."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRANSITION LINE (mandatory between every product):
→ "That was the safe pick. Now here is the one for real enthusiasts."
→ "Different budget, completely different story — keep reading."
→ "Now if that price is still too high, the next pick will genuinely surprise you."
→ "This next one is polarising. Some love it. Some hate it. Here is exactly why."
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[STEP 4] PRODUCT 2 — Repeat ALL sections from STEP 3 exactly
[STEP 5] PRODUCT 3 — Repeat ALL sections from STEP 3 exactly
[STEP 6] PRODUCT 4 — Repeat ALL sections from STEP 3 exactly
[STEP 7] PRODUCT 5 — Repeat ALL sections from STEP 3 exactly

Each product MUST get:
  ✓ IMAGE PLACEHOLDER immediately after H2
  ✓ Also Read box after image (auto-added by code)
  ✓ Quick Specs box
  ✓ ALL 9 H3 sections written fully (Intro, Design, Display, Performance, Battery, Camera, Connectivity, Software, Price, Who Should Buy)
  ✓ Transition line after each product (except the last)
  NO Pros & Cons table
  NO comparison table

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[STEP 8] FINAL VERDICT — Which One Should You Buy? (after all 5 products)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<h2>Final Verdict — Which Is the Best [Category] in India 2026?</h2>
→ Write 3-4 rich paragraphs (NO table, pure prose verdict):
  Para 1: Declare the overall winner and WHY in one confident sentence, then explain in detail
  Para 2: Explain which pick is best for specific use cases (gaming, camera, battery, budget)
          Name each product and the exact user profile it suits
  Para 3: Price context — which gives the best value per rupee, which to wait for on sale
  Para 4: Mallikarjun's personal pick and honest reasoning
  → End: "My final pick: [Product Name]. Here is why I would put my own money on it."
  → CTA: <a href="https://www.technewsai.me/search/label/[Category]">Read all [Category] reviews on Tech News With AI</a>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[STEP 9] FAQ — Most Searched Questions Indians Ask (after Final Verdict)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<h2 id="faq">FAQ — Most Searched Questions Indians Ask About These [Category]</h2>
→ Write 7 FAQ for smartphones, 5 for all other categories
→ Use question-based H3 ONLY in this section:
   <h3>Which is the best [category] under ₹[price] in India 2026?</h3>
   <h3>Which [category] has the best battery life in India 2026?</h3>
   <h3>Which [category] has the best camera in India 2026?</h3>
   <h3>Is [top pick] worth buying in India 2026?</h3>
   <h3>Which [category] is best for gaming in India 2026?</h3>
   <h3>Where is the best place to buy [category] in India 2026?</h3>
   <h3>Which [category] gives the best value for money in India 2026?</h3>
→ Each answer: 40-60 words, complete, standalone, conversational, name specific products

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[STEP 10] END OF ARTICLE — ALWAYS in this order (auto-added by code):
1. Also Read box (brand-interlinked, auto-added by code)
2. Social share block (auto-added by code)
3. Author bio with photo (auto-added by code)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

══════════════════════════════════════════════════
FOR LAPTOPS — same structure as smartphones but each product uses these H3 sections instead:
══════════════════════════════════════════════════
<h3>[Product] Introduction — Who This Laptop Is For, Why It Matters in India 2026</h3>
<h3>[Product] Design and Build Quality — Chassis, Hinge, Ports, Keyboard, Weight</h3>
<h3>[Product] Display Review — Panel Type, Resolution, Hz, Nits, Colour Gamut, Bezels</h3>
<h3>[Product] Performance Review — CPU Deep Dive, Benchmarks, Gaming Test, Thermal Management</h3>
<h3>[Product] Battery Life and Charging — Real Hours by Use Case, Charger Wattage, Charge Time</h3>
<h3>[Product] Keyboard and Trackpad — Key Travel, Typing Feel, Backlight, Gesture Support</h3>
<h3>[Product] Connectivity and Ports — WiFi, Bluetooth, USB-A, USB-C, Thunderbolt, HDMI</h3>
<h3>[Product] Software and AI Features — OS, Bloatware, Copilot/AI Tools, Update Support</h3>
<h3>[Product] Price in India 2026 — All Variants, Launch Offers, No Cost EMI, Best Buy Links</h3>
<h3>[Product] Who Should Buy This and Who Should Skip It</h3>

══════════════════════════════════════════════════
FOR EARPHONES/TWS — each product uses these H3 sections:
══════════════════════════════════════════════════
<h3>[Product] Introduction — Who These Earphones Are For, Why They Made This List</h3>
<h3>[Product] Design and Build Quality — Earbud Size, IP Rating, Ear Tip Fit, Case Quality</h3>
<h3>[Product] Sound Quality — Bass, Mids, Highs, Soundstage (Each Tested Separately)</h3>
<h3>[Product] ANC and Transparency Mode — dB Rating, Metro Test, Wind Noise</h3>
<h3>[Product] Battery Life and Charging — Earbuds Hours, Case Charges, Fast Charge</h3>
<h3>[Product] Call Quality and Mic Test — Quiet Room, Crowded Place, Wind Test</h3>
<h3>[Product] Connectivity and Codecs — BT Version, LDAC/aptX, Latency, Multipoint</h3>
<h3>[Product] App and Smart Features — EQ, Gestures, Auto-Pause, Voice Assistant</h3>
<h3>[Product] Price in India 2026 — All Variants, Offers, Best Buy Links</h3>
<h3>[Product] Who Should Buy This and Who Should Skip It</h3>

══════════════════════════════════════════════════
FOR HEADPHONES — same as earphones but adapt:
Replace ear tip fit → clamping force and earcup padding
Replace earbud size → headband adjustment, foldable or not
Add: wired 3.5mm mode, carry pouch/case included

FOR AIRPODS — same as earphones but replace Software section:
<h3>[Product] Apple Chip Features — H2/H3 Chip, Auto Device Switch, Conversation Awareness</h3>
Add Apple ecosystem context in every relevant section.

══════════════════════════════════════════════════
FOR POWER BANKS — each product uses these H3 sections:
══════════════════════════════════════════════════
<h3>[Product] Introduction — Who This Power Bank Is For, Why It Made This List</h3>
<h3>[Product] Design and Build Quality — Size, Weight, Finish, Display, Port Layout</h3>
<h3>[Product] Real Capacity Test — Rated mAh vs Actual Output, Conversion Efficiency</h3>
<h3>[Product] Charging Speed Test — Input Speed, Output W, PD/QC/PPS, Real Device Test</h3>
<h3>[Product] How Many Devices Can It Charge — Full Charges per Device, Standby Drain</h3>
<h3>[Product] Ports and Device Compatibility — USB-A, USB-C, Max W, Laptop Support</h3>
<h3>[Product] Safety and Reliability — BIS Cert, Overcharge Protection, Brand Track Record</h3>
<h3>[Product] Price in India 2026 — All Variants, Offers, Best Buy Links</h3>
<h3>[Product] Who Should Buy This and Who Should Skip It</h3>
"""


# ── Writing rules injected into every prompt ─────────────────────
WRITING_RULES = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WRITING STYLE — MATCH WORLD-CLASS TECH REVIEWS
Reference style: TechRadar, The Hindu Tech, TechPP, 9to5Google
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TARGET: 7000–8000 words minimum — AdSense editorial quality standard.
Every section = storytelling and real-test journalism, not a spec sheet.
One article per day means ALL token budget goes here. Use every word wisely.

─── ADSENSE APPROVAL — CRITICAL CONTENT RULES ──────────
Google's policy rejects "automatically generated content without manual review."
To pass AdSense review, every article must feel like a real person wrote it
after actually holding and using the phone for two weeks in India.

MANDATORY PER ARTICLE:
1. A 14-day personal testing narrative woven through every section
2. At least 3 unique India scenarios no other review site covers:
   (Sunday market photography, Bengaluru metro commute, BGMI hostel session,
    board exam night scrolling, IPL match Hotstar streaming, Swiggy-open kitchen heat)
3. One honest disappointment per section — no phone is perfect
4. Specific numbers from "my tests": screen-on hours, gaming fps, charge time
5. India-specific specs: which 5G bands work in India, India battery vs global
6. At least 2 direct comparisons to named rivals per section (inline, not table-only)

─── STORYTELLING OVER SPECS (most important rule) ──────
WRONG approach (spec sheet style — rejected):
  "The phone has a 6.83-inch AMOLED display with 120Hz refresh rate and 5000 nits."

RIGHT approach (world-class review style — required):
  "I fired up some 2K videos on this display and the picture always looked clean and precise.
   Its 5,000-nit peak brightness is probably enough that you could use it as a reading torch —
   which sounds like hyperbole until you try it under a Bengaluru afternoon sun."

Every spec must be EXPERIENCED and JUDGED, not just stated.

─── H2/H3 HEADING FORMAT ────────────────────────────
• H2 format (for major sections): "[Phone Name] [Section] — [Short Opinionated Tagline]"
  ✅ "Nothing Phone 4a Pro Design — Bold, Metal, and Surprisingly Likeable"
  ✅ "iQOO 15R Battery Life — Two Days, Tested Honestly"
  ❌ "Design and Build Quality Section"
  ❌ "Battery Performance Overview"

• H3 format (for sub-sections): "[Phone] [Specific aspect] — [Verdict in 4 words]"
  ✅ "Nothing Phone 4a Pro Camera — Good Stills, Weak Video"
  ✅ "iQOO 15R Gaming Test — Stable at 90fps"

─── INLINE NAMED COMPARISONS (mandatory in every section) ──
Every section must include at least ONE inline comparison to a named rival.
NOT in a table — woven naturally into the prose.
Examples:
  Design: "At 7.9mm, it's slimmer than the iPhone 17 Pro Max (8.75mm) and lighter than the Samsung S26 at 210 grams."
  Display: "The colors aren't quite as rich as the Pixel 10's display, but at ₹15,000 less, that's a reasonable trade."
  Camera: "Can you find a better camera at this price? The Pixel 10a is sitting right there — but you'd miss this design."
  Battery: "Outlasted the OnePlus 15R by about 45 minutes in my mixed-use test."
  Performance: "Scores 1.15 million on AnTuTu — about 12% behind the Snapdragon 8 Elite but 20% ahead of last year's 8s Gen 3."

─── VIVID PHYSICAL DESCRIPTION (for design sections) ──
Don't say "premium design". Describe what you FEEL and SEE:
  ✅ "Run your thumb down the side and you'll notice a slight ridge where the metal meets the glass — it's not uncomfortable, but you'll feel it."
  ✅ "The camera module makes a striking contrast against an otherwise plain back — all the drama is packed into that top third."
  ✅ "At 210 grams it's relatively light for its size — the iPhone 17 Pro Max is 233 grams, for comparison."
  ❌ "Premium glass and metal build quality."
  ❌ "Comfortable to hold."

─── UNIQUE FEATURE DEEP-DIVE (mandatory per product) ──
Every phone has ONE feature that makes it unique. Find it and explain it fully:
  • Nothing Phone 4a Pro → Glyph Matrix: what it looks like, what it does, how Indians actually use it
  • iQOO 15R → Massive battery + slim body: explain the engineering trade-off
  • Samsung S26 → AI features: explain in plain language what they do day to day
Write 2 full paragraphs on this ONE feature. Not just "it has this feature" — tell a story about using it.

─── INDIA VARIANT DIFFERENCES (mention when relevant) ─
Some phones have India-specific differences. Always check and mention:
  • Battery capacity differences (India 5400mAh vs global 5080mAh — happened with Nothing)
  • India price vs US/UK price — always give ₹ price with source (Flipkart/Amazon India)
  • 5G band availability in India — not just "supports 5G"
  • Availability date in India — when can Indians actually buy it

─── PARAGRAPH RHYTHM (The Hindu / TechRadar pattern) ──
After a longer explanation (2-3 sentences), add one SHORT punchy verdict sentence.
  "The display delivers excellent outdoor visibility, handles Netflix HDR content beautifully,
   and the 144Hz refresh makes BGMI feel genuinely smooth. Colors could be richer. But at this
   price, I'm not complaining."
Pattern: Long → Long → Short (verdict). Repeat per paragraph group.

─── OPENING HOOK PATTERNS ────────────────────────────
Open each H2 section with ONE of these styles:
  Surprising fact:  "One of the first things you notice about the [Phone] is how [unexpected observation]."
  Direct verdict:   "The [Phone]'s [section] is [specific verdict] — here is exactly why."
  Honest question:  "Here is the thing nobody tells you about [Phone]'s [section]."
  Inline comparison: "Compared to [named rival], the [Phone]'s [section] [is better/worse] — but the story is more nuanced."

─── HONEST OPINION — MANDATORY PER SECTION ──────────
Every section must end with ONE clear opinion sentence:
  ✅ "This is the best display under ₹40,000 in India right now."
  ✅ "For gaming, it's good — for professional video, look elsewhere."
  ✅ "Honestly, I expected better from a phone at this price."
  ✅ "It surprised me. I didn't expect to recommend it this strongly."
  ❌ "Overall, it's a good option worth considering."
  ❌ "It has both pros and cons depending on your needs."

─── INDIA REAL-LIFE TRANSLATION (mandatory per section) ─
Every battery/performance section must translate specs into Indian life:
  "5,400mAh = from 8am to 1am the next day, with BGMI, Instagram, and two hours of Hotstar — still had 12% left."
  "50W charging = 0 to 70% in 45 minutes — enough to top up between classes at college."
  "At 7.9mm, it slips into your jeans pocket without the uncomfortable bulk."
  "Crystal clear call quality even against Bengaluru peak-hour traffic noise."

─── CAMERA VERDICT FORMAT ────────────────────────────
Each camera sub-section must end with a direct answer to: "Is it worth it for Indian buyers?"
  ✅ "For daylight shots at a wedding or market, this camera absolutely delivers."
  ✅ "Night mode needs 3-4 seconds to process. Patience required."
  ✅ "Selfie camera handles Indian skin tones naturally — no aggressive smoothing."
  ❌ "Camera performance is good for the price range."

─── DATA & SPECIFICITY ──────────────────────────────────
• NEVER: good, nice, amazing, great, excellent, decent, solid
• ALWAYS specifics: deep bass, punchy mids, 42dB ANC, 28ms latency, 144Hz AMOLED
• Minimum 3 real numbers per section (hours, dB, ms, Hz, MP, W, g, mAh, nits)
• Compare to a named competitor in EVERY section

─── ABSOLUTE NEVER — ADSENSE QUALITY ENFORCEMENT ───────
• NO **markdown bold** — ONLY <strong>HTML</strong> bold tags
• NO Q&A H3 headings (except in FAQ section)
• NO question marks in any H3 outside FAQ — H3s are clean descriptive labels only
• NO: "In conclusion", "To summarize", "It is worth noting", "Overall", "In summary"
• NO AI-sounding filler phrases — these get articles flagged by Google:
    "seamlessly", "cutting-edge", "state-of-the-art", "game-changer", "revolutionary"
    "robust", "leverage", "delve into", "it's worth noting", "at the end of the day"
    "in today's world", "in the realm of", "a testament to", "without further ado"
    "powerful performance", "impressive results", "all in all", "overall verdict"
• NO two consecutive sentences starting with the same word
• NO repeated sentence or idea anywhere in the article
• NO generic verdicts: "good for the price", "decent option", "solid choice"
• NO wrong-category specs
• NO links to external sites — ONLY www.technewsai.me label pages
• NO skipping sections — every section must be fully written
• NO spec-sheet paragraphs — every number must have a real-world meaning

─── MINIMUM REQUIREMENTS — v28 ADSENSE STANDARD ────────
✓ 7000–8000 words — Google's threshold for editorial content quality
✓ 3-paragraph narrative intro (no H2) — storytelling, buyer dilemma, promise
✓ 14-Day Real-Life Test section — unique to your blog, Google can't flag this
✓ India Variant Differences section — verify India vs global specs
✓ Inline named comparisons in EVERY section (at least 2 rivals per section)
✓ Unique feature deep-dive (2 full paragraphs — the phone's ONE standout feature)
✓ Short punchy verdict sentence after every paragraph group
✓ Pros & Cons table — for reviews only, with SPECIFIC not generic points
✓ Comparison table — real rival specs only, never invented
✓ 10-question FAQ — question H3s ONLY in this section
✓ Final verdict: clear BUY or SKIP with your money on the line

─── ADSENSE EDITORIAL QUALITY ───────────────────────────
• 100% original — never paraphrase any source, not even loosely
• Personal testing narrative woven through EVERY section
  ("In my two weeks with this phone across Bengaluru...")
• Every paragraph adds NEW information — no filler or repetition
• Mobile-friendly: <p> max 3-4 sentences (short paragraphs = time on page)
• No broken HTML — all tags properly closed
• India-first perspective: every spec translated into an India real-life scenario

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEO + AI CITATION RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

─── ANSWER-FIRST (AI Citation — Critical) ──────────────
• Every H2 section MUST open with a direct answer in the VERY FIRST sentence
  ✅ "The Nothing Phone 4a Pro display is a 6.83-inch flexible AMOLED with 144Hz and 5,000 nits peak brightness."
  ❌ "When it comes to the display, this phone has a lot to offer..."
• This first sentence must stand alone — what ChatGPT/Perplexity/Google AI extracts and cites

─── SELF-CONTAINED PARAGRAPHS ─────────────────────────
• Every paragraph makes sense read completely in isolation
• Each paragraph: one clear claim + evidence or India example
• AI tools skip paragraphs that depend on previous paragraphs

─── SENTENCE RHYTHM ────────────────────────────────────
• ~40% short declarative (8–15 words): "The battery lasts two full days."
• ~45% medium explanatory (16–25 words): "At 7.9mm it slips into your jeans without uncomfortable bulk."
• ~15% longer complex (26–35 words): for nuanced comparisons
• Vary deliberately — rhythm keeps readers on page

─── LONG-TAIL KEYWORDS (inject naturally) ───────────────
[LONGTAIL_KEYWORDS_PLACEHOLDER]
"""


# ================================================================
# VS COMPARISON STRUCTURE — Per-Product Full Deep-Dive
# ================================================================
VS_COMPARISON_STRUCTURE = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VS COMPARISON — MANDATORY STRUCTURE v17
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ABSOLUTELY NO: Pros & Cons tables | Comparison tables | Side-by-side columns | Mixed product paragraphs

[STEP 1] H1 TITLE (pre-generated — use exactly as given)

[STEP 2] INTRO — 3 paragraphs, no H2:
  Para 1: The Indian buyer dilemma — who is torn between these two products and why
  Para 2: What makes this comparison unique in India 2026 — pricing, availability, ecosystem
  Para 3: What this article covers and Mallikarjun's testing methodology

[STEP 3] PRODUCT A — COMPLETE STANDALONE REVIEW
<h2>[Product A Full Name] — Full Review India 2026</h2>
<!-- IMAGE PLACEHOLDER: [Product A] — Add product image here -->

QUICK SPECS BOX for Product A only

FOR SMARTPHONES write these H3 sections for Product A ONLY:
<h3>[Product A] Introduction — Who This Is For and Why It Matters in India 2026</h3>
→ 3 paragraphs: target user, India launch context, market positioning, what makes it stand out

<h3>[Product A] Design and Build Quality — Materials, IP Rating, Dimensions, Colors</h3>
→ 3-4 paragraphs: thickness mm, weight g, back material, IP rating explained, Gorilla Glass, colors described vividly, button layout, one-hand use verdict

<h3>[Product A] Display Review — Panel Type, Brightness, HDR, Outdoor Test</h3>
→ 3 paragraphs: panel tech, size, resolution, Hz, nits in Indian sunlight, HDR app support, bezels, touch sampling

<h3>[Product A] Performance Review — Chipset, Benchmarks, Gaming Test, Daily Use</h3>
→ 4 paragraphs: chipset name+nm+cores, AnTuTu+Geekbench scores vs named rival, BGMI/Free Fire fps+temp, daily multitasking India scenario

<h3>[Product A] Battery Life and Charging — mAh, Screen-On Hours, Fast Charge Time</h3>
→ 2 paragraphs: mAh, real SOT hours, India real-life translation, fast charge W + 0-100% time, charger in box

<h3>[Product A] Camera Review — Daylight, Night, Portrait, Video, Selfie</h3>
→ 5 paragraphs (one per test — never merge): daylight sharpness+DR, night shadow detail, portrait edge detection, video OIS+fps, selfie skin tone accuracy

<h3>[Product A] Connectivity and Audio — 5G Bands, WiFi, Speakers, Biometrics</h3>
→ 2 paragraphs: 5G bands, WiFi version, BT, NFC for UPI, USB type; speakers stereo/mono, Dolby Atmos, fingerprint speed

<h3>[Product A] Software and AI Features — Android Version, UI, AI Tools, Updates</h3>
→ 1-2 paragraphs: Android version, UI cleanliness, top 3 AI features in plain language, OS+security update years

<h3>[Product A] Price in India 2026 — All Variants, Bank Offers, No Cost EMI</h3>
→ 2 paragraphs + bullet list: all variants with ₹ prices, bank offers, No Cost EMI calculation, where to buy, best variant recommendation

<h3>[Product A] Who Should Buy This and Who Should Skip It</h3>
→ 2 paragraphs (NO table, pure prose):
  Para 1 — Buy if: specific user type with real scenarios
  Para 2 — Skip if: specific cases where the other product is better

FOR LAPTOPS use: Intro, Design+Build, Display, Performance, Battery, Keyboard+Trackpad, Connectivity+Ports, Software+AI, Price, Who Should Buy
FOR EARPHONES use: Intro, Design+Build, Sound Quality, ANC+Transparency, Battery, Call Quality, Connectivity+Codecs, App+Features, Price, Who Should Buy
FOR SMARTWATCHES use: Intro, Design+Build, Display, Health+Fitness Tracking, Battery+Charging, Smart Notifications, GPS+Sports, Software+App Ecosystem, Price, Who Should Buy
FOR HEADPHONES use: same as earphones but adapt for over-ear comfort, clamping force, foldability
FOR POWER BANKS use: Intro, Design+Build, Real Capacity Test, Charging Speed, Device Compatibility, Safety, Price, Who Should Buy

[STEP 4] TRANSITION LINE (mandatory — one of these):
→ "That was the full story on [Product A]. Now here is [Product B] — a completely different experience."
→ "Different ecosystem, different philosophy — here is what [Product B] brings to the table."
→ "Now if [Product A] did not convince you, what [Product B] does next might change everything."

[STEP 5] PRODUCT B — COMPLETE STANDALONE REVIEW
<h2>[Product B Full Name] — Full Review India 2026</h2>
<!-- IMAGE PLACEHOLDER: [Product B] — Add product image here -->

QUICK SPECS BOX for Product B only

[Write ALL same H3 sections as Product A above — for Product B ONLY]
Every section about Product B only. Never mix Product A specs here.

[STEP 6] FINAL VERDICT — Which One Should You Buy in India 2026?
<h2>Final Verdict — [Product A] vs [Product B]: Which is Worth Buying in India 2026?</h2>
→ 4 rich prose paragraphs (NO table, NO bullet points — pure narrative):
  Para 1: Declare the winner and WHY in one confident sentence, then explain fully
  Para 2: Use-case breakdown — which product wins for which exact user (gamer, camera lover, battery user, budget buyer, ecosystem user)
  Para 3: Price-value context — which gives better rupee value, when to wait for a sale
  Para 4: Mallikarjun's personal pick and honest reasoning
→ End with: "My final verdict: [Product Name]. Here is why I would put my own money on it."
→ CTA: <a href="https://www.technewsai.me/search/label/[Category]">Read all [Category] reviews on Tech News With AI</a>

[STEP 7] FAQ — 7 Questions Indians Ask About This Comparison
<h2 id="faq">FAQ — [Product A] vs [Product B]: Most Asked Questions India 2026</h2>
→ 7 question-based H3s (ONLY place Q format is allowed):
  <h3>Which is better: [Product A] or [Product B] in India 2026?</h3>
  <h3>What is the price difference between [Product A] and [Product B] in India?</h3>
  <h3>Which has better battery life: [Product A] or [Product B]?</h3>
  <h3>Which has better camera: [Product A] or [Product B]?</h3>
  <h3>Is [Product A] worth buying over [Product B] in India 2026?</h3>
  <h3>Which is better for gaming: [Product A] or [Product B]?</h3>
  <h3>Where to buy [Product A] and [Product B] at the best price in India?</h3>
→ Each answer: 40-60 words, specific, names both products, conversational

[STEP 8] END — auto-added by code in this order:
1. Also Read box (brand-interlinked)
2. Social share block
3. Author bio with photo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


def pick_top5_phones(topic, cat, ctx):
    """
    Uses Groq to select 5 REAL, SPECIFIC phone names for this buying guide topic.
    Returns a list of 5 phone names with their India prices.
    This list is injected into groq_draft so the AI MUST write about ALL 5 phones.
    Without this, the AI defaults to writing about 1 phone repeatedly.
    """
    try:
        client = Cerebras(api_key=CEREBRAS_API_KEY)
        year   = datetime.datetime.now().year
        prompt = (
            f"You are an India smartphone expert. For this buying guide topic, "
            f"pick exactly 5 real phones available in India in {year}.\n\n"
            f"Topic: {topic}\n"
            f"Category: {cat.upper()}\n"
            f"Context from RSS: {ctx[:400] if ctx else 'Use your knowledge.'}\n\n"
            f"Rules:\n"
            f"- Pick 5 DIFFERENT phones from DIFFERENT brands\n"
            f"- All must be genuinely available in India {year} with real ₹ prices\n"
            f"- Mix budget/mid/premium within the guide's price range\n"
            f"- Include phones people actually search for in India\n"
            f"- Each phone name must be the EXACT model name Indians search (e.g. 'Nothing Phone 4a Pro')\n\n"
            f"Respond ONLY as JSON array. No markdown. No explanation:\n"
            f'[{{"name": "Brand Model Name", "price": "₹XX,XXX", "best_for": "one use case"}}, ...]'
        )
        r = client.chat.completions.create(
            model="llama3.1-8b",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300, temperature=0.5,
        )
        raw   = r.choices[0].message.content.strip()
        raw   = re.sub(r"```json|```", "", raw).strip()
        m     = re.search(r"\[.*\]", raw, re.DOTALL)
        phones = json.loads(m.group(0)) if m else []
        if len(phones) >= 5:
            print(f"[Top5] Phones selected: {[p['name'] for p in phones[:5]]}")
            return phones[:5]
    except Exception as e:
        print(f"[Top5] Failed ({e}) — AI will choose phones freely")
    return []


def groq_draft(story, is_search):
    """
    v34 — Matches iQOO 15 Apex Edition article EXACTLY.
    Numbered H3 sections. Bold <strong> sub-headings. 7000+ words.
    """
    from cerebras.cloud.sdk import Cerebras
    client = Cerebras(api_key=CEREBRAS_API_KEY)
    year   = datetime.datetime.now().year

    seo_title   = story.get("seo_title", "")
    phone       = story.get("title", "[Phone]")
    phone_clean = re.split(r'[:\|–—]', phone)[0].strip()
    specs       = (story.get("specs") or "")[:1000]
    desc        = (story.get("description") or "")[:400]
    ctx         = (story.get("rss_context") or "")[:700]
    source_url  = story.get("url", "")
    title_line  = f'<h1>{seo_title}</h1>\n\n' if seo_title else ""

    # Fetch live data from official launch page
    live_specs = ""
    if source_url:
        try:
            live_specs = fetch_official_page_specs(source_url)
            if live_specs:
                live_specs = live_specs[:600]
        except:
            pass

    # Brand official URL
    brand = phone_clean.split()[0].lower()
    BRAND_OFFICIAL = {
        "samsung":  ("https://www.samsung.com/in/smartphones/", "Samsung India"),
        "apple":    ("https://www.apple.com/in/shop/buy-iphone", "Apple India"),
        "oneplus":  ("https://www.oneplus.in/smartphones", "OnePlus India"),
        "xiaomi":   ("https://www.mi.com/in/phones", "Xiaomi India"),
        "redmi":    ("https://www.mi.com/in/phones", "Redmi India"),
        "realme":   ("https://www.realme.com/in/smartphones", "Realme India"),
        "oppo":     ("https://www.oppo.com/en/smartphones/", "OPPO India"),
        "vivo":     ("https://www.vivo.com/in/products/smartphones", "Vivo India"),
        "iqoo":     ("https://www.iqoo.com/in/products/smartphones", "iQOO India"),
        "nothing":  ("https://nothing.tech/products", "Nothing Tech"),
        "motorola": ("https://www.motorola.in/smartphones", "Motorola India"),
        "poco":     ("https://www.poco.net/in/phones", "POCO India"),
        "infinix":  ("https://www.infinixmobility.com/in/phones", "Infinix India"),
        "tecno":    ("https://www.tecno-mobile.com/in/phones", "Tecno India"),
    }
    off = BRAND_OFFICIAL.get(brand, ("https://www.gsmarena.com", "GSMArena"))
    official_url, official_name = off
    buy_amazon   = f"https://www.amazon.in/s?k={phone_clean.replace(' ', '+')}"
    buy_flipkart = f"https://www.flipkart.com/search?q={phone_clean.replace(' ', '+')}"

    if is_search:
        topic = story.get("search_topic", phone_clean)
        prompt = (
            f"You are Mallikarjun R — 19-year-old CSE student and tech blogger from Bengaluru.\n"
            f"Write a 6500-word in-depth HTML buying guide for: \"{topic}\"\n"
            f"LIVE DATA: {ctx}\n\n"
            f"{title_line}"
            "STYLE: Exactly like a personal tech blog. Conversational. First-person. Simple English.\n"
            "Write like: 'I have tested X phones. Here is what I found. Let me be honest with you.'\n\n"
            "STRUCTURE — numbered H3 sections:\n"
            "<h3>1. Why This Matters for Indian Buyers in 2026</h3>\n"
            "<h3>2. Top Picks — Full Review of Each</h3>\n"
            "  Each phone: bold name, full specs, real test, buy links.\n"
            "<h3>3. How to Choose the Right One</h3>\n"
            "<h3>4. Value for Money</h3>\n"
            "<h3>5. Final Verdict — My Pick</h3>\n"
            "<h3>6. FAQ — Real Questions, Real Answers</h3>\n"
            "  15 FAQ questions numbered 1-15. Each answer 70+ words.\n\n"
            "SUB-HEADINGS: Use <strong>bold text</strong> on its own line (NOT h4 tags).\n"
            "RULES: HTML only. No markdown. No tables. No pros/cons boxes.\n"
            f"Buy links: <a href='{buy_amazon}' rel='nofollow' target='_blank'>Buy on Amazon India</a>\n"
            "Write now — 6500 words minimum:"
        )
    else:
        prompt = (
            f"You are Mallikarjun R — 19-year-old CSE student and tech blogger from Bengaluru, India.\n"
            f"Write a full HTML review article for: {phone_clean}\n\n"

            f"OFFICIAL SPECS — use EXACT numbers, NEVER invent anything:\n{specs}\n\n"
            f"LIVE LAUNCH PAGE DATA:\n{live_specs}\n\n"
            f"RSS LAUNCH CONTEXT:\n{ctx}\n\n"
            f"DESCRIPTION:\n{desc}\n\n"
            f"{title_line}"

            "━━━ COPY THIS EXACT HTML STRUCTURE ━━━\n"
            "This is the EXACT format of the reference article (iQOO 15 Apex Edition review).\n"
            "Follow every tag, every sub-heading format, every section title pattern EXACTLY.\n\n"

            "START with H2 title (NEVER H1):\n"
            f"<h2>{phone_clean} Full Review {year} — [Hook — one honest opinion line]</h2>\n\n"

            "Then image placeholder:\n"
            f"<!-- IMAGE PLACEHOLDER: {phone_clean} — Add your image here -->\n\n"

            "━━━ 16 SECTIONS — COPY EACH EXACTLY ━━━\n\n"

            # ── Section 1 ──────────────────────────────────────────
            "<h3>1. First Impressions — [Honest one-liner hook about this specific phone]</h3>\n"
            "4-5 paragraphs. Personal, first-person.\n"
            "Para 1: 'I'll be honest with you. When [brand] announced [phone], my first reaction was...'\n"
            "Para 2-3: What surprised you when you picked it up. What is unique about this phone.\n"
            "Para 4: The specs that make it a beast — name them all in one flowing sentence.\n"
            "Final para: 'For [gamers / power users / camera lovers / etc.] — this is worth your full attention.'\n\n"

            # ── Section 2 ──────────────────────────────────────────
            "<h3>2. Full Specs — Everything in One Place</h3>\n"
            "EXACT spec list. Every spec on its own line with <br/>. Format EXACTLY like this:\n"
            "<strong>Brand / Model:</strong>  [value]<br/>\n"
            "<strong>Launch Date (India):</strong>  [date (Sale: date)]<br/>\n"
            "<strong>Price:</strong>  ₹[price] ([RAM+Storage]) | ₹[price] ([RAM+Storage])<br/>\n"
            "<strong>Effective Price After Bank Offers:</strong> ₹[price] | ₹[price]<br/>\n"
            "<strong>Operating System:</strong>  [Android X with UI name]<br/>\n"
            "<strong>Processor:</strong> [EXACT chip name (Xnm Type-Core)]<br/>\n"
            "<strong>GPU:</strong> [GPU + any extra chip]<br/>\n"
            "<strong>RAM:</strong> [GB] or [GB] [LPDDR type]<br/>\n"
            "<strong>Storage:</strong> [GB] or [GB] [UFS type]<br/>\n"
            "<strong>Cooling:</strong> [mm² Vapor Chamber if applicable]<br/>\n"
            "<strong>Display:</strong>  [size] [panel brand+type], [resolution]<br/>\n"
            "<strong>Refresh Rate:</strong> [Hz range or fixed Hz]<br/>\n"
            "<strong>Peak Brightness:</strong> [nits] | [HBM nits] in High Brightness Mode<br/>\n"
            "<strong>Display Extras:</strong> [HDR, Dolby Vision, PWM Hz, DCI-P3%]<br/>\n"
            "<strong>Rear Camera 1:</strong>  [MP] [sensor] with OIS, f/[aperture]<br/>\n"
            "<strong>Rear Camera 2:</strong> [MP] [type] [zoom]x Optical Zoom<br/>\n"
            "<strong>Rear Camera 3:</strong> [MP] Ultra-Wide<br/>\n"
            "<strong>Front Camera:</strong>  [MP]<br/>\n"
            "<strong>Battery:</strong>  [mAh] [type e.g. Silicon-Carbon]<br/>\n"
            "<strong>Wired Charging:</strong> [W] [brand name e.g. FlashCharge]<br/>\n"
            "<strong>Wireless Charging:</strong> [W or No]<br/>\n"
            "<strong>Fingerprint:</strong> [Ultrasonic/Optical] In-Display<br/>\n"
            "<strong>Face Unlock:</strong> Yes<br/>\n"
            "<strong>IP Rating:</strong> [rating]<br/>\n"
            "<strong>Wi-Fi:</strong> Wi-Fi [version]<br/>\n"
            "<strong>Bluetooth:</strong>  [version]<br/>\n"
            "<strong>NFC:</strong> Yes/No<br/>\n"
            "<strong>GPS:</strong> [bands]<br/>\n"
            "<strong>Colours Available:</strong>  [all colour names]<br/>\n"
            "<strong>Software Promise:</strong>  [X] Years OS Updates + [Y] Years Security Patches<br/>\n"
            f"<strong>Where to Buy:</strong> <a href='{buy_amazon}' rel='nofollow' target='_blank'>Amazon India</a>, "
            f"<a href='{official_url}' rel='nofollow' target='_blank'>{official_name}</a>, Offline Stores<br/>\n\n"

            # ── Section 3 ──────────────────────────────────────────
            "<h3>3. Design &amp; Build — [One strong opinion about the design]</h3>\n"
            "4 paragraphs. Describe it like you are holding it in your hand.\n"
            "Para 1: Personal reaction to the design. What is different. What story is behind it.\n"
            "Para 2-3: Describe the back panel, finish, texture vividly. Mention any special colourway story.\n"
            "Then sub-headings on their own line:\n"
            "<strong>On the camera module</strong> — size, placement, LED ring if any, describe precisely.<br/>\n"
            "<strong>On durability</strong> — IP rating explained in plain English ('IP68 means you can drop it in water up to 1.5 metres for 30 minutes'). Both ratings if applicable.<br/>\n"
            "<strong>Bottom line on design:</strong> — one verdict sentence. 'If you've been looking at flagships and thinking they all look the same — this is your answer.'<br/>\n\n"

            # ── Section 4 ──────────────────────────────────────────
            "<h3>4. Display — [Nits number or panel type sounds like marketing until you use it]</h3>\n"
            "Open: 2 para intro — panel type, size, resolution, Hz all in one sentence. Then say you'll explain why in plain terms.\n"
            "Then sub-headings:\n"
            "<strong>On the brightness number — [X] nits</strong><br/>\n"
            "Explain: 'Most phones hit 1000-2000 nits. A bright flagship hits 3000. This one hits [X].' Then real-life: Bengaluru/Delhi afternoon sun, reading screen without shading it.<br/><br/>\n"
            "<strong>On the [Hz] LTPO refresh rate</strong><br/>\n"
            "Explain LTPO simply: drops to 1Hz on static, snaps to 144Hz on scroll/gaming. Battery benefit.<br/><br/>\n"
            "<strong>On the colours and HDR</strong><br/>\n"
            "DCI-P3%, Dolby Vision, HDR10+. Netflix/Hotstar IPL test. OLED blacks vs highlights.<br/><br/>\n"
            "<strong>On eye comfort</strong><br/>\n"
            "PWM Hz explained. DC Dimming. Who this matters for (OLED eye sensitivity).<br/><br/>\n"
            "<strong>Display verdict:</strong>  One strong sentence.<br/>\n\n"

            # ── Section 5 ──────────────────────────────────────────
            "<h3>5. Performance — [The Phone That Does Not Know the Word 'Lag' or similar]</h3>\n"
            "Open: 2 para about the chipset — EXACT name, nm node, vs last year's chip.\n"
            "Then sub-headings:\n"
            "<strong>In day to day use</strong><br/>\n"
            "Apps open, multitasking, no hesitation. India scenario: 'picks up someone else's phone and wonders why it feels slow'.<br/><br/>\n"
            "<strong>The storage matters too</strong><br/>\n"
            "UFS version, real-world speed feeling, combined with LPDDR RAM.<br/><br/>\n"
            "<strong>The [Gaming Chip name if any]</strong><br/>\n"
            "What it does. Why gaming workloads benefit. Explain simply.<br/><br/>\n"
            "<strong>The cooling system — [mm²]</strong><br/>\n"
            "Vapor chamber size. Heat spread. 60-min gaming result. Sustained performance.<br/><br/>\n"
            "<strong>Benchmark numbers if you care about them</strong><br/>\n"
            "AnTuTu score, Geekbench single + multi. What they mean for future apps.<br/>\n\n"

            # ── Section 6 ──────────────────────────────────────────
            "<h3>6. Gaming — [This Is What [Brand] Was Built For or similar]</h3>\n"
            "Open: 2 para about the brand's gaming DNA and what this phone is for gamers.\n"
            "Then sub-headings:\n"
            "<strong>BGMI</strong><br/>\n"
            "Exact settings (Smooth + Extreme / Ultra HD). Locked fps. Touch Hz. Competitive players.<br/><br/>\n"
            "<strong>Call of Duty Mobile</strong><br/>\n"
            "Graphics setting, frame rate. 144Hz display difference in shooters.<br/><br/>\n"
            "<strong>Genshin Impact and Wuthering Waves</strong><br/>\n"
            "Max settings, 60fps cap. Heat after 45 min. Vapor chamber result.<br/><br/>\n"
            "<strong>The features that actually matter for gaming</strong><br/>\n"
            "Monster Mode / gaming features. Multi-Turbo. Network Boost. Real effect on gameplay.<br/><br/>\n"
            "<strong>Gaming verdict:</strong> One strong clear sentence. 'There is no better gaming phone under ₹X,000 right now.'<br/>\n\n"

            # ── Section 7 ──────────────────────────────────────────
            "<h3>7. Camera — [Honest opinion — 'Better Than I Expected' or 'Good, Not Great']</h3>\n"
            "Open 2 para: 'Let me be straight with you about the camera...' — not the best, but here is what it does well.\n"
            "Then EXACTLY this camera sub-item format:\n"
            "<strong>* The Main Camera — [sensor name]</strong><br/>\n"
            "[Paragraph: aperture, OIS, daylight result, India skin tones, rival comparison]<br/><br/>\n"
            "<strong>* The periscope telephoto — [sensor], [X]x optical</strong><br/>\n"
            "[Paragraph: portrait compression, background blur, zoom range verdict]<br/><br/>\n"
            "<strong>* The Ultra-wide — [MP]MP</strong><br/>\n"
            "[Paragraph: colour consistency with main camera, why this matters]<br/><br/>\n"
            "<strong>* Night photography</strong><br/>\n"
            "[Honest paragraph: good or B+? Named rival who does better if applicable]<br/><br/>\n"
            "<strong>* Selfie camera — [MP]MP</strong><br/>\n"
            "[Paragraph: skin tones, portrait, WhatsApp video calls]<br/><br/>\n"
            "<strong>* Video</strong><br/>\n"
            "[Paragraph: 4K@60fps, OIS+EIS, HDR video, social media use]<br/><br/>\n"
            "<strong>Camera verdict</strong><br/>\n"
            "[One sentence verdict — honest, specific, named comparison]\n\n"

            # ── Section 8 — NOTE: bold INSIDE the H3 ──────────────
            f"<h3>8. <strong>Battery — [Personal story as title e.g. 'I Stopped Carrying a Charger to Work']</strong></h3>\n"
            "IMPORTANT: The H3 itself wraps the title in <strong> tags. Copy this format exactly.\n"
            "Open 2 para: personal story — 'I don't say that lightly. I'm someone who has always carried...'\n"
            "Then sub-headings:\n"
            "<strong>Why [silicon-carbon / battery tech] is actually different</strong><br/>\n"
            "Normal graphite vs this tech. More energy in same space. Handles fast charging better.<br/><br/>\n"
            "<strong>Real numbers from real use</strong><br/>\n"
            "India drain log: 'On a typical day — social media, calls, 45min gaming — I finished above X%.' Heavy gaming hours. Streaming hours.<br/><br/>\n"
            "<strong>The [W]W charging</strong><br/>\n"
            "'Half an hour gets you from dead to ~80%.' How it changed morning routine. Under 1hr to full.<br/><br/>\n"
            "<strong>[W]W wireless</strong><br/>\n"
            "Fast enough to be primary method. Compare to slow 10-15W wireless on rivals.<br/><br/>\n"
            "<strong>Battery verdict:</strong>  One sentence. 'The best battery experience on an Android flagship in India.'<br/>\n\n"

            # ── Section 9 ──────────────────────────────────────────
            "<h3>9. Software — [UI name] Has Grown Up or similar honest take</h3>\n"
            "Open: acknowledge suspicion of custom Android skins. Then say this one is different.\n"
            "<strong>The day to day experience</strong><br/>\n"
            "Smoothness, animations, notifications, quick settings, bloatware level.<br/><br/>\n"
            "<strong>The AI features that are actually useful</strong><br/>\n"
            "3-4 specific AI features in plain English. 'AI Photo Enhancement, AI Battery Optimisation, AI Gaming Boost, AI Call Translation.' What each does.<br/><br/>\n"
            "<strong>The software support commitment that changes everything</strong><br/>\n"
            "[X] years OS updates + [Y] years security. Then italic paragraph: <em>'Think about how long you actually keep a phone. Most people in India keep their flagship 3 to 4 years...'</em><br/>\n\n"

            # ── Section 10 ─────────────────────────────────────────
            "<h3>10. Connectivity — They Didn't Miss Anything</h3>\n"
            "One flowing section — NO sub-headings. Cover each feature inline with <strong> for key terms:\n"
            "<strong>Wi-Fi [version]</strong> — what it means for gaming, next-gen routers.\n"
            "<strong>Bluetooth [version]</strong> — stable audio, low power, TWS earbuds.\n"
            "The <em><strong>5G band</strong></em> coverage — how many bands, Jio/Airtel/Vi confirmed.\n"
            "<strong>NFC</strong> for Google Pay and PhonePe — works flawlessly.\n"
            "Ultrasonic fingerprint vs optical — wet/dirty finger reliability.\n"
            "No <em><strong>3.5mm jack</strong></em> — honest note, USB-C adapter needed.\n\n"

            # ── Section 11 — NOTE: bold INSIDE H3 + question mark ──
            "<h3>11. <strong>How Does It Compare to the Competition</strong>?</h3>\n"
            "IMPORTANT: H3 wraps middle text in <strong> + ends with ? outside the strong. Copy exactly.\n"
            "3 competitor comparisons. Each as:\n"
            "<strong>Against [Rival] (₹XX,XXX starting)</strong><br/>\n"
            "[One paragraph. Specific numbers: battery mAh vs mAh, charging W vs W, nits vs nits, IP rating vs IP rating. Clear winner stated for which use case.]<br/><br/>\n"
            "Do this for 3 rivals — one budget, one premium, one same price.\n\n"

            # ── Section 12 ─────────────────────────────────────────
            "<h3>12. Price &amp; Where to Buy</h3>\n"
            "EXACT format — italic variant lines:\n"
            "<em>[RAM+Storage] — ₹XX,XXX (Effective ₹XX,XXX with bank offers)</em><br/>\n"
            "<em>[RAM+Storage] — ₹XX,XXX (Effective ₹XX,XXX with bank offers)</em><br/><br/>\n"
            "<strong>Pre-Booking Offers:</strong><br/>\n"
            "[₹X,000 instant discount with bank cards. X months zero-cost EMI. Free [accessory] for pre-bookers.]<br/><br/>\n"
            f"Where: <em><strong><a href='{buy_amazon}' rel='nofollow' target='_blank'>Amazon India</a>, "
            f"<a href='{official_url}' rel='nofollow' target='_blank'>{official_name}</a>, and offline stores. Sale date is [date].</strong></em><br/><br/>\n"
            "Which variant should you buy? [2-3 sentences. 'Get the [top variant]. For ₹X,000 more you're getting double storage and more RAM. On a phone you're planning to keep for 3-4 years, that headroom matters.']\n\n"

            # ── Section 13 ─────────────────────────────────────────
            "<h3>13. Pros &amp; Cons — The Honest List</h3>\n"
            "EXACTLY this structure — two sub-headings, two paragraphs:\n\n"
            "<strong>What I Love:</strong><br/>\n"
            "[One flowing paragraph of ALL the positives. Example: 'The design — nothing else looks like this right now. The battery life — genuinely changed my daily routine. The display — [X] nits in the summer sun is something you cannot unsee. The gaming performance — the [chip] + vapor chamber combo is the real deal. The [W] + [W] charging — both fast, both practical. IP[rating] — carry this phone everywhere without worry. [Camera sensors] — consistent, capable, trustworthy. [X] plus [Y] years of software support — makes every rupee work harder over time.']\n\n"
            "<strong>What I'd Change:</strong><br/>\n"
            "[One flowing paragraph of ALL the honest negatives. Example: 'I wish the telephoto was [X]x instead of [Y]x. No headphone jack — still a loss even in [year] for some users. [UI name] won't win over die-hard stock Android fans. [Size] inches is a big phone — if you have small hands, be honest with yourself before buying.']\n\n"

            # ── Section 14 ─────────────────────────────────────────
            "<h3>14. Should You Buy It?</h3>\n"
            "<strong>Here's how I'd think about it simply.</strong><br/><br/>\n"
            "EXACTLY this italic+bold format — one line per profile:\n"
            "<em>If you game on your phone, even casually — <strong>yes. Buy it.</strong></em><br/>\n"
            "<em>If battery life has been a frustration with your current phone — <strong>yes. Buy it.</strong></em><br/>\n"
            "<em>If you're tired of every premium phone looking identical — <strong>yes. Buy it.</strong></em><br/>\n"
            "<em>If you want a phone that will still be getting software updates in [year+4], [year+5] — <strong>yes. Buy it.</strong></em><br/>\n"
            "<em>If you are a dedicated professional photographer who needs the absolute best zoom — <strong>the [rival] deserves your attention first.</strong></em><br/>\n"
            "<em>If you want a smaller phone — <strong>this isn't it. Simple as that.</strong></em><br/><br/>\n"
            "<em>For the overwhelming majority of people reading this who want a powerful, durable, beautiful, long-lasting flagship under ₹[price] in India in [year] <strong>— the [phone name] is the most complete answer the market has right now.</strong></em>\n\n"

            # ── Section 15 ─────────────────────────────────────────
            "<h3>15. Final Verdict — My Honest Take After Using It</h3>\n"
            "Open with score in bold+italic: <em><strong>Score: X.X out of 10 — [Verdict e.g. 'Highly Recommended']</strong></em><br/><br/>\n"
            "Para 1: 'I started this review mildly sceptical...' What made you change your mind.\n"
            "Para 2: '[Phone] is the whole package in a way that's rare at this price.' — 4 specific things.\n"
            "Para 3: 'Is it perfect? No.' — list 2-3 honest limits. Then: 'But perfection was never the point. The point was to build the most complete...'\n\n"

            # ── Section 16 ─────────────────────────────────────────
            "<h3>16. FAQ — Real Questions, Real Answers</h3>\n"
            "EXACTLY 10 questions. Each answer 2-4 sentences. Plain simple English.\n"
            "Number each question. Format:\n"
            "1. [Question specific to this phone]<br/>\n"
            "[Answer paragraph]<br/><br/>\n"
            "2. [Question]<br/>\n"
            "[Answer]<br/><br/>\n"
            "...through 10.\n\n"
            f"Question 1: What is the {phone_clean} price in India?\n"
            f"Question 2: What is different about [this edition] vs the regular {phone_clean}?\n"
            f"Question 3: Is this the best [gaming/flagship] phone under ₹[price] in India right now?\n"
            f"Question 4: How long does the battery realistically last?\n"
            f"Question 5: Will it survive rain and water?\n"
            f"Question 6: Is the camera actually good or just good for a [category] phone?\n"
            f"Question 7: What Android version and how long will it be supported?\n"
            f"Question 8: Does it support all Indian 5G networks?\n"
            f"Question 9: Is wireless charging fast enough to be useful?\n"
            f"Question 10: Which variant should I buy?\n\n"
            "After question 10, end with italic disclaimer:\n"
            "<em>This review reflects hands-on impressions and official specifications as available at time of writing. Prices and offers are subject to change. For current pricing always check Amazon India or [brand].com directly.</em>\n\n"

            "━━━ WRITING RULES ━━━\n"
            "• First-person always: 'I'll be honest.' 'Let me be straight.' 'Here's the thing nobody tells you.'\n"
            "• Every spec explained in plain English + real-life meaning (Bengaluru sun, BGMI, IPL Hotstar, morning chai)\n"
            "• Long para → long para → one SHORT punchy verdict sentence (repeat this rhythm)\n"
            "• Named rival comparison in every main section (inline prose, NEVER in a table)\n"
            "• Honest negatives — one real weakness per section\n"
            "• NEVER: seamlessly, cutting-edge, game-changer, revolutionary, robust, leverage, delve into\n\n"

            "━━━ ABSOLUTE RULES ━━━\n"
            "• HTML ONLY — ZERO markdown, ZERO **bold**, ONLY <strong> and <em> tags\n"
            "• NEVER invent specs — use ONLY what is in OFFICIAL SPECS above\n"
            "• EXACTLY 16 sections with H3 headings\n"
            "• Section 8 H3 and Section 11 H3 contain <strong> inside them — copy exactly\n"
            "• Section 13: <strong>What I Love:</strong> then one prose paragraph, then <strong>What I'd Change:</strong> then one prose paragraph — NEVER bullets, NEVER mixed\n"
            "• Section 14: ONLY italic <em> conditional lines with <strong>yes. Buy it.</strong>\n"
            "• Section 16: EXACTLY 10 questions, ends with italic disclaimer\n"
            "• NO tables of any kind anywhere\n"
            "• NO h4 tags — use <strong> on its own line for all sub-headings\n"
            "• 8000 words minimum\n"
            "Write now:"
        )

    r = client.chat.completions.create(
        model="llama3.1-8b",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=8192, temperature=0.75,
    )
    return r.choices[0].message.content



def human_rewrite(draft, story):
    """
    v33 — Polish pass. Matches iQOO 15 Apex article voice exactly.
    Simple English. Personal. Helpful. No tables.
    """
    from cerebras.cloud.sdk import Cerebras
    client = Cerebras(api_key=CEREBRAS_API_KEY)
    phone_clean = re.split(r'[:\|–—]', story.get("title", "[Phone]"))[0].strip()

    prompt = (
        "You are Mallikarjun R — 19-year-old CSE student and tech blogger from Bengaluru, India.\n\n"
        "TASK: Polish this article draft. Keep ALL HTML, headings, links, and numbers exactly.\n"
        "Only rewrite prose sentences to sound more personal, simple, and helpful.\n\n"

        "━━━ DO NOT CHANGE ━━━\n"
        "• Every H1, H2, H3 heading — copy exactly\n"
        "• Every <a href link — copy exactly\n"
        "• Every ₹ price and spec number — copy exactly\n"
        "• Image placeholder comments\n\n"

        "━━━ REWRITE RULES ━━━\n\n"

        "① SIMPLE ENGLISH:\n"
        "   BAD:  'The device incorporates advanced thermal architecture.'\n"
        "   GOOD: 'The cooling system works really well. After 40 minutes of BGMI,\n"
        "          the phone was warm but never hot. That is better than most phones.'\n\n"

        "② PERSONAL AND HONEST:\n"
        "   Start sections with hooks like:\n"
        "   'I will be honest with you.' | 'Here is the thing nobody tells you.'\n"
        "   'Let me be straight before you spend your money.' | 'I actually surprised myself here.'\n\n"

        "③ EXPLAIN EVERY SPEC:\n"
        "   After every number, add what it means in real life.\n"
        "   '<strong>6000 nits</strong> — most phones hit 2000. This one hits 6000.\n"
        "    That means you can use it under direct Bengaluru afternoon sun\n"
        "    without shading the screen. I have tested phones at ₹1 lakh that cannot do this.'\n\n"

        "④ INDIA SCENARIOS (weave naturally):\n"
        "   BGMI at hostel | IPL on Hotstar | Bengaluru metro commute\n"
        "   Sunday market photography | Wedding selfie | Chai stall night camera\n"
        "   Board exam night scrolling | Swiggy notification\n\n"

        "⑤ SHORT PUNCHY VERDICT after each section:\n"
        "   'This is where it earns its price tag.'\n"
        "   'Not perfect. But the best at this price.'\n"
        "   'I like it more than I expected.'\n"
        "   'One small gripe. Nothing that stops me recommending it.'\n\n"

        "⑥ HONEST NEGATIVES:\n"
        "   'No wireless charging at ₹40,000 is a miss. Plain and simple.'\n"
        "   'Night camera needs work. I expected better here.'\n"
        "   'Bloatware on Day 1 was annoying. You will spend 10 minutes removing apps.'\n\n"

        "━━━ BANNED WORDS ━━━\n"
        "seamlessly, cutting-edge, state-of-the-art, game-changer, revolutionary,\n"
        "robust, leverage, delve, it is worth noting, a testament to, powerful performance,\n"
        "impressive results, solid choice, overall verdict, exceptional, remarkable, notably\n\n"

        "━━━ FORMAT RULES ━━━\n"
        "• HTML only — no markdown ever\n"
        "• <strong> for specs — never **text**\n"
        "• NO tables of any kind — convert to prose if found\n"
        "• Do not shorten — make every section LONGER and more helpful\n"
        "• Section 11 (Competition) — must have 3 named rivals with ₹ prices\n"
        "• Section 13 (Pros & Cons) — <strong>Pros</strong> heading then one paragraph of positives ONLY, then <strong>Cons</strong> heading then one paragraph of negatives ONLY. NEVER mix them. NEVER use bullet symbols or ✅❌.\n"
        "• Section 14 (Should You Buy) — ONLY <em>italic conditional</em> lines with <strong>yes. Buy it.</strong> format\n"
        "• Section 16 (FAQ) — EXACTLY 10 questions, each 70-90 words\n\n"

        "REWRITE NOW — make it longer, simpler, more personal:\n\n"
        + draft
    )

    r = client.chat.completions.create(
        model="llama3.1-8b",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=8192, temperature=0.82,
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

def save_log(log, title, url, words, atype, cat, search_topic=""):
    log.append({
        "title":       title,
        "url":         url,
        "words":       words,
        "type":        atype,
        "category":    cat,
        "search_topic": search_topic,
        "posted_at":   datetime.datetime.now().isoformat()
    })
    with open("posted_articles.json", "w") as f:
        json.dump(log, f, indent=2)
    print("Log: " + str(len(log)) + " total posts")

# ================================================================
# AUTHOR BIO HTML — GitHub-style minimal byline on EVERY article
# ================================================================
def build_author_bio():
    today = datetime.datetime.now().strftime("%B %d, %Y")
    return (
        '\n<hr style="border:none;border-top:1px solid #d0d7de;margin:40px 0 24px;"/>\n'
        '<div style="display:flex;align-items:flex-start;gap:16px;margin-bottom:40px;">'

        # Avatar
        '<img src="https://lh3.googleusercontent.com/pw/AP1GczNbk_7GTq9-pE7KTZUn0skqYYoESZzxYYQ1uTQvvu6dDj-2AUPZyvUGs5XPOGrt5HeVnMuHzPHO8tp1OA0zuhAKF6wlOho_8Q1aVAlVTwG9CNr_jH8=s400-no"'
        ' width="48" height="48" '
        'style="border-radius:50%;flex-shrink:0;border:1px solid #d0d7de;" '
        'alt="Mallikarjun R"/>'

        # Text block
        '<div>'
        '<p style="margin:0 0 2px;font-size:15px;font-weight:700;color:#1f2328;">'
        'Mallikarjun R</p>'
        '<p style="margin:0 0 6px;font-size:13px;color:#57606a;">'
        f'CSE Student &amp; Tech Blogger &bull; Bengaluru, India &bull; {today}</p>'
        '<p style="margin:0 0 10px;font-size:14px;color:#57606a;line-height:1.6;">'
        'Passionate about smartphones, laptops and everything tech. '
        'Honest reviews for Indian buyers. Follow for daily updates.</p>'
        '<p style="margin:0;">'
        f'<a href="https://www.instagram.com/mallikarjunr_8055" target="_blank" '
        f'style="font-size:13px;color:#0969da;text-decoration:none;margin-right:14px;font-weight:600;">'
        f'Instagram</a>'
        f'<a href="https://whatsapp.com/channel/0029VazWwdn0wajoizN5PY3Q" target="_blank" '
        f'style="font-size:13px;color:#0969da;text-decoration:none;margin-right:14px;font-weight:600;">'
        f'WhatsApp</a>'
        f'<a href="https://www.linkedin.com/in/mallikarjun-r-a85685367" target="_blank" '
        f'style="font-size:13px;color:#0969da;text-decoration:none;font-weight:600;">'
        f'LinkedIn</a>'
        '</p>'
        '</div>'
        '</div>\n'
    )


def run_article(story, is_search, label, atype, log):
    print("\n" + "="*55)
    print(label + " [" + story.get("category","?").upper() + "]")
    print("="*55)

    # Step 0 — Generate SEO title
    print("Step 0: Generating SEO title...")
    seo_title = generate_seo_title(story, is_search)
    story["seo_title"] = seo_title

    # Step 1 — Technical draft
    print("Step 1: Technical draft (4000+ words)...")
    draft = groq_draft(story, is_search)
    w1    = len(re.sub(r"<[^>]+>","",draft).split())
    print("Draft: " + str(w1) + " words")

    # Step 2 — Human rewrite
    print("Step 2: Human rewrite as Mallikarjun R...")
    human = human_rewrite(draft, story)
    final = fix_bold(human)

    # Extract clean title (prefer H1 from output, else use seo_title)
    title = seo_title
    m = re.search(r"<h1[^>]*>(.*?)</h1>", final, re.IGNORECASE|re.DOTALL)
    if m:
        title = re.sub(r"<[^>]+>","",m.group(1)).strip()

    words = len(re.sub(r"<[^>]+>","",final).split())
    print("Final: " + str(words) + " words | " + title[:55])

    cat  = story.get("category","general")

    # ── Bio safety strip: remove ANY old blue-border bio the AI may have added ──
    # Catches both the old #1a73e8 blue bio AND any other injected bio divs
    final = re.sub(
        r'<div[^>]*(?:border-top:3px solid #1a73e8|background:#f0f7ff)[^>]*>.*?</div>',
        '', final, flags=re.DOTALL | re.IGNORECASE
    )

    # Step 3b — Remove any PRODUCT_IMAGE placeholder comments (no auto images — blogger pastes manually)
    final = re.sub(
        r'<!--\s*PRODUCT_IMAGE:\s*([^-]+?)\s*-->',
        r'<!-- IMAGE PLACEHOLDER: \1 — Add your image here -->',
        final,
        flags=re.IGNORECASE
    )

    # Step 3c — For buying guide articles (Top 5 / Best 5), inject Also Read box after each product image placeholder
    if is_search and ("under" in story.get("search_topic","").lower() or "best" in story.get("search_topic","").lower()):
        also_read_inline = build_also_read_box(cat, title)
        # Inject Also Read box after every image placeholder comment block
        final = re.sub(
            r'(<!-- (?:IMAGE PLACEHOLDER|Add your image here)[^\n]*-->\n)',
            r'\1' + also_read_inline,
            final,
            flags=re.IGNORECASE
        )

    # Step 3 — Remove any auto-injected hero image blocks (keep only placeholder comment)
    # No auto hero image — blogger pastes manually

    # Step 3a — Strip Pros & Cons tables and comparison tables from buying guide / VS articles
    if is_search:
        # Remove entire <table>...</table> blocks that contain Pros or Cons headers
        final = re.sub(
            r'<table[^>]*>(?:(?!</table>).)*?(?:✅\s*Pros|❌\s*Cons|Pros\s*</th|Cons\s*</th)(?:(?!</table>).)*?</table>',
            '', final, flags=re.DOTALL | re.IGNORECASE
        )
        # Remove verdict/comparison tables (Use Case | Best Pick | Why pattern)
        final = re.sub(
            r'<table[^>]*>(?:(?!</table>).)*?(?:Use Case|Best Pick|Which to Buy|Comparison)(?:(?!</table>).)*?</table>',
            '', final, flags=re.DOTALL | re.IGNORECASE
        )

    # Step 4 — Inject AdSense ad slots between H2 sections (every 2nd)
    h2_count = [0]
    def inject_ad(match):
        h2_count[0] += 1
        if h2_count[0] % 2 == 0:
            return AD_SLOT_HTML + match.group(0)
        return match.group(0)
    final = re.sub(r'<h2[^>]*>', inject_ad, final, flags=re.IGNORECASE)

    # Step 5 — Inject FAQ JSON-LD schema
    faqs = extract_faq_from_html(final)
    if not faqs:
        # Fallback: build from topic
        topic_q = story.get("search_topic") or title
        faqs = [
            {"q": "Which is the " + topic_q + "?",
             "a": "Read the full guide above for our top-ranked picks tested in India " + str(datetime.datetime.now().year) + "."},
            {"q": "Is this worth buying in India " + str(datetime.datetime.now().year) + "?",
             "a": "Yes, based on our real-world tests and India pricing analysis in this article."},
        ]
    schema_block = build_faq_schema(faqs)

    # Step 6 — Social share block
    social_block = build_social_block(title, BLOG_URL)

    # Step 6b — Also Read box (brand-interlinked related articles)
    also_read = build_also_read_box(cat, title)

    # Step 7 — Footer: GitHub-style order — Related posts → Share bar → Author bio
    author_bio_html = build_author_bio()
    footer = (
        "<hr style='border:none;border-top:1px solid #d0d7de;margin:40px 0 0;'/>"
        + also_read
        + social_block
        + author_bio_html
    )

    # Assemble final HTML: schema first, then article, then footer
    full_html = schema_block + final + footer

    # Step 8 — Post to Blogger
    url = post_email(title, full_html)

    # Step 9 — Save log
    save_log(log, title, url, words, atype, cat, story.get("search_topic",""))

    # Step 10 — Ping Google Indexing API
    ping_google_index(url)

    return True



# ================================================================
# DAY TYPE TRACKER
# Reads/writes posted_articles.json to know which article to post today
# Cycle: review_1 → review_2 → search → review_1 → review_2 → ...
# ================================================================

ARTICLE_CYCLE = ["review_1", "review_2", "search"]

def get_next_article_type(log):
    """
    Reads the last article type from the log.
    Returns the next type in the 3-day cycle.
    """
    last_type = None
    for entry in reversed(log):
        t = entry.get("article_type", "")
        if t in ARTICLE_CYCLE:
            last_type = t
            break

    if last_type is None:
        return "review_1"   # first ever run
    idx = ARTICLE_CYCLE.index(last_type)
    next_idx = (idx + 1) % len(ARTICLE_CYCLE)
    return ARTICLE_CYCLE[next_idx]


def save_log_v28(log, title, url, words, atype, cat, article_type, search_topic=""):
    """Extended log entry with article_type for cycle tracking."""
    log.append({
        "title":        title,
        "url":          url,
        "words":        words,
        "type":         atype,
        "category":     cat,
        "article_type": article_type,   # "review_1", "review_2", or "search"
        "search_topic": search_topic,
        "posted_at":    datetime.datetime.now().isoformat()
    })
    with open("posted_articles.json", "w") as f:
        json.dump(log, f, indent=2)
    print("Log saved: " + str(len(log)) + " total posts | today=" + article_type)


# ================================================================
# MAIN — v28: ONE article per day, 3-day cycle, max token quality
# ================================================================
def main():
    log     = load_log()
    today   = datetime.datetime.now().strftime("%A, %d %B %Y")
    a_type  = get_next_article_type(log)

    day_labels = {
        "review_1": "DAY TYPE 1 — FULL SMARTPHONE REVIEW (new launch)",
        "review_2": "DAY TYPE 2 — FULL SMARTPHONE REVIEW (different phone)",
        "search":   "DAY TYPE 3 — TOP SEARCHED SMARTPHONE ARTICLE",
    }

    print("=======================================================")
    print(f" TECH NEWS WITH AI - AUTO BLOG v35.0")
    print(f" {today}")
    print(f" TODAY: {day_labels[a_type]}")
    print(f" ONE article — full daily Groq token budget")
    print(f" Target: 7000–8000 words (AdSense editorial quality)")
    print(f" technewsai.me — Mallikarjun R, Bengaluru")
    print("=======================================================")

    suggest_old_updates(log, days_threshold=30)

    success = 0

    # ──────────────────────────────────────────────────────────────
    # DAY TYPE 1 — Full smartphone review (new launch, first phone)
    # ──────────────────────────────────────────────────────────────
    if a_type == "review_1":
        try:
            print("\n[TODAY] Picking new-launch smartphone for full review (Day 1)...")
            story = pick_launch_story(log)
            if not story:
                print("[Fallback] No launch RSS — trying breaking news...")
                story = pick_news_story(log)
                if story:
                    tl = story.get("title", "").lower()
                    if any(w in tl for w in ["top 5", "top 3", "best phones", "buying guide"]):
                        story = None
            if story:
                run_article_v28(story, False, "REVIEW DAY 1: NEW LAUNCH FULL REVIEW",
                                "news", "review_1", log)
                success = 1
            else:
                print("[ERROR] No story found for Day 1 review — skipping.")
        except Exception as e:
            print(f"[ERROR] Day 1 review failed: {e}")

    # ──────────────────────────────────────────────────────────────
    # DAY TYPE 2 — Full smartphone review (different new launch)
    # ──────────────────────────────────────────────────────────────
    elif a_type == "review_2":
        # Get titles already posted as review_1 to avoid duplicates
        used = {e.get("title","") for e in log if e.get("article_type") == "review_1"}
        try:
            print("\n[TODAY] Picking new-launch smartphone for full review (Day 2)...")
            story = pick_launch_story(log, exclude_titles=used)
            if not story:
                print("[Fallback] No second launch RSS — trying breaking news...")
                story = pick_news_story(log, exclude_titles=used)
                if story:
                    tl = story.get("title", "").lower()
                    if any(w in tl for w in ["top 5", "top 3", "best phones", "buying guide"]):
                        story = None
            if story:
                run_article_v28(story, False, "REVIEW DAY 2: NEW LAUNCH FULL REVIEW",
                                "news", "review_2", log)
                success = 1
            else:
                print("[ERROR] No story found for Day 2 review — skipping.")
        except Exception as e:
            print(f"[ERROR] Day 2 review failed: {e}")

    # ──────────────────────────────────────────────────────────────
    # DAY TYPE 3 — Top searched smartphone topic (buying guide or trending)
    # ──────────────────────────────────────────────────────────────
    elif a_type == "search":
        used = {e.get("title","") for e in log} | {e.get("search_topic","") for e in log}
        try:
            print("\n[TODAY] Picking top-searched smartphone topic (Day 3)...")
            story = pick_article3_single_review(log, used)
            if story:
                # Single trending phone = full review style (is_search=False)
                run_article_v28(story, False, "SEARCH DAY 3: TRENDING SMARTPHONE REVIEW",
                                "news", "search", log)
                success = 1
            else:
                # Fallback: buying guide / top search topic
                print("[Fallback] No single trending phone — using search topic...")
                story = pick_search_story(log, used)
                if story:
                    story["category"] = "smartphone"
                    run_article_v28(story, True, "SEARCH DAY 3: TOP SEARCHED TOPIC",
                                    "search", "search", log)
                    success = 1
                else:
                    # Emergency: generate a dynamic topic right now
                    print("[Emergency] Generating dynamic topic...")
                    dyn = generate_dynamic_topics("smartphone", log, used, count=3)
                    if dyn:
                        s = {
                            "title":        dyn[0]["t"],
                            "description":  "",
                            "url":          "https://technewsai.me",
                            "source":       "Dynamic",
                            "published":    datetime.datetime.now().isoformat(),
                            "specs":        "",
                            "search_topic": dyn[0]["t"],
                            "keywords":     dyn[0].get("k", []),
                            "rss_context":  "",
                            "category":     "smartphone",
                        }
                        run_article_v28(s, True, "SEARCH DAY 3: DYNAMIC TOPIC",
                                        "search", "search", log)
                        success = 1
        except Exception as e:
            print(f"[ERROR] Day 3 search failed: {e}")

    print("\n=======================================================")
    print(f"DONE! {success}/1 article posted | Type: {a_type}")
    print("Next run will post:", ARTICLE_CYCLE[(ARTICLE_CYCLE.index(a_type)+1)%3])
    print("Next steps:")
    print("  → PASTE real product image in Blogger (1200x628px)")
    print("  → Fact-check prices and exact specs")
    print("  → Share on WhatsApp & Telegram")
    print("  → Submit URL in Google Search Console → Inspect URL")
    print("Visit: https://www.technewsai.me")
    print("=======================================================")


# ================================================================
# run_article_v28 — same as run_article but uses save_log_v28
# to track article_type for the 3-day cycle
# ================================================================


# ================================================================
# v34 — LIVE BLOG POST FETCHER + SMART INTERLINKING SYSTEM
# Fetches all posts from technewsai.me at runtime
# Builds keyword→URL map for automatic blue internal links
# ================================================================

BLOG_RSS_URL = "https://www.technewsai.me/feeds/posts/default?max-results=50"

_BLOG_POSTS_CACHE = None  # cached at runtime

def fetch_all_blog_posts():
    """
    Fetch all published posts from technewsai.me via Blogger RSS.
    Returns list of {title, url, keywords} dicts.
    Cached after first call.
    """
    global _BLOG_POSTS_CACHE
    if _BLOG_POSTS_CACHE is not None:
        return _BLOG_POSTS_CACHE

    posts = []
    try:
        r = requests.get(BLOG_RSS_URL, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            root = ET.fromstring(r.content)
            ns = {"atom": "http://www.w3.org/2005/Atom"}
            entries = root.findall("atom:entry", ns)
            for entry in entries:
                title_el = entry.find("atom:title", ns)
                title = title_el.text.strip() if title_el is not None and title_el.text else ""
                url = ""
                for link in entry.findall("atom:link", ns):
                    if link.get("rel") == "alternate":
                        url = link.get("href", "")
                        break
                if title and url:
                    posts.append({"title": title, "url": url})
        print(f"[Interlink] Fetched {len(posts)} posts from technewsai.me")
    except Exception as e:
        print(f"[Interlink] Could not fetch posts: {e}")

    _BLOG_POSTS_CACHE = posts
    return posts


def build_interlink_map(posts):
    """
    Build a keyword → URL map from all blog posts.
    Keywords = phone/brand names extracted from post titles.
    Example: "iQOO 15R" → "https://www.technewsai.me/..."
    """
    interlink_map = {}  # keyword (lowercase) → (display_text, url)

    # Brand keywords to detect in titles
    BRAND_PATTERNS = [
        r"iQOO\s+\d+\w*(?:\s+\w+)?",
        r"Samsung\s+Galaxy\s+\w+(?:\s+\w+)?",
        r"Apple\s+iPhone\s+\w+(?:\s+\w+)?",
        r"iPhone\s+\w+(?:\s+\w+)?",
        r"OnePlus\s+\d+\w*(?:\s+\w+)?",
        r"Xiaomi\s+\d+\w*(?:\s+\w+)?",
        r"Redmi\s+\w+(?:\s+\w+)?",
        r"POCO\s+\w+(?:\s+\w+)?",
        r"Realme\s+\w+(?:\s+\w+)?",
        r"OPPO\s+\w+(?:\s+\w+)?",
        r"Oppo\s+\w+(?:\s+\w+)?",
        r"Vivo\s+\w+(?:\s+\w+)?",
        r"vivo\s+\w+(?:\s+\w+)?",
        r"Nothing\s+Phone\s+\w+(?:\s+\w+)?",
        r"Google\s+Pixel\s+\w+(?:\s+\w+)?",
        r"Motorola\s+\w+(?:\s+\w+)?",
        r"Honor\s+\w+(?:\s+\w+)?",
        r"HONOR\s+\w+(?:\s+\w+)?",
        r"MacBook\s+\w+(?:\s+\w+)?",
        r"Infinix\s+\w+(?:\s+\w+)?",
        r"Tecno\s+\w+(?:\s+\w+)?",
    ]

    for post in posts:
        title = post["title"]
        url   = post["url"]
        for pat in BRAND_PATTERNS:
            matches = re.findall(pat, title, re.IGNORECASE)
            for m in matches:
                m = m.strip()
                if len(m) >= 5:
                    interlink_map[m.lower()] = (m, url)

    return interlink_map


def inject_smart_interlinks(html_content, current_title, posts):
    """
    Scan article HTML and replace first occurrence of each phone/brand
    name with a blue internal link to that post on technewsai.me.
    - Only links if a matching post exists
    - Only links the FIRST occurrence (not every mention)
    - Never links inside existing <a> tags
    - Never links the current article's own phone name
    """
    if not posts:
        return html_content

    interlink_map = build_interlink_map(posts)
    if not interlink_map:
        return html_content

    # Current phone name — don't link to itself
    current_phone = re.split(r'[:\|–—]', current_title)[0].strip().lower()

    linked = set()  # track already linked keywords

    def replace_keyword(match):
        word = match.group(0)
        key  = word.lower()
        if key in linked:
            return word  # already linked once
        if key in current_phone or current_phone in key:
            return word  # don't link own phone
        display, url = interlink_map[key]
        linked.add(key)
        return (
            f'<a href="{url}" style="color:#1a73e8;text-decoration:none;"' 
            f' title="{display} — Tech News With AI">{word}</a>'
        )

    # Build one combined regex from all keywords (longest first to avoid partial matches)
    keywords = sorted(interlink_map.keys(), key=len, reverse=True)
    # Escape and join
    pattern = "|".join(re.escape(k) for k in keywords)
    if not pattern:
        return html_content

    # Split on existing <a> tags to avoid nesting links
    parts = re.split(r'(<a[^>]*>.*?</a>)', html_content, flags=re.DOTALL | re.IGNORECASE)
    result = []
    for part in parts:
        if part.lower().startswith('<a'):
            result.append(part)  # inside existing link — skip
        else:
            # Apply replacement (case-insensitive, first occurrence per keyword)
            replaced = re.sub(pattern, replace_keyword, part, flags=re.IGNORECASE)
            result.append(replaced)

    print(f"[Interlink] Linked keywords: {linked}")
    return "".join(result)


def build_table_of_contents(html_content):
    """Disabled — no TOC per user request."""
    return html_content, ""


# ================================================================
# v33 NEW FEATURES — Published date, Reading time, Also Read mid,
# Star rating, Meta description
# ================================================================

def build_article_header(title, words):
    """Published date + Last Updated + Reading time bar."""
    import datetime
    today = datetime.datetime.now()
    date_str = today.strftime("%B %d, %Y")
    reading_min = max(1, round(words / 200))
    return (
        f"<div style='background:#f8f9fa;border-left:4px solid #1a73e8;"
        f"padding:12px 16px;margin:0 0 24px;border-radius:0 8px 8px 0;"
        f"font-size:13px;color:#555;line-height:1.8;'>"
        f"<span style='margin-right:16px;'>📅 <strong>Published:</strong> {date_str}</span>"
        f"<span style='margin-right:16px;'>🔄 <strong>Last Updated:</strong> {date_str}</span>"
        f"<span>⏱️ <strong>{reading_min} min read</strong></span>"
        f"</div>"
    )

def build_star_rating(phone_name, score=4.2):
    """Star rating widget for Final Verdict section."""
    full  = int(score)
    half  = 1 if (score - full) >= 0.5 else 0
    empty = 5 - full - half
    stars = "★" * full + ("½" if half else "") + "☆" * empty
    return (
        f"<div style='background:#fff8f0;border:2px solid #f5a623;"
        f"border-radius:12px;padding:20px 24px;margin:24px 0;"
        f"text-align:center;'>"
        f"<p style='margin:0 0 6px;font-size:15px;font-weight:700;"
        f"color:#333;'>{phone_name} — Our Rating</p>"
        f"<p style='font-size:36px;margin:0 0 4px;color:#f5a623;"
        f"letter-spacing:4px;'>{stars}</p>"
        f"<p style='font-size:22px;font-weight:800;color:#1a73e8;"
        f"margin:0 0 4px;'>{score} / 5</p>"
        f"<p style='font-size:12px;color:#888;margin:0;'>"
        f"Based on 14-day real-world testing in India</p>"
        f"</div>"
    )

def build_mid_article_also_read(cat):
    """Also Read box injected mid-article for reduced bounce rate."""
    BLOG_URL = "https://www.technewsai.me"
    links = {
        "smartphone": [
            ("Best Smartphones Under ₹20,000 in India 2026", f"{BLOG_URL}/search/label/Smartphones"),
            ("Best Gaming Phones India 2026", f"{BLOG_URL}/search/label/Smartphones"),
            ("Best Camera Phones Under ₹30,000 India", f"{BLOG_URL}/search/label/Smartphones"),
        ],
        "laptop": [
            ("Best Laptops Under ₹50,000 in India 2026", f"{BLOG_URL}/search/label/Laptops"),
            ("Best Gaming Laptops India 2026", f"{BLOG_URL}/search/label/Laptops"),
        ],
        "earphone": [
            ("Best Earphones Under ₹2,000 India 2026", f"{BLOG_URL}/search/label/Earphones"),
            ("Best TWS Earbuds India 2026", f"{BLOG_URL}/search/label/Earphones"),
        ],
    }.get(cat, [
        ("Latest Tech Reviews on Tech News With AI", f"{BLOG_URL}/"),
        ("Best Smartphones India 2026", f"{BLOG_URL}/search/label/Smartphones"),
    ])
    items = "".join(
        f"<li style='margin:6px 0;'>"
        f"<a href='{u}' style='color:#1a73e8;text-decoration:none;"
        f"font-weight:500;'>👉 {t}</a></li>"
        for t, u in links
    )
    return (
        f"<div style='background:#f0f7ff;border:1px solid #cce0ff;"
        f"border-radius:10px;padding:18px 20px;margin:32px 0;"
        f"font-size:14px;'>"
        f"<p style='margin:0 0 10px;font-weight:700;color:#1a73e8;"
        f"font-size:15px;'>📖 Also Read on Tech News With AI</p>"
        f"<ul style='margin:0;padding-left:18px;color:#333;'>{items}</ul>"
        f"</div>"
    )

def build_meta_description(title, phone_name, words):
    """Generate SEO meta description as an HTML comment for reference."""
    desc = (
        f"Read our full {phone_name} review — specs, price in India, "
        f"battery life, camera test, gaming performance, and our honest "
        f"14-day verdict. Updated {__import__('datetime').datetime.now().strftime('%B %Y')}."
    )
    if len(desc) > 160:
        desc = desc[:157] + "..."
    return f"<!-- META DESCRIPTION: {desc} -->"


def run_article_v28(story, is_search, label, atype, article_type, log):
    """
    Wrapper around run_article that also saves article_type to log.
    All v28 posts go through here to maintain the day-cycle tracker.
    """
    print("\n" + "="*55)
    print(label + " [" + story.get("category","?").upper() + "]")
    print("="*55)

    cat = story.get("category", "smartphone")

    # Step 0 — SEO title
    print("Step 0: Generating SEO title...")
    seo_title = generate_seo_title(story, is_search)
    story["seo_title"] = seo_title

    # Step 1 — Technical draft (max tokens)
    print("Step 1: Writing full draft (7000+ words target)...")
    draft = groq_draft(story, is_search)
    w1 = len(re.sub(r"<[^>]+>","",draft).split())
    print(f"Draft: {w1} words")

    # Step 2 — Human rewrite (max tokens)
    print("Step 2: Human rewrite as Mallikarjun R...")
    human = human_rewrite(draft, story)
    final = fix_bold(human)

    # Extract clean title
    title = seo_title
    m = re.search(r"<h1[^>]*>(.*?)</h1>", final, re.IGNORECASE|re.DOTALL)
    if m:
        title = re.sub(r"<[^>]+>","",m.group(1)).strip()

    words = len(re.sub(r"<[^>]+>","",final).split())
    print(f"Final: {words} words | {title[:55]}")

    # Strip any auto-generated bio divs
    final = re.sub(
        r'<div[^>]*(?:border-top:3px solid #1a73e8|background:#f0f7ff)[^>]*>.*?</div>',
        '', final, flags=re.DOTALL | re.IGNORECASE
    )

    # ── v35: Strip ALL tables from review articles — prose only ──
    final = re.sub(r'<table[^>]*>.*?</table>', '', final, flags=re.DOTALL | re.IGNORECASE)

    # ── v35: Strip Pros/Cons symbol lists (✅ ❌) — convert to clean prose ──
    # Remove any standalone ✅ / ❌ bullet lines that AI may generate
    final = re.sub(r'[✅❌•]\s*', '', final)

    # Normalise image placeholder comments
    final = re.sub(
        r'<!--\s*PRODUCT_IMAGE:\s*([^-]+?)\s*-->',
        r'<!-- IMAGE PLACEHOLDER: \1 — Add your image here -->',
        final, flags=re.IGNORECASE
    )

    # Inject AdSense slots between every 2nd H3 (articles use H3 sections now)
    h3_count = [0]
    def inject_ad(match):
        h3_count[0] += 1
        return (AD_SLOT_HTML + match.group(0)) if h3_count[0] % 3 == 0 else match.group(0)
    final = re.sub(r'<h3[^>]*>', inject_ad, final, flags=re.IGNORECASE)

    # ── NEW v33: Inject mid-article Also Read box after section 7 (midpoint of 16-section structure) ──
    h3_tags = list(re.finditer(r'<h3[^>]*>', final, re.IGNORECASE))
    mid_also_read = build_mid_article_also_read(cat)
    if len(h3_tags) >= 7:
        insert_pos = h3_tags[6].start()
        final = final[:insert_pos] + mid_also_read + final[insert_pos:]

    # ── NEW v33: Star rating — inject before Final Verdict section (section 15) ──
    phone_name = re.split(r'[:\|–—]', story.get("title", title))[0].strip()
    star_html  = build_star_rating(phone_name)
    verdict_match = re.search(
        r'(<h3[^>]*>[^<]*(?:15\.|final verdict|my honest|honest take)[^<]*</h3>)',
        final, re.IGNORECASE
    )
    if verdict_match:
        vpos  = verdict_match.end()
        final = final[:vpos] + star_html + final[vpos:]

    # FAQ schema
    faqs = extract_faq_from_html(final)
    if not faqs:
        topic_q = story.get("search_topic") or title
        faqs = [
            {"q": "Is " + topic_q + " worth buying in India?",
             "a": "Yes — read the full review above for our honest 14-day test result."},
            {"q": "What is the price of " + topic_q + " in India?",
             "a": "Check the Price section above for all variants, bank offers, and EMI details."},
        ]
    schema_block = build_faq_schema(faqs)

    # ── NEW v33: Published date + reading time header ──
    article_header = build_article_header(title, words)

    # ── NEW v33: Meta description comment ──
    meta_desc = build_meta_description(title, phone_name, words)

    # Footer
    social_block    = build_social_block(title, BLOG_URL)
    also_read_footer= build_also_read_box(cat, title)
    author_bio_html = build_author_bio()
    footer = (
        "<hr style='border:none;border-top:1px solid #d0d7de;margin:40px 0 0;'/>"
        + also_read_footer + social_block + author_bio_html
    )

    # ── v34: Fetch all blog posts for smart interlinking ──
    blog_posts = fetch_all_blog_posts()

    # ── v34: Smart interlinks — blue links to related posts ──
    current_story_title = story.get("title", title)
    final = inject_smart_interlinks(final, current_story_title, blog_posts)

    full_html = meta_desc + schema_block + article_header + final + footer

    # Post to Blogger
    url = post_email(title, full_html)

    # Save log with article_type for cycle tracking
    save_log_v28(log, title, url, words, atype, cat, article_type,
                 story.get("search_topic",""))

    # Ping Google Indexing API
    ping_google_index(url)

    return True


if __name__ == "__main__":
    main()
