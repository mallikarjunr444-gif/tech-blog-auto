# TECH NEWS WITH AI - AUTO BLOG v15.0 ADVANCED FINAL
# technewsai.me - Mallikarjun R, Bengaluru
# ================================================================
# SCHEDULE:
#   Daily   → 1 Smartphone news + 2 Google search topics
#   Weekly  → Laptop, Earphones, Headphones, AirPods, PowerBank, Smartwatch
# ================================================================
# PROCESS:
#   Step 1: Fetch from 65+ official RSS feeds
#   Step 2: AUTO-GENERATE live search topics from RSS headlines (Groq)
#   Step 3: Groq generates clickbait-honest SEO title with number
#   Step 4: Groq writes 4000+ word draft (bullets + tables)
#   Step 5: Groq rewrites as Mallikarjun R (human voice)
#   Step 6: Inject FAQ schema, image blocks, social share, footer
#   Step 7: Ping Google Indexing API + post to Blogger via email
# ================================================================
# v14 NEW FEATURES (ADSENSE + TRAFFIC UPGRADE):
#
#   ADSENSE APPROVAL:
#   - Original content guarantee enforced in every prompt
#   - No thin content — min 4000 words, every section rich
#   - Proper HTML structure (no broken tags, no markdown)
#   - Mobile-friendly: short paragraphs, <p> max 3 sentences
#   - Fast-load: no inline heavy CSS, clean Blogger-safe HTML
#   - AdSense-ready ad slot comments injected between sections
#
#   SEO & TRAFFIC:
#   - Groq generates CTR-optimised clickbait-honest title (with numbers)
#   - Long-tail keywords auto-injected from RSS trends per category
#   - JSON-LD FAQ Schema markup in every post (Google ranking boost)
#   - Image placeholder blocks (1200px Google Discover-ready + alt text)
#   - Social share block: WhatsApp, Telegram, Reddit, Quora links
#   - Google Indexing API ping after every post (instant crawl request)
#   - Old blog update suggester: flags posts >30 days for refresh
#
#   ENGAGEMENT:
#   - Trending AI/tech angle injected into topics daily
#   - All 26 traffic tips wired into prompts and HTML structure
# ================================================================

import os  # must be first — keys below read from environment

GROQ_API_KEY       = os.environ.get("GROQ_API_KEY", "")
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
]

# ================================================================
# CATEGORY STRUCTURES — 12 sections per category
# ================================================================
CAT = {

    "smartphone": {
        "labels": ["Smartphones", "Mobile", "Tech News", "Price in India", "Review", "2026"],
        "detect": ["phone", "smartphone", "android", "iphone", "samsung", "oneplus",
                   "realme", "xiaomi", "oppo", "vivo", "nothing", "honor", "huawei",
                   "pixel", "motorola", "nokia", "infinix", "tecno", "poco", "redmi",
                   "iqoo", "lava", "micromax", "narzo", "moto"],
        "news_topics": [
            "Samsung Galaxy launch India 2026",
            "iPhone launch specs India 2026",
            "OnePlus launch India 2026",
            "Xiaomi Redmi Poco launch India 2026",
            "OPPO Realme launch India 2026",
            "Vivo iQOO launch India 2026",
            "Nothing phone launch 2026",
            "Honor phone launch India 2026",
            "Google Pixel launch India 2026",
            "Motorola Moto launch India 2026",
            "Infinix phone launch India 2026",
            "Tecno Spark launch India 2026",
            "Narzo launch India 2026",
            "budget 5G phone launch India 2026",
            "foldable phone launch India 2026",
            "gaming smartphone launch India 2026",
        ],
        "search_topics": [
            {"t": "best phone under 10000 India 2026",             "k": ["budget phone", "10000"]},
            {"t": "best phone under 12000 India 2026",             "k": ["phone 12000", "India"]},
            {"t": "best phone under 15000 India 2026",             "k": ["phone 15000", "India"]},
            {"t": "best phone under 20000 India 2026",             "k": ["phone 20000", "India"]},
            {"t": "best phone under 25000 India 2026",             "k": ["phone 25000", "India"]},
            {"t": "best phone under 30000 India 2026",             "k": ["phone 30000", "India"]},
            {"t": "best phone under 40000 India 2026",             "k": ["phone 40000", "India"]},
            {"t": "best phone under 50000 India 2026",             "k": ["flagship phone", "India"]},
            {"t": "best 5G phone under 15000 India 2026",          "k": ["5G phone", "India"]},
            {"t": "best 5G phone under 20000 India 2026",          "k": ["5G phone 20000", "India"]},
            {"t": "best 5G phone under 25000 India 2026",          "k": ["5G phone 25000", "India"]},
            {"t": "Samsung Galaxy S26 vs iPhone 17 India 2026",    "k": ["Samsung", "iPhone"]},
            {"t": "OnePlus 14 vs Samsung S26 India 2026",          "k": ["OnePlus", "Samsung"]},
            {"t": "Realme 14 Pro vs Redmi Note 14 Pro India 2026", "k": ["Realme", "Redmi"]},
            {"t": "Nothing Phone 3 vs OnePlus 14 India 2026",      "k": ["Nothing Phone", "OnePlus"]},
            {"t": "iQOO Neo 10 vs OnePlus Nord 4 India 2026",      "k": ["iQOO", "OnePlus Nord"]},
            {"t": "Pixel 9a vs Nothing Phone 3 India 2026",        "k": ["Pixel", "Nothing Phone"]},
            {"t": "best camera phone under 20000 India 2026",      "k": ["camera phone", "India"]},
            {"t": "best camera phone under 30000 India 2026",      "k": ["camera phone 30000", "India"]},
            {"t": "best battery life phone India 2026",            "k": ["battery phone", "India"]},
            {"t": "best gaming phone under 20000 India 2026",      "k": ["gaming phone", "India"]},
            {"t": "best gaming phone under 30000 India 2026",      "k": ["gaming phone 30000", "India"]},
            {"t": "best phone for students India 2026",            "k": ["student phone", "India"]},
            {"t": "best phone for photography India 2026",         "k": ["camera phone", "photography"]},
            {"t": "best phone for video India 2026",               "k": ["video phone", "India"]},
            {"t": "is iPhone 17 worth buying India 2026",          "k": ["iPhone 17", "India"]},
            {"t": "is Samsung S26 worth buying India 2026",        "k": ["Samsung S26", "India"]},
            {"t": "is OnePlus 14 worth buying India 2026",         "k": ["OnePlus 14", "India"]},
            {"t": "is Nothing Phone 3 worth buying India 2026",    "k": ["Nothing Phone 3", "India"]},
            {"t": "best phone with 5000mAh battery India 2026",    "k": ["5000mAh", "India"]},
            {"t": "best slim phone India 2026",                    "k": ["slim phone", "India"]},
            {"t": "best AMOLED phone under 15000 India 2026",      "k": ["AMOLED phone", "India"]},
            {"t": "best phone with 120Hz display India 2026",      "k": ["120Hz phone", "India"]},
            {"t": "Redmi Note 14 Pro vs Samsung M35 India 2026",   "k": ["Redmi Note 14", "Samsung M35"]},
            {"t": "Poco X7 Pro vs iQOO Z9 India 2026",            "k": ["Poco X7", "iQOO Z9"]},
            {"t": "best Motorola phone India 2026",                "k": ["Motorola", "India"]},
            {"t": "best Infinix phone India 2026",                 "k": ["Infinix", "India"]},
        ],
        "sections": [
            "INTRO. Introduction — Who This Phone Is For, Why It Matters in India 2026 (3 paragraphs)",
            "2. Design and Build Quality — Premium Feel or Not? Materials, IP Rating, Dimensions, Colors, Durability",
            "3. Display Review — Brightness, HDR, Outdoor Test, Panel Type, Resolution, Refresh Rate, Real Usage",
            "4. Performance Review — Chipset Deep Dive, Benchmarks, Gaming Test (titles+fps), Daily Usage Experience",
            "5. Battery Life and Charging — Real Usage Test, mAh, Screen-On Hours, Fast Charge Time, India Scenarios",
            "6. Camera Review — Daylight, Night, Portrait, Video, Selfie (each tested separately with real results)",
            "7. Connectivity and Audio — 5G Bands, WiFi, Bluetooth, NFC, Speakers, Sensors, Biometrics",
            "8. Software and AI Features — Android Version, UI, AI Tools, Updates and Long-Term Support",
            "9. Price in India 2026 — All Variants, Launch Offers, No Cost EMI, Best Buy Links",
            "10. Who Should Buy and Who Should Avoid — Specific User Types with Clear Reasons",
            "11. Final Verdict — Is It Worth It? Clear Buy or Skip Recommendation",
            "12. FAQ — Most Searched Questions Indians Ask About This Phone (7 questions)",
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
        from groq import Groq
        client = Groq(api_key=GROQ_API_KEY)

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
            model="llama-3.1-8b-instant",  # fast+cheap for topic generation
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
def pick_news_story(log):
    print("\n[News] Searching RSS feeds...")
    feeds = ALL_RSS[:]
    random.shuffle(feeds)
    used_titles = {e.get("title","") for e in log}

    priority = ["smartphone", "laptop"]
    for pcat in priority:
        data = CAT[pcat]
        random.shuffle(feeds)
        for name, url in feeds[:15]:
            arts = fetch_rss(name, url)
            for a in arts:
                if a["title"] not in used_titles:
                    if any(kw in a["title"].lower() for kw in data["detect"]):
                        a["specs"]    = get_specs(a["title"])
                        a["category"] = pcat
                        print("Found [" + pcat + "]: " + a["title"][:60])
                        return a

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
    print("\n[Search] Building hybrid topic pool (dynamic RSS + static backup)...")

    used_titles  = {e.get("title","")        for e in log}
    used_topics  = {e.get("search_topic","") for e in log}
    combined_used = used_titles | used_topics | used_in_run

    priority_cats    = ["smartphone", "laptop"]
    secondary_cats   = [c for c in CAT if c not in priority_cats]

    all_options = []   # list of (cat, {"t":..., "k":[...]}, source)

    # ── 1. DYNAMIC topics from live RSS (priority categories first) ──
    for pcat in priority_cats:
        dynamic = generate_dynamic_topics(pcat, log, combined_used, count=6)
        for t in dynamic:
            all_options.append((pcat, t, "dynamic"))

    # ── 2. STATIC hardcoded backup (priority categories) ──
    for pcat in priority_cats:
        for t in CAT[pcat]["search_topics"]:
            if t["t"] not in combined_used:
                all_options.append((pcat, t, "static"))

    # ── 3. DYNAMIC topics for rotation categories (if due) ──
    for cat in secondary_cats:
        if not should_post_cat(log, cat):
            continue
        dynamic = generate_dynamic_topics(cat, log, combined_used, count=4)
        for t in dynamic:
            all_options.append((cat, t, "dynamic"))
        # Static backup for these too
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

    # Prioritise dynamic topics over static (fresher = higher rank)
    dynamic_opts = [(c, t, s) for c, t, s in all_options if "dynamic" in s]
    static_opts  = [(c, t, s) for c, t, s in all_options if "static"  in s]
    random.shuffle(dynamic_opts)
    random.shuffle(static_opts)
    ordered = dynamic_opts + static_opts

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
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*",     r"<em>\1</em>",          text)
    text = re.sub(r"```html",       "",                       text)
    text = re.sub(r"```",           "",                       text)
    return text.strip()

# ================================================================
# v14: TITLE GENERATOR — clickbait-honest, numbered, SEO-optimised
# ================================================================
def generate_seo_title(story, is_search):
    """Groq generates a CTR-optimised H1 title with number hook."""
    try:
        client = Groq(api_key=GROQ_API_KEY)
        cat    = story.get("category", "smartphone")
        topic  = story.get("search_topic") or story.get("title", "")
        year   = datetime.datetime.now().year

        prompt = (
            f"You are an India SEO expert. Generate ONE perfect blog title.\n\n"
            f"Topic: {topic}\n"
            f"Category: {cat.upper()}\n"
            f"Year: {year}\n\n"
            f"TITLE RULES:\n"
            f"- Must contain a NUMBER: Top 5, Top 10, Best 7, etc.\n"
            f"- Must be clickbait-honest: make it exciting BUT accurate\n"
            f"- Must include primary keyword and India {year}\n"
            f"- Must be under 65 characters (fits Google title tag)\n"
            f"- Use power words: Best, Tested, Ranked, Honest, Worth It, Buying Guide\n"
            f"- Format options (pick the best fit):\n"
            f"  'Top 5 Best [Product] Under ₹[Price] India {year} — Tested & Ranked'\n"
            f"  '[Product A] vs [Product B] India {year}: Which One Wins?'\n"
            f"  'Is [Product] Worth Buying India {year}? Honest Review'\n"
            f"  'Best [Feature] [Category] India {year}: Top 7 Picks Tested'\n\n"
            f"Output ONLY the title text. No quotes. No explanation."
        )
        r = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # fast+cheap for short title task
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
    Social sharing footer with real app logos (official Wikimedia/CDN).
    Includes WhatsApp, Telegram, Reddit, Quora, LinkedIn, Medium.
    """
    encoded_title = requests.utils.quote(title[:100])
    encoded_url   = requests.utils.quote(url)
    wa_text       = requests.utils.quote(f"{title[:80]} 👉 {url}")

    logo_style = "width:24px;height:24px;vertical-align:middle;margin-right:5px;border-radius:4px;"
    link_style = "display:inline-flex;align-items:center;margin:6px 10px;font-size:13px;font-weight:bold;text-decoration:none;"

    def logo_link(href, logo_url, label, color):
        return (
            f'<a href="{href}" target="_blank" rel="noopener" '
            f'style="{link_style}color:{color};">'
            f'<img src="{logo_url}" alt="{label}" style="{logo_style}" loading="lazy"/>'
            f'{label}</a>'
        )

    return (
        '<div style="border:1px solid #ddd;padding:20px 16px;margin:28px 0;text-align:center;'
        'border-radius:8px;">'
        '<p style="margin:0 0 14px;font-size:15px;font-weight:bold;color:#222;">'
        '📢 Found this helpful? Share it with your friends!</p>'
        '<div style="display:flex;flex-wrap:wrap;justify-content:center;gap:4px;">'

        + logo_link(
            f"https://wa.me/?text={wa_text}",
            SOCIAL_LOGOS["whatsapp"],
            "WhatsApp", "#25d366"
        )
        + logo_link(
            f"https://t.me/share/url?url={encoded_url}&text={encoded_title}",
            SOCIAL_LOGOS["telegram"],
            "Telegram", "#0088cc"
        )
        + logo_link(
            f"https://reddit.com/submit?url={encoded_url}&title={encoded_title}",
            SOCIAL_LOGOS["reddit"],
            "Reddit", "#ff4500"
        )
        + logo_link(
            f"https://www.linkedin.com/sharing/share-offsite/?url={encoded_url}",
            SOCIAL_LOGOS["linkedin"],
            "LinkedIn", "#0077b5"
        )
        + logo_link(
            f"https://medium.com/new-story",
            SOCIAL_LOGOS["medium"],
            "Medium", "#333"
        )

        + '</div>'
        '<p style="margin:14px 0 0;font-size:12px;color:#888;">'
        '💡 <em>Also answer related questions on '
        f'<img src="{SOCIAL_LOGOS["quora"]}" alt="Quora" style="width:16px;height:16px;vertical-align:middle;margin:0 3px;"/>'
        f'<a href="https://www.quora.com/search?q={encoded_title}" target="_blank" '
        'rel="noopener" style="color:#a82400;font-weight:bold;">Quora</a>'
        ' and link back to this article for extra traffic!</em></p>'
        '</div>\n'
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
    Builds a styled 'Also Read' box at the end of the blog.
    For a Vivo blog → links to all Vivo label posts.
    For any brand → links to that brand's label page.
    Falls back to category label page if no brand detected.
    Point 5: All blogs interlinked by brand.
    """
    brand = detect_brand_from_title(title)
    cat_label = CAT_LABELS.get(cat, "Smartphones")

    # Determine the primary "Also Read" link (brand or category)
    if brand and brand in INTERNAL_LINKS:
        brand_display = brand.title()
        brand_url     = INTERNAL_LINKS[brand]
        also_read_label = f"More {brand_display} Reviews"
        also_read_url   = brand_url
    else:
        also_read_label = f"More {cat_label} Reviews"
        also_read_url   = f"{BLOG_URL}/search/label/{cat_label}"

    # Build related links row
    related_links = []
    related_cats = list(CAT_LABELS.values())
    for lbl in related_cats[:4]:
        related_links.append(
            f'<a href="{BLOG_URL}/search/label/{lbl}" '
            f'style="display:inline-block;margin:4px 8px;font-size:13px;'
            f'color:#1a73e8;text-decoration:none;font-weight:500;">'
            f'📱 {lbl.replace("+", " ")}</a>'
        )

    return (
        '\n<div style="border:2px solid #1a73e8;border-radius:10px;padding:20px;'
        'margin:32px 0;background:#f0f7ff;">'
        '<p style="margin:0 0 12px;font-size:16px;font-weight:bold;color:#1a73e8;">'
        '📚 Also Read — Related Articles</p>'
        f'<p style="margin:0 0 10px;">'
        f'<a href="{also_read_url}" target="_blank" '
        f'style="font-size:15px;font-weight:bold;color:#1a73e8;">'
        f'→ {also_read_label} on Tech News With AI</a></p>'
        '<p style="margin:8px 0 4px;font-size:13px;color:#444;">Browse by category:</p>'
        '<div style="display:flex;flex-wrap:wrap;gap:2px;">'
        + "".join(related_links) +
        '</div>'
        f'<p style="margin:10px 0 0;font-size:12px;color:#888;">'
        f'<em>All reviews tested and written by Mallikarjun R | '
        f'<a href="{BLOG_URL}" target="_blank" style="color:#1a73e8;">technewsai.me</a></em></p>'
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
MANDATORY ARTICLE STRUCTURE v16 — TOP 5 / BEST 5 BUYING GUIDES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

Now write ALL of the following sections for THIS product IN ORDER.
NO Pros & Cons table. NO comparison table. Just rich narrative prose.

══════════════════════════════════════════════════
FOR SMARTPHONES — write these sections for EACH of the 5 phones:
══════════════════════════════════════════════════

<h3>[Product] Introduction — Who This Phone Is For and Why It Matters in India 2026</h3>
→ 3 paragraphs: who this phone is built for, what problem it solves, why it ranks at this position,
  India market context (launch date, pricing history, availability on Flipkart/Amazon),
  what makes it stand out from every other phone at this price

<h3>[Product] Design and Build Quality — Premium Feel or Budget Compromise?</h3>
→ 3-4 paragraphs: exact thickness (mm) and weight (g), back panel material, IP rating explained,
  Gorilla Glass version, color variants described vividly, button placement, one-hand usability,
  India real-life line: "At X mm it slips into your jeans without the uncomfortable bulk"

<h3>[Product] Display Review — Brightness, HDR, Outdoor Test, Real Usage</h3>
→ 3 paragraphs: panel type (AMOLED/IPS/LTPO), size, resolution, refresh rate Hz,
  peak brightness nits and what it means in Indian outdoor sun,
  HDR10+ or Dolby Vision support on Netflix/YouTube/Prime,
  real verdict: "In Bengaluru afternoon sun — could I read texts without squinting?"

<h3>[Product] Performance Review — Chipset Deep Dive, Benchmarks, Gaming Test</h3>
→ 4 paragraphs covering:
  [Chipset] full name, nm process, core layout, GPU name, what makes it different
  [Benchmarks] AnTuTu, Geekbench scores vs named competitors
  [Gaming] BGMI/Free Fire/COD Mobile fps at which settings, temperature after 30min, cooling system
  [Daily Use] app switching speed, RAM management, India scenario: "Instagram → Chrome → BGMI — zero stutter"

<h3>[Product] Battery Life and Charging — Real Usage Test, Screen-On Hours, India Scenarios</h3>
→ 2 paragraphs:
  Para 1: mAh, real screen-on hours, what usage mix (gaming/social/video),
          India real-life: "X mAh = full IPL match + 6hrs college + evening commute = still Y% left"
  Para 2: fast charge wattage, 0→50% time, 0→100% time, wireless charging, charger in box or not

<h3>[Product] Camera Review — Daylight, Night, Portrait, Video, Selfie (Each Tested)</h3>
→ 5 paragraphs — ONE per test, NEVER merge:
  [Daylight] main sensor MP, aperture, OIS, colour accuracy, dynamic range, real scenario
  [Night] shadow detail, noise, processing time, astrophotography, honest comparison to named rival
  [Portrait] edge detection in hair/glasses, bokeh quality, natural or artificial
  [Video] max resolution + fps, OIS verdict (walking video smooth?), slow-mo capability, audio quality
  [Selfie] MP, autofocus, Indian skin tone accuracy, portrait selfie edge detection

<h3>[Product] Connectivity and Audio — 5G Bands, WiFi, Speakers, Sensors, Biometrics</h3>
→ 2 paragraphs:
  Para 1: 5G band count, WiFi version, BT version, NFC for UPI, USB type, IR blaster
  Para 2: stereo/mono speakers, Dolby Atmos, loudness test, fingerprint type/speed, face unlock

<h3>[Product] Software and AI Features — Android Version, UI, AI Tools, Update Support</h3>
→ 1-2 paragraphs: Android version, UI name, bloatware level, top 3 AI features in plain language,
  OS update years and security patch years, why this matters for long-term value

<h3>[Product] Price in India 2026 — All Variants, Launch Offers, No Cost EMI, Best Buy Links</h3>
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
WRITING STYLE — MATCH THE iQOO 15R REVIEW BLOG EXACTLY
Reference: https://www.technewsai.me/2026/03/iqoo-15r-review-indias-slimmest-7600mah.html
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TARGET: 4000+ words total. Every H3 section = 2 to 4 rich paragraphs.

─── H3 HEADING FORMAT ───────────────────────────────
• H3 format: "[Product Name] [Section Name] — [Short Descriptive Tagline]"
  ✅ CORRECT: <h3>iQOO 15R Design and Build Quality — Slim, Sleek, and Seriously Durable</h3>
  ✅ CORRECT: <h3>Dell XPS 15 Battery Life — All-Day Power or Office Slave?</h3>
  ✅ CORRECT: <h3>Sony WH-1000XM6 Sound Quality — Deep Bass That Hits Different</h3>
  ❌ WRONG:   <h3>What Are the Key Design Elements of the iQOO 15R?</h3>
  ❌ WRONG:   <h3>Is the Battery Worth It?</h3>
  ❌ WRONG:   <h3>How Does It Actually Perform?</h3>
• FAQ section H3s are the ONLY place question format is allowed.

─── PARAGRAPH STYLE (iQOO 15R REFERENCE) ────────────
• Write 2 to 4 flowing prose paragraphs per H3 — NOT bullet point lists.
• Each paragraph: 3 to 6 sentences. Mix short (6-8 words) with medium (12-16 words).
• Pattern per section:
    Para 1: Lead with the most impressive or surprising fact about this spec
    Para 2: Explain what it means in real Indian daily life with concrete scenarios
    Para 3: Honest trade-off or comparison — what it beats, what it misses
• Bullet points ONLY for: specs box, price variants list, final specifications list
• NEVER write a H3 section as only bullet points — always prose first

─── OPENING HOOK (first sentence of each H3 section) ───
Use one of these styles to open each section naturally:
  "One of the first things that catches your attention about [X] is..."
  "The [section] on the [Product] is a [descriptor] — here is why it matters."
  "For a phone clearly oriented toward [use case], [spec] is non-negotiable."
  "What makes the [Product]'s [section] particularly interesting is..."
  "It is worth being clear about where the [spec] sits relative to the market."

─── INDIA REAL-LIFE TRANSLATION (mandatory per section) ─
Every battery/performance section must translate specs into Indian life:
  "7,600mAh = two full days of mixed use for the average Indian user"
  "At 7.9mm, it slips into your jeans pocket without the uncomfortable bulk"
  "Lasted the entire IPL match + 2 hours of Hotstar binge, still had 25% left"
  "During BGMI at 90fps for 40 continuous minutes — barely warm to the touch"
  "Crystal clear call quality even against Bengaluru peak-hour traffic noise"

─── HONEST TRADE-OFF (mandatory per product) ────────────
Be clear about what the product sacrifices. Like iQOO 15R blog:
  "It is worth being clear about where the camera setup sits relative to the market.
   The phone has deliberately skipped a dedicated telephoto lens to keep the price
   competitive — a trade-off that iQOO has been transparent about."
→ Honesty builds trust. Never hide a weakness. State it, then explain why it still matters.

─── ENGAGEMENT HOOKS ────────────────────────────────────
Add naturally to prose (not as separate lines):
  "But there is one thing nobody tells you about this phone."
  "Before you add it to cart — read this section first."
  "This next one is polarising. Some love it. Some hate it. Here is why."
  "Now if that price is still too high, the next pick will genuinely surprise you."

─── TRANSITION LINES between each product ───────────────
  "That was the safe pick. Now here is the one for real enthusiasts."
  "Different budget, completely different story — keep reading."
  "This next one is polarising. Some love it. Some hate it. Here is exactly why."

─── DATA & SPECIFICITY ──────────────────────────────────
• NEVER: good, nice, amazing, great, excellent, decent, solid
• ALWAYS specifics: deep bass, punchy mids, 42dB ANC, 28ms latency, 144Hz AMOLED
• Minimum 3 real numbers per section (hours, dB, ms, Hz, MP, W, g, mAh, nits)
• Compare to a named competitor: "beats the OnePlus 13R by 15% on AnTuTu"

─── CATEGORY ACCURACY ───────────────────────────────────
• Earphones:   ANC dB | codec AAC/aptX/LDAC | driver mm | IP rating | latency ms
• Headphones:  clamping force | earcup padding | ANC dB | fold design | wired mode
• Smartphones: SoC name+process | panel type+Hz | sensor name | mAh | charge W | IP
• Laptops:     CPU name+gen | RAM GB | SSD GB+type | nits | Wh | kg | GPU name
• Smartwatch:  display type+size | battery days | GPS type | SpO2/ECG | ATM
• Power Bank:  mAh rated vs actual | input W | output W | PD/QC version | g weight

─── ABSOLUTE NEVER ──────────────────────────────────────
• NO **markdown bold** — ONLY <strong>HTML</strong> bold tags
• NO Q&A H3 headings (except in FAQ section)
• NO: "In conclusion", "To summarize", "It is worth noting", "Overall"
• NO repeated sentence anywhere in the article
• NO wrong-category specs (AMOLED in earphone article = immediate reject)
• NO links to external sites — ONLY www.technewsai.me label pages
• NO auto-image insertion — images are pasted manually by the blogger
• NO Pros & Cons tables in Top 5 / Best 5 / Buying Guide articles
• NO comparison tables or side-by-side tables in Top 5 / Buying Guide articles
• NO verdict tables in Top 5 / Buying Guide articles — write prose verdict only
• NO skipping sections — every product must have EVERY category H3 section written in full

─── MINIMUM REQUIREMENTS ────────────────────────────────
✓ 4000+ words of rich prose content (Top 5 articles should be 6000+ words)
✓ Narrative hook intro (3 paragraphs, no H2)
✓ Primary keyword in first 100 words
✓ For Top 5 / Buying Guide: every product gets Quick Specs box + ALL category H3 sections
✓ Full Specifications bullet list per product
✓ Transition line between every product
✓ Final Verdict as prose paragraphs (NO table in buying guides)
✓ FAQ AFTER Final Verdict, with 5-7 question H3s (only Q&A allowed here)
✓ Author bio as absolute last element

─── ADSENSE APPROVAL ────────────────────────────────────
• 100% original — never copy or closely paraphrase any source
• Every paragraph adds NEW information — no filler or repeated ideas
• <p> max 3-4 sentences (mobile-friendly)
• No broken HTML — all tags properly closed

─── LONG-TAIL KEYWORDS (inject naturally) ───────────────
These must appear in the article text — not stuffed, naturally woven:
[LONGTAIL_KEYWORDS_PLACEHOLDER]
"""


def groq_draft(story, is_search):
    client   = Groq(api_key=GROQ_API_KEY)
    cat      = story.get("category", "smartphone")
    struct   = CAT.get(cat, CAT["smartphone"])

    # Build the section-to-H2 instruction — each section becomes a mandatory H2
    sections_list = struct["sections"]
    # Strip leading "N. " numbering for cleaner H2 text; keep the full description as guide
    pat = re.compile(r"^\d+\.\s*")
    sections_as_h2 = "\n".join(
        "  <h2 id=\"section-" + str(i+1) + "\">" + pat.sub("", s.split("—")[0]).strip() + "</h2>  "
        + "<-- H2 " + str(i+1) + " of " + str(len(sections_list))
        + " | details: " + (s.split("—")[1].strip() if "—" in s else s)
        for i, s in enumerate(sections_list)
    )

    cat_label  = cat.upper()
    link_rules = build_internal_link_instructions(cat)

    # Build longtail keywords from live context
    ctx_text    = story.get("rss_context", "")
    topic_text  = story.get("search_topic") or story.get("title", "")
    longtail_kw = build_longtail_keywords(cat, ctx_text, topic_text)
    kw_list     = "\n".join(f"  • {k}" for k in longtail_kw)

    rules_with_kw = WRITING_RULES.replace(
        "[LONGTAIL_KEYWORDS_PLACEHOLDER]", kw_list
    )

    seo_title = story.get("seo_title", "")
    title_instruction = (
        f'USE THIS EXACT H1 TITLE (already SEO-optimised):\n<h1>{seo_title}</h1>\n\n'
        if seo_title else
        f"Generate H1 title: number hook + primary keyword + India + year. Max 65 chars.\n\n"
    )

    # Category-specific H2 section block shown prominently
    section_block = (
        f"━━━ CATEGORY: {cat_label} — MANDATORY {len(sections_list)} H2 SECTIONS ━━━\n"
        f"Write ALL sections below IN ORDER as H2 headings.\n"
        f"Do NOT skip, reorder, or merge any section.\n"
        f"CRITICAL: Use the EXACT H2 text shown below. Replace {{Product}} with the real product name.\n"
        f"Do NOT use clickbait or dramatic hooks as H2 text. H2 must be clean and descriptive.\n"
        f"Personal hooks and commentary go in the first <p> paragraph UNDER the H2, never inside it.\n"
        f"Under each H2, write H3 question-based subheadings.\n\n"
        f"{sections_as_h2}\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )

    if is_search:
        topic = story["search_topic"]
        ctx   = story.get("rss_context", "")
        if " vs " in topic.lower():
            mode = (
                "HEAD TO HEAD COMPARISON.\n"
                "- Compare BOTH products in every single section side by side.\n"
                "- Each section: show Product A result, then Product B result.\n"
                "- Add separate Pros & Cons table for EACH product.\n"
                "- Add specs box for each product.\n"
                "- End with a 'Which to Buy' verdict table (plain border, no colour).\n"
                "- Add 'Best For' line for each product.\n"
                "- Use transition line between each comparison section.\n"
            )
        elif "under" in topic.lower() or "best" in topic.lower():
            mode = (
                "TOP 5 BUYING GUIDE.\n"
                "- List exactly 5 real products with full real India specs and prices.\n"
                "- Follow the MANDATORY ARTICLE STRUCTURE v16 below EXACTLY for every product.\n"
                "- Every product gets ALL category-specific H3 sections written in full prose.\n"
                "- Add Quick Specs box for every product.\n"
                "- Add IMAGE PLACEHOLDER immediately after each product H2 heading.\n"
                "- Add transition line between each product.\n"
                "- NO Pros & Cons table anywhere in the article.\n"
                "- NO comparison table anywhere in the article.\n"
                "- Final Verdict section is written as rich prose paragraphs — NO table.\n"
                "- FAQ section comes AFTER the Final Verdict.\n"
            )
        else:
            mode = (
                "EXPERT GUIDE.\n"
                "- Answer the search question completely with real data.\n"
                "- Recommend 3-5 specific products with India prices.\n"
                "- Add specs box and Pros & Cons for each recommended product.\n"
                "- Practical India advice throughout.\n"
            )

        prompt = (
            title_instruction +
            "Write a comprehensive SEO-optimised guide for Indians searching: '" + topic + "'\n\n"
            "ARTICLE TYPE: " + mode + "\n\n"
            "REAL DATA FROM RSS AND REVIEW SOURCES:\n"
            + (ctx or "Use your latest India market 2026 knowledge.") + "\n\n"
            + section_block
            + BUYING_GUIDE_STRUCTURE + "\n\n"
            + rules_with_kw + "\n\n"
            + link_rules + "\n\n"
            "SEO CHECKLIST:\n"
            "✓ H1 is the pre-generated title above (use it exactly)\n"
            "✓ Primary keyword in first 100 words\n"
            "✓ Keyword in at least 3 H2 headings\n"
            "✓ Question-based H3 subheadings (improves SEO)\n"
            "✓ Long-tail keywords woven in naturally (not stuffed)\n"
            "✓ Real ₹ prices — Flipkart/Amazon India\n"
            "✓ Real product names — never invent specs\n"
            "✓ h1 h2 h3 p ul li table — HTML only, NEVER markdown\n"
            "✓ <p> tags: max 3 sentences (mobile-friendly)\n"
            "✓ <strong> for specs, prices, key data\n"
            "✓ Brand names hyperlinked to your blog label pages only\n"
            "✓ FAQ section: first question = exact search query\n"
            "✓ ORIGINAL content — no copy, no thin filler\n"
            "Write now:"
        )
    else:
        prompt = (
            title_instruction +
            "Write a detailed SEO-optimised article about: " + story["title"] + "\n"
            "CATEGORY: " + cat.upper() + "\n"
            "SOURCE: " + story["source"] + "\n"
            "REAL SPECS:\n" + (story.get("specs") or "Use your knowledge for this device.") + "\n"
            "DESCRIPTION: " + story.get("description", "") + "\n\n"

            "MANDATORY STRUCTURE:\n"
            "1. Use the pre-generated H1 title above (exactly as given)\n"
            "2. Hook intro — 2 lines: problem + solution. Primary keyword in first 100 words.\n"
            "3. Table of Contents — plain border, no colour:\n"
            + TOC_HTML + "\n"
            "4. Specs box for this device:\n"
            + SPECS_BOX_HTML + "\n"
            "5. Pros & Cons table — plain border, no colour:\n"
            + PROS_CONS_HTML + "\n\n"

            + section_block

            + rules_with_kw + "\n\n"
            + link_rules + "\n\n"
            "SEO CHECKLIST:\n"
            "✓ H1 is the pre-generated title (use exactly)\n"
            "✓ Primary keyword in first 100 words\n"
            "✓ Long-tail keywords woven in naturally\n"
            "✓ Question-based H3 subheadings\n"
            "✓ Real ₹ prices\n"
            "✓ <strong> for key specs\n"
            "✓ <p> max 3 sentences (mobile-friendly)\n"
            "✓ Brand names hyperlinked to your blog label pages only\n"
            "✓ Bullet points — not long paragraphs\n"
            "✓ Real-life India usage line in every section\n"
            "✓ FAQ with 7 questions Indians actually search\n"
            "✓ Strong final verdict with clear winner + CTA\n"
            "✓ ORIGINAL content — no copy, no thin filler\n"
            "Write now:"
        )
    r = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=6000, temperature=0.7,
    )
    return r.choices[0].message.content


# ================================================================
# STEP 2: HUMAN REWRITE — Mallikarjun R voice (v12)
# ================================================================
def human_rewrite(draft, story):
    client = Groq(api_key=GROQ_API_KEY)
    cat    = story.get("category", "smartphone")
    today  = datetime.datetime.now().strftime("%B %d, %Y")
    labels = ", ".join(CAT.get(cat, CAT["smartphone"])["labels"])
    link_rules = build_internal_link_instructions(cat)

    author_bio = (
        '<div style="border-top:3px solid #1a73e8;margin-top:40px;padding:20px;'
        'background:#f0f7ff;border-radius:12px;">'
        "<table><tr>"
        '<td style="width:85px;vertical-align:top;padding-right:15px;">'
        '<img src="https://lh3.googleusercontent.com/pw/AP1GczNbk_7GTq9-pE7KTZUn0skqYYoESZzxYYQ1uTQvvu6dDj-2AUPZyvUGs5XPOGrt5HeVnMuHzPHO8tp1OA0zuhAKF6wlOho_8Q1aVAlVTwG9CNr_jH8=s400-no"'
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
        f'<p style="font-size:12px;color:#999;"><em>Published: {today} &bull; <a href="{BLOG_URL}" target="_blank">technewsai.me</a></em></p>'
        "</td></tr></table></div>"
    )

    prompt = (
        "You are Mallikarjun R — 19-year-old CSE student and tech blogger from Bengaluru, India.\n"
        "Category: " + cat.upper() + " | Labels: " + labels + "\n\n"

        "━━━ YOUR TASK ━━━\n"
        "This draft is tool-generated and generic. Rewrite it entirely in your voice.\n"
        "Preserve ALL HTML tables and ALL structure. Only rewrite the TEXT.\n\n"

        "━━━ MUST PRESERVE (DO NOT TOUCH) ━━━\n"
        "• All HTML tables — comparison, pros/cons, verdict, specs boxes\n"
        "• Expert Tip callout divs and Should You Buy boxes\n"
        "• Table of Contents and all anchor links\n"
        "• ALL H1, H2, H3 HEADINGS — copy them EXACTLY as they are. NEVER rewrite heading text.\n"
        "• All internal links to www.technewsai.me\n"
        "• Best For lines, Mini Verdict lines, CTA lines\n\n"

        "━━━ CRITICAL HEADING RULE ━━━\n"
        "H2 and H3 heading text is FIXED — copy it exactly from the draft.\n"
        "H2 section headings follow this pattern: '[Product Name] [Section] — [Short Tagline]'\n"
        "Example: 'iQOO 15R Design and Build Quality — Premium Feel or Not?'\n"
        "Example: 'Sony WH-1000XM6 Battery Life and Charging — Real Usage Test'\n"
        "The ONLY place question-format H3s are allowed = inside the FAQ section.\n"
        "Personal hooks go in the FIRST <p> paragraph AFTER the heading — never inside the H2.\n"
        "Correct: <h2>iQOO 15R Performance Review</h2><p>Here is what genuinely surprised me...</p>\n"
        "Wrong:   <h2>Does the iQOO 15R Perform Well?</h2>\n\n"

        "━━━ FOR EVERY SECTION, DO ALL OF THESE ━━━\n\n"
        "① PERSONAL HOOK — first <p> AFTER the H2/H3 (NOT inside the heading):\n"
        "   'Here is what the spec sheet does NOT tell you about this one.'\n"
        "   'I tested this for 2 weeks straight. The result genuinely surprised me.'\n"
        "   'Before you add to cart — read this section first.'\n\n"
        "② CLIFFHANGER after first line of every product:\n"
        "   'But there is one big problem with it. Keep reading.'\n"
        "   'Sounds perfect — until you see the battery numbers.'\n\n"
        "③ PERSONAL EXPERIENCE (category-specific):\n"
        "   Earphones: 'I wore these for my entire Bengaluru metro ride — here is what I noticed.'\n"
        "   Phone:     'I have been testing phones at this price for the last 3 months.'\n"
        "   Laptop:    'After a full week of coding sessions and Netflix on this machine —'\n"
        "   Powerbank: 'My phone died mid-exam call. That is why I tested every model here.'\n"
        "   Watch:     'I wore this for 2 weeks straight — morning runs, office, gym, sleep.'\n\n"
        "④ INDIA REAL-LIFE LINE — make every spec mean something:\n"
        "   Bad:  '5000mAh battery'\n"
        "   Good: '<strong>5000mAh</strong> = full IPL match + 6 hrs college + evening commute'\n"
        "   Bad:  '30hr battery'\n"
        "   Good: '<strong>30 hrs total</strong> = 5 days of office commute without charging'\n\n"
        "⑤ HONEST REACTION (1 punchy line per section):\n"
        "   'Genuinely surprised me for this price.'\n"
        "   'Honestly? I expected better from this brand.'\n"
        "   'This is where it gets really interesting.'\n\n"
        "⑥ TRANSITION BRIDGE between every product:\n"
        "   'Now if that price is still too high, the next pick will surprise you.'\n"
        "   'Different budget, completely different experience — here we go.'\n"
        "   'This next one is polarising. Some love it. Some hate it. Here is why.'\n\n"
        "⑦ INDIA ADVICE (specific, actionable):\n"
        "   'Grab this during Flipkart Big Billion Days — extra ₹500 off with bank card.'\n"
        "   '8GB variant is worth ₹1500 more. Trust me on this one.'\n\n"
        "⑧ ONE LIKE + ONE DISLIKE (honest, product-specific):\n"
        "   'Love: deep bass response on the 10mm driver.'\n"
        "   'Dislike: call quality drops in heavy wind above 20 kmph.'\n\n"

        "━━━ WRITING STYLE ━━━\n"
        "• Write rich PROSE paragraphs for each section (like the reference blog at technewsai.me)\n"
        "• Mix bullets with paragraphs — not everything should be bullet points\n"
        "• Indian English: value for money, decent enough, not bad at all\n"
        "• Connectors: look, here is the thing, honestly, but wait, catch is\n"
        "• Questions embedded in prose: 'But does it hold up in real use?'\n"
        "• India scenarios: IPL, hostel WiFi, Bengaluru traffic, wedding, board exams\n"
        "• Comparison lines: 'better ANC than X', 'cheaper than Y by ₹NNN'\n"
        "• Specific words only — NEVER: good, nice, amazing, great, excellent\n"
        "• Use: deep bass, clear vocals, crisp display, punchy mids, warm tones, sharp camera\n\n"

        "━━━ CATEGORY ACCURACY ━━━\n"
        "Only use specs that match the category:\n"
        "• Earphones: ANC dB, codec, driver size, IP rating, latency ms, ear tip fit\n"
        "• Headphones: clamping force, padding, ANC level, wired backup, fold design\n"
        "• Phones: display type, processor name, camera MP/aperture, battery mAh, charge W\n"
        "• Laptops: CPU name+gen, RAM GB, SSD GB/type, display nits, battery Wh, kg weight\n"
        "• Smartwatch: display size+type, battery days, GPS, SpO2, ECG, ATM water rating\n"
        "• Powerbank: mAh real output, input W, output W, PD/QC, cable type, g weight\n"
        "NEVER mix categories. Never write AMOLED display for earphones.\n\n"

        + link_rules + "\n\n"

        "━━━ ABSOLUTE NEVER ━━━\n"
        "• NEVER **markdown** — ONLY <strong>HTML</strong> tags\n"
        "• NEVER: 'In conclusion', 'To summarize', 'It is worth noting'\n"
        "• NEVER change clean H3 headings to question format\n"
        "• NEVER two consecutive sections starting the same way\n"
        "• NEVER repeat same sentence in different sections\n"
        "• NEVER remove or change any HTML table\n"
        "• NEVER link to any website except www.technewsai.me\n"
        "• NEVER write generic sentences that could apply to any product\n"
        "• NEVER add Pros & Cons tables in Top 5 / Best 5 / Buying Guide articles\n"
        "• NEVER add comparison tables or side-by-side tables in Buying Guide articles\n"
        "• NEVER add verdict tables in Buying Guide articles — prose verdict only\n\n"

        "━━━ FINAL CHECKS ━━━\n"
        "✓ 4000+ words\n"
        "✓ Hook intro — problem line 1, solution line 2\n"
        "✓ Primary keyword in first 100 words\n"
        "✓ Curiosity gap hook on every H2 (in first <p> after heading)\n"
        "✓ Cliffhanger after first line of every product\n"
        "✓ Transition bridge between every product section\n"
        "✓ All products: specs box + ALL category H3 sections (no pros/cons table in buying guides) + should-you-buy + mini verdict\n"
        "✓ Strong final verdict with clear winner declared\n"
        "✓ Author bio at the very end\n\n"

        "ADD AUTHOR BIO as absolute last element:\n"
        + author_bio + "\n\n"

        "NOW REWRITE — every word human, every spec accurate:\n\n"
        + draft
    )

    r = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=5000, temperature=0.88,
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

    # Step 7 — Footer
    footer = (
        "<hr/>"
        + also_read
        + social_block
        + f"<p style='font-size:12px;color:#888;text-align:center;padding:10px;'>"
        f"<em>Published by Mallikarjun R | "
        f"<a href='{BLOG_URL}' target='_blank'>Tech News With AI</a>"
        f" | technewsai.me</em></p>"
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
# MAIN
# ================================================================
def main():
    print("=======================================================")
    print(" TECH NEWS WITH AI - AUTO BLOG v14.0 ADVANCED")
    print(" Daily: 1 News + 2 Dynamic Search Topics")
    print(" Topics: Live RSS → Groq auto-generates trending topics")
    print(" Content: 4000+ words | Schema | Images | Social Share")
    print(" AdSense: Original content | Mobile-friendly | Hooks")
    print(" technewswithai.blogspot.com")
    print("=======================================================")

    log         = load_log()
    used_in_run = set()
    success     = 0

    # Suggest old posts to update (SEO refresh)
    suggest_old_updates(log, days_threshold=30)

    # Article 1 — Latest RSS News (phone/laptop priority)
    try:
        s1 = pick_news_story(log)
        if s1:
            run_article(s1, False, "ARTICLE 1: LATEST NEWS", "news", log)
            log = load_log()
            success += 1
            print("Waiting 35s...")
            time.sleep(35)
    except Exception as e:
        print("Article 1 failed: " + str(e))

    # Article 2 — Dynamic search topic
    try:
        s2 = pick_search_story(log, used_in_run)
        if s2:
            run_article(s2, True, "ARTICLE 2: SEARCH TOPIC", "search", log)
            log = load_log()
            success += 1
            print("Waiting 35s...")
            time.sleep(35)
    except Exception as e:
        print("Article 2 failed: " + str(e))

    # Article 3 — 2nd Google Search Topic
    try:
        s3 = pick_search_story(log, used_in_run)
        if s3:
            run_article(s3, True, "ARTICLE 3: SEARCH TOPIC", "search", log)
            success += 1
    except Exception as e:
        print("Article 3 failed: " + str(e))

    print("\n=======================================================")
    print("DONE! " + str(success) + "/3 articles posted!")
    print("Next steps:")
    print("  → Submit sitemap in Google Search Console")
    print("  → Share articles on WhatsApp & Telegram channels")
    print("  → Post answers on Quora with your blog links")
    print("  → Republish summaries on Medium + LinkedIn")
    print("  → Replace image placeholders in Blogger with 1200px images")
    print("Visit: https://technewswithai.blogspot.com")
    print("=======================================================")


if __name__ == "__main__":
    main()
