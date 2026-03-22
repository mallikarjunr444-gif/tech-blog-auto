# TECH NEWS WITH AI - AUTO BLOG v13.0 ADVANCED FINAL
# technewswithai.blogspot.com - Mallikarjun R, Bengaluru
# ================================================================
# SCHEDULE:
#   Daily   → 1 Smartphone/Laptop news + 2 Google search topics
#   Weekly  → Earphones Headphones AirPods PowerBank Smartwatch
#             (each once every rotation schedule)
# ================================================================
# PROCESS:
#   Step 1: Fetch from 65+ official RSS feeds
#   Step 2: AUTO-TOPIC ENGINE generates live topics from RSS+Trends
#   Step 3: Groq writes 4000+ word SEO-optimised draft
#   Step 4: Groq rewrites as human (Mallikarjun R voice)
#   Step 5: Post to Blogger via email
# ================================================================
# v13 CHANGES (AUTO TOPIC + 4000-WORD + ADVANCED ENGAGEMENT):
#   - AUTO-TOPIC ENGINE: Google Trends India RSS + RSS product
#     extraction + dynamic "vs" and "review" topic generation
#   - 6-hour topic cache (auto_topics_cache.json) — no stale topics
#   - Regex product extractor for all 7 categories
#   - Price-bracket topics auto-generated for every run
#   - 4000+ word target (was 3000)
#   - max_tokens bumped to 8000 (draft) and 8000 (rewrite)
#   - Engagement: storytelling hooks, data callouts, cliffhangers,
#     reader polls, "Did you know?" boxes, engagement CTAs
#   - Bullet-first structure enforced across all sections
#   - Internal brand links auto-injected per category
# ================================================================

GROQ_API_KEY       = "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"
NEWS_API_KEY       = "673bca5ceab54fa8bb7ed0344c8f6d13"
BLOGGER_POST_EMAIL = "mallikarjunr444.technewswithai6361@blogger.com"
GMAIL_ADDRESS      = "mallikarjunr444@gmail.com"
GMAIL_APP_PASSWORD = "oeirtosmlhuwntka"

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
            "1. Why These Earphones Are Worth Talking About in India",
            "2. Design Comfort and Build Quality — form factor materials fit tip sizes",
            "3. Sound Quality Deep Dive — bass mids highs soundstage balanced vs bass-heavy",
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
            "1. Why These Headphones Are Getting Attention in India",
            "2. Design Build Comfort — padding clamp force foldability weight materials",
            "3. Sound Signature Deep Dive — bass mids highs soundstage tuning style",
            "4. ANC vs Passive Isolation — real world environments performance comparison",
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
            "1. Are These AirPods Worth Buying in India in 2026",
            "2. Design Fit and Color Options — form factor comfort ear tip sizes",
            "3. Sound Quality and Apple Spatial Audio — real listening experience",
            "4. ANC and Transparency Mode — comparison with Sony Bose Samsung",
            "5. Apple Ecosystem Integration — iPhone iPad Mac seamless switching",
            "6. Call Quality and Siri — mic clarity wind noise India Siri accuracy",
            "7. Battery Life Case and Charging — hours MagSafe wireless quick charge",
            "8. H2 Chip Smart Features — adaptive audio conversation awareness",
            "9. Comfort for Indian Ears Long Sessions — gym commute daily wear",
            "10. India Price Is It Worth It — vs Noise boAt Sony OnePlus comparison",
            "11. Should You Buy AirPods or Android Alternative — honest India advice",
            "12. My Final Verdict and FAQ — buy or skip + 7 questions Indians ask",
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
            "11. Top 3 Alternatives with India Prices — Anker MI Realme boAt compared",
            "12. My Final Verdict and FAQ — recommendation + 7 questions about power banks",
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
# ================================================================
ROTATION_DAYS = {
    "earphones":  7,
    "headphones": 14,
    "airpods":    14,
    "powerbank":  21,
    "smartwatch": 10,
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
    for name, url in feeds[:20]:
        for a in fetch_rss(name, url):
            if any(kw.lower() in a["title"].lower() for kw in keywords):
                ctx.append("FROM " + a["source"] + ": " + a["title"] + " — " + a["description"][:200])
            if len(ctx) >= 8:
                break
        if len(ctx) >= 8:
            break
    return "\n".join(ctx[:8])

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

# ================================================================
# AUTO TOPIC ENGINE — Google Trends + RSS Product Extraction
# ================================================================

GOOGLE_TRENDS_IN  = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=IN"
AUTO_TOPICS_CACHE = "auto_topics_cache.json"
CACHE_TTL_HOURS   = 6   # refresh every 6 hours

# ── Extra live trend sources (RSS-parseable, no auth needed) ──────
EXTRA_TREND_FEEDS = [
    ("Bing SmartphoneIN",   "https://www.bing.com/news/search?q=best+smartphone+india+2026&format=RSS"),
    ("Bing LaptopIN",       "https://www.bing.com/news/search?q=best+laptop+india+2026&format=RSS"),
    ("Bing EarphonesIN",    "https://www.bing.com/news/search?q=best+earphones+india+2026&format=RSS"),
    ("Bing SmartwatchIN",   "https://www.bing.com/news/search?q=best+smartwatch+india+2026&format=RSS"),
    ("Bing PowerbankIN",    "https://www.bing.com/news/search?q=best+power+bank+india+2026&format=RSS"),
    ("Bing HeadphonesIN",   "https://www.bing.com/news/search?q=best+headphones+india+2026&format=RSS"),
    ("Bing PhoneLaunch",    "https://www.bing.com/news/search?q=phone+launch+india&format=RSS"),
    ("Bing LaptopLaunch",   "https://www.bing.com/news/search?q=laptop+launch+india&format=RSS"),
    ("Reddit IndiaTech",    "https://www.reddit.com/r/IndiaTech.rss?limit=20"),
    ("Reddit Android",      "https://www.reddit.com/r/Android.rss?limit=10"),
    ("Reddit Apple",        "https://www.reddit.com/r/apple.rss?limit=10"),
    ("Reddit Earphones",    "https://www.reddit.com/r/headphones+inearfidelity.rss?limit=10"),
    ("DDG BestPhoneIN",     "https://duckduckgo.com/?q=best+phone+india+2026&ia=news&format=rss"),
    ("DDG BestLaptopIN",    "https://duckduckgo.com/?q=best+laptop+india+2026&ia=news&format=rss"),
]

NEWSAPI_TREND_QUERIES = [
    "best smartphone india 2026", "best laptop india 2026", "best earphones india 2026",
    "best smartwatch india 2026", "best power bank india 2026", "best headphones india 2026",
    "phone launch india", "laptop launch india", "earbuds launch india",
    "5G phone india", "budget phone india", "gaming phone india",
]

# ── Regex patterns to extract product model names from RSS text ───
BRAND_PATTERNS = {
    "smartphone": [
        r"(Samsung Galaxy [A-Z][0-9A-Za-z\+\s]{2,20})",
        r"(iPhone\s?[0-9]{1,2}\s?(?:Pro|Plus|Max|Mini)?)",
        r"(OnePlus\s?(?:Nord\s?)?[0-9]{1,2}\s?(?:Pro|Ultra|R|T)?)",
        r"(Redmi Note\s?[0-9]{1,2}\s?(?:Pro|Plus|Turbo)?)",
        r"(Poco\s?[A-Z][0-9]{1,2}\s?(?:Pro|GT|Ultra)?)",
        r"(Realme\s?[0-9]{1,2}\s?(?:Pro|Plus|Ultra)?)",
        r"(Nothing Phone\s?\(?[0-9a-z]+\)?)",
        r"(Google Pixel\s?[0-9][a-z]?(?:\s?Pro)?)",
        r"(Motorola (?:Edge|Razr|Moto G|Moto E)\s?[0-9A-Za-z\s]{2,15})",
        r"(iQOO\s?(?:Neo\s?|Z\s?|)[0-9]{1,2}\s?(?:Pro|Ultra|GT)?)",
        r"(Vivo\s?[VTX][0-9]{1,2}\s?(?:Pro|GT|Plus)?)",
        r"(OPPO\s?(?:Reno|Find|A)\s?[0-9A-Za-z\s]{2,12})",
        r"(Infinix\s?(?:Note|Hot|Zero)\s?[0-9A-Za-z\s]{2,10})",
    ],
    "laptop": [
        r"(MacBook\s?(?:Air|Pro)\s?(?:M[0-9])?)",
        r"(Dell\s?(?:XPS|Inspiron|Alienware|Vostro)\s?[0-9A-Za-z\s]{2,12})",
        r"(HP\s?(?:Pavilion|Envy|Spectre|Victus|Omen)\s?[0-9A-Za-z\s]{2,12})",
        r"(Lenovo\s?(?:IdeaPad|ThinkPad|Legion|LOQ)\s?[0-9A-Za-z\s]{2,12})",
        r"(ASUS\s?(?:ROG|TUF|ZenBook|VivoBook)\s?[0-9A-Za-z\s]{2,12})",
        r"(Acer\s?(?:Nitro|Aspire|Predator|Swift)\s?[0-9A-Za-z\s]{2,12})",
        r"(MSI\s?(?:Katana|Stealth|Titan|Raider)\s?[0-9A-Za-z\s]{2,12})",
    ],
    "earphones": [
        r"(boAt\s?Airdopes\s?[0-9A-Za-z\s]{2,12})",
        r"(Nothing Ear\s?(?:\([0-9a-z]+\)|[0-9a-z]*))",
        r"(OnePlus\s?Buds\s?[A-Za-z0-9\s]{0,10})",
        r"(Sony\s?WF[- ][0-9A-Z\-]{3,12})",
        r"(Samsung Galaxy Buds\s?[0-9A-Za-z\+\s]{0,10})",
        r"(Noise Buds\s?[A-Za-z0-9\s]{2,12})",
        r"(Realme Buds\s?[A-Za-z0-9\s]{2,12})",
        r"(JBL\s?(?:Tune|Live|Free|Reflect)\s?[0-9A-Za-z\s]{2,12})",
    ],
    "headphones": [
        r"(Sony\s?WH[- ][0-9A-Z\-]{4,12})",
        r"(Bose\s?(?:QC|QuietComfort|NC)\s?[0-9A-Za-z\s]{2,12})",
        r"(boAt\s?Rockerz\s?[0-9A-Za-z\s]{2,12})",
        r"(JBL\s?Tune\s?[0-9A-Za-z\s]{2,12})",
        r"(Sennheiser\s?[A-Z]{2}[0-9]{2,4})",
    ],
    "smartwatch": [
        r"(Apple Watch\s?(?:Series\s?[0-9]+|Ultra|SE)\s?[0-9A-Za-z\s]{0,10})",
        r"(Samsung Galaxy Watch\s?[0-9A-Za-z\s]{0,12})",
        r"(Amazfit\s?(?:GTR|GTS|T-Rex|Bip|Falcon)\s?[0-9A-Za-z\s]{0,12})",
        r"(Garmin\s?(?:Venu|Vivoactive|Forerunner|Fenix)\s?[0-9A-Za-z\s]{0,12})",
        r"(boAt\s?Watch\s?[A-Za-z0-9\s]{2,12})",
        r"(Noise\s?(?:ColorFit|Evolve)\s?[A-Za-z0-9\s]{2,12})",
    ],
    "powerbank": [
        r"(Anker\s?(?:PowerCore|Prime)\s?[0-9A-Za-z\s]{0,12})",
        r"((?:MI|Xiaomi)\s?(?:Power Bank|Powerbank)\s?[0-9A-Za-z\s]{0,12})",
        r"(boAt\s?(?:Energy|Power)\s?[A-Za-z0-9\s]{0,12})",
        r"(Realme\s?(?:Power Bank|Powerbank)\s?[0-9A-Za-z\s]{0,12})",
        r"(Ambrane\s?[A-Za-z0-9\s]{2,12})",
    ],
    "airpods": [
        r"(AirPods\s?(?:Pro\s?[0-9]?|Max|[0-9]+)?)",
    ],
}

# ── Topic generators: product name → review/worth-buying topics ───
TOPIC_GENS = {
    "smartphone": [
        lambda m, y: f"{m} full review India {y}",
        lambda m, y: f"is {m} worth buying India {y}",
        lambda m, y: f"{m} price specs India {y}",
    ],
    "laptop": [
        lambda m, y: f"{m} review India {y}",
        lambda m, y: f"is {m} worth buying India {y}",
    ],
    "earphones": [
        lambda m, y: f"{m} review India {y}",
        lambda m, y: f"is {m} worth buying India {y}",
    ],
    "headphones": [
        lambda m, y: f"{m} review India {y}",
    ],
    "smartwatch": [
        lambda m, y: f"{m} review India {y}",
        lambda m, y: f"is {m} worth buying India {y}",
    ],
    "powerbank": [
        lambda m, y: f"{m} review India {y}",
    ],
    "airpods": [
        lambda m, y: f"{m} review India {y}",
        lambda m, y: f"is {m} worth buying India {y}",
    ],
}

VS_TEMPLATES = [
    "{a} vs {b} India {y}",
    "{a} vs {b} which is better India {y}",
    "{a} vs {b} full comparison India {y}",
]

# ── Auto price-bracket topics (generated fresh each run) ─────────
PRICE_TOPICS_TMPL = {
    "smartphone": [
        ("best 5G phone under {p} India {y}", ["5G phone", "India"]),
        ("best phone under {p} India {y}",    ["phone", "India"]),
        ("best camera phone under {p} India {y}", ["camera phone", "India"]),
        ("best gaming phone under {p} India {y}", ["gaming phone", "India"]),
    ],
    "laptop": [
        ("best laptop under {p} India {y}",         ["laptop", "India"]),
        ("best gaming laptop under {p} India {y}",  ["gaming laptop", "India"]),
        ("best laptop for students under {p} India {y}", ["student laptop", "India"]),
    ],
    "earphones": [
        ("best earphones under {p} India {y}",      ["earphones", "India"]),
        ("best TWS earbuds under {p} India {y}",    ["TWS earbuds", "India"]),
        ("best ANC earphones under {p} India {y}",  ["ANC earphones", "India"]),
    ],
    "headphones": [
        ("best headphones under {p} India {y}",     ["headphones", "India"]),
        ("best ANC headphones under {p} India {y}", ["ANC headphones", "India"]),
    ],
    "smartwatch": [
        ("best smartwatch under {p} India {y}",     ["smartwatch", "India"]),
        ("best smartwatch with calling under {p} India {y}", ["calling smartwatch", "India"]),
    ],
    "powerbank": [
        ("best power bank under {p} India {y}",     ["power bank", "India"]),
        ("best fast charging power bank under {p} India {y}", ["fast charging", "India"]),
    ],
    "airpods": [],
}

PRICE_BRACKETS = {
    "smartphone":  ["₹8000",  "₹10000", "₹12000", "₹15000", "₹20000",
                    "₹25000", "₹30000", "₹40000", "₹50000"],
    "laptop":      ["₹30000", "₹40000", "₹50000", "₹60000", "₹70000", "₹80000"],
    "earphones":   ["₹500",   "₹1000",  "₹1500",  "₹2000",  "₹3000",  "₹5000"],
    "headphones":  ["₹2000",  "₹3000",  "₹5000",  "₹10000"],
    "smartwatch":  ["₹2000",  "₹3000",  "₹5000",  "₹10000"],
    "powerbank":   ["₹1000",  "₹1500",  "₹2000"],
    "airpods":     [],
}

# ─────────────────────────────────────────────────────────────────
def load_auto_cache():
    if os.path.exists(AUTO_TOPICS_CACHE):
        try:
            with open(AUTO_TOPICS_CACHE) as f:
                return json.load(f)
        except Exception:
            pass
    return {"topics": [], "generated_at": ""}

def save_auto_cache(data):
    try:
        with open(AUTO_TOPICS_CACHE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception:
        pass

def fetch_google_trends_india():
    """Fetch today's trending search topics from Google Trends India."""
    trends = []
    try:
        r = requests.get(GOOGLE_TRENDS_IN, headers=HEADERS, timeout=10)
        root = ET.fromstring(r.content)
        for item in root.findall(".//item"):
            t = item.find("title")
            if t is not None and t.text:
                trends.append(t.text.strip())
    except Exception as ex:
        print("[Trends] Failed: " + str(ex))
    return trends[:40]

def extract_products_from_rss(cat):
    """
    Scan RSS feeds and extract real product model names for the category.
    Returns list of unique (product_name, source) tuples.
    """
    patterns = BRAND_PATTERNS.get(cat, [])
    if not patterns:
        return []
    feeds = ALL_RSS[:]
    random.shuffle(feeds)
    found = {}  # product → source
    for fname, furl in feeds[:30]:
        arts = fetch_rss(fname, furl)
        for a in arts:
            text = a["title"] + " " + a.get("description", "")
            for pat in patterns:
                for m in re.findall(pat, text, re.IGNORECASE):
                    m = m.strip()
                    if len(m) > 6 and m not in found:
                        found[m] = fname
        if len(found) >= 20:
            break
    return list(found.items())[:15]

def generate_dynamic_topics():
    """
    Auto-topic engine — runs on every call, refreshes cache every 6 hrs.
    Priority order of generated topics:
      1. Google Trends India (highest engagement potential)
      2. RSS product review topics
      3. RSS product vs topics
      4. Price-bracket buying guides
    """
    cache = load_auto_cache()
    refresh = True
    if cache.get("generated_at") and cache.get("topics"):
        try:
            age = datetime.datetime.now() - datetime.datetime.fromisoformat(cache["generated_at"])
            if age.total_seconds() < CACHE_TTL_HOURS * 3600:
                refresh = False
        except Exception:
            pass

    if not refresh:
        print("[AutoTopics] Cache valid (" + str(len(cache["topics"])) + " topics). Skipping refresh.")
        return cache.get("topics", [])

    print("[AutoTopics] Refreshing topics from Google Trends + RSS...")
    year = str(datetime.datetime.now().year)
    new_topics = []

    # 1 ── Google Trends India → map to category
    trends = fetch_google_trends_india()
    print("[AutoTopics] Google Trends fetched: " + str(len(trends)) + " items")
    for trend in trends:
        tl = trend.lower()
        for cat, cdata in CAT.items():
            if any(kw in tl for kw in cdata["detect"]):
                kws = [w for w in re.findall(r"[a-z0-9]+", tl) if len(w) > 3][:2]
                new_topics.append({
                    "t": trend + " India " + year,
                    "k": kws or [cat],
                    "cat": cat,
                    "source": "google_trends",
                    "priority": 1,
                })
                break

    # 2 ── RSS product extraction → review + worth-buying topics
    for cat in CAT.keys():
        products = extract_products_from_rss(cat)
        gens = TOPIC_GENS.get(cat, [])
        print("[AutoTopics] " + cat + ": extracted " + str(len(products)) + " products from RSS")
        for prod, src in products:
            for gen in gens:
                new_topics.append({
                    "t": gen(prod, year),
                    "k": [prod.split()[0].lower(), "India"],
                    "cat": cat,
                    "source": "rss_review",
                    "priority": 2,
                })

        # 3 ── Pair products → vs topics
        if len(products) >= 2:
            pairs = [(products[i][0], products[j][0])
                     for i in range(min(4, len(products)))
                     for j in range(i + 1, min(5, len(products)))]
            for a, b in pairs[:5]:
                tmpl = random.choice(VS_TEMPLATES)
                new_topics.append({
                    "t": tmpl.format(a=a, b=b, y=year),
                    "k": [a.split()[0].lower(), b.split()[0].lower()],
                    "cat": cat,
                    "source": "rss_vs",
                    "priority": 2,
                })

    # 4 ── Price-bracket buying guides
    for cat, templates in PRICE_TOPICS_TMPL.items():
        for price in PRICE_BRACKETS.get(cat, []):
            for tmpl, kws in templates:
                new_topics.append({
                    "t": tmpl.format(p=price, y=year),
                    "k": kws,
                    "cat": cat,
                    "source": "price_bracket",
                    "priority": 3,
                })

    # 5 ── Extra trend feeds (Bing, Reddit, DDG RSS)
    print("[AutoTopics] Mining extra trend RSS feeds...")
    for fname, furl in EXTRA_TREND_FEEDS:
        try:
            r2 = requests.get(furl, headers=HEADERS, timeout=8)
            if r2.status_code == 200:
                root2 = ET.fromstring(r2.content)
                for item2 in root2.findall(".//item")[:6]:
                    t2 = item2.find("title")
                    if t2 is not None and t2.text:
                        raw = re.sub(r"<[^>]+>", "", t2.text).strip()
                        tl2 = raw.lower()
                        for cat2, cdata2 in CAT.items():
                            if any(kw in tl2 for kw in cdata2["detect"]):
                                kws2 = [w for w in re.findall(r"[a-z0-9]+", tl2) if len(w) > 3][:2]
                                clean = re.sub(r"\s+", " ", raw).strip()
                                if "india" not in clean.lower():
                                    clean += " India"
                                if year not in clean:
                                    clean += " " + year
                                new_topics.append({
                                    "t": clean[:120],
                                    "k": kws2 or [cat2],
                                    "cat": cat2,
                                    "source": "extra_rss",
                                    "priority": 1,
                                })
                                break
        except Exception:
            pass

    # 6 ── NewsAPI trending headline mining
    print("[AutoTopics] Mining NewsAPI for trending headlines...")
    for nq in NEWSAPI_TREND_QUERIES:
        try:
            r3 = requests.get("https://newsapi.org/v2/everything",
                params={"q": nq, "language": "en", "sortBy": "publishedAt",
                        "pageSize": 5, "apiKey": NEWS_API_KEY}, timeout=10)
            d3 = r3.json()
            if d3.get("status") == "ok":
                for art in d3.get("articles", [])[:5]:
                    raw3 = (art.get("title") or "").strip()
                    tl3  = raw3.lower()
                    for cat3, cdata3 in CAT.items():
                        if any(kw in tl3 for kw in cdata3["detect"]):
                            kws3 = [w for w in re.findall(r"[a-z0-9]+", tl3) if len(w) > 3][:2]
                            clean3 = re.sub(r"\s+", " ", raw3).strip()
                            if "india" not in clean3.lower():
                                clean3 += " India"
                            if year not in clean3:
                                clean3 += " " + year
                            new_topics.append({
                                "t": clean3[:120],
                                "k": kws3 or [cat3],
                                "cat": cat3,
                                "source": "newsapi_trend",
                                "priority": 1,
                            })
                            break
        except Exception:
            pass

    # 7 ── pytrends related queries (optional — needs pip install pytrends)
    try:
        from pytrends.request import TrendReq
        pt = TrendReq(hl="en-IN", tz=330, timeout=(10, 30))
        for kw_group in ["best smartphone india", "best earphones india", "best laptop india"]:
            try:
                pt.build_payload([kw_group], timeframe="now 7-d", geo="IN")
                rel = pt.related_queries()
                df  = rel.get(kw_group, {}).get("rising")
                if df is not None and not df.empty:
                    for q_row in df["query"].tolist()[:5]:
                        q_tl = q_row.lower()
                        for cat4, cdata4 in CAT.items():
                            if any(kw in q_tl for kw in cdata4["detect"]):
                                new_topics.append({
                                    "t": q_row.strip() + " India " + year,
                                    "k": [w for w in q_tl.split() if len(w) > 3][:2],
                                    "cat": cat4,
                                    "source": "pytrends",
                                    "priority": 1,
                                })
                                break
                time.sleep(1)
            except Exception:
                pass
        print("[AutoTopics] pytrends done")
    except ImportError:
        print("[AutoTopics] pytrends not installed — skipping (pip install pytrends)")

    # Deduplicate within generated pool
    seen, deduped = set(), []
    for t in new_topics:
        key = t["t"].lower().strip()
        if key not in seen:
            seen.add(key)
            deduped.append(t)

    cache = {"topics": deduped, "generated_at": datetime.datetime.now().isoformat()}
    save_auto_cache(cache)
    print("[AutoTopics] Done — " + str(len(deduped)) + " unique topics cached.")
    return deduped


def pick_search_story(log, used_in_run):
    print("\n[Search] Auto-picking topic from RSS + Trends engine...")

    used_titles  = {e.get("title","").lower().strip()        for e in log}
    used_topics  = {e.get("search_topic","").lower().strip() for e in log}
    combined_used = used_titles | used_topics | {t.lower().strip() for t in used_in_run}

    # --- Live auto-generated topics ---
    live_topics = generate_dynamic_topics()

    # --- Static fallback pool ---
    static_topics = []
    for pcat in ["smartphone", "laptop"]:
        for t in CAT[pcat]["search_topics"]:
            static_topics.append({"t": t["t"], "k": t["k"], "cat": pcat,
                                   "source": "static", "priority": 4})
    for cat, data in CAT.items():
        if cat in ("smartphone", "laptop"):
            continue
        if not should_post_cat(log, cat):
            continue
        for t in data.get("search_topics", []):
            static_topics.append({"t": t["t"], "k": t["k"], "cat": cat,
                                   "source": "static", "priority": 4})

    # Merge and filter: live first, then static
    all_options = []
    seen_keys   = set()
    for t in live_topics + static_topics:
        key = t["t"].lower().strip()
        if key in combined_used or key in seen_keys:
            continue
        cat = t.get("cat", "smartphone")
        if cat not in ("smartphone", "laptop") and not should_post_cat(log, cat):
            continue
        seen_keys.add(key)
        all_options.append(t)

    # Last resort: only run-dedup (allow cross-run repeats from static)
    if not all_options:
        print("[Search] All unique topics used — falling back to run-dedup only.")
        run_used_keys = {t.lower().strip() for t in used_in_run}
        for t in static_topics:
            key = t["t"].lower().strip()
            if key not in run_used_keys:
                all_options.append(t)

    if not all_options:
        return None

    # Sort by priority (1=Trends, 2=RSS, 3=Price, 4=Static), then shuffle within tier
    all_options.sort(key=lambda x: x.get("priority", 4))
    top_priority  = all_options[0].get("priority", 4)
    top_tier      = [t for t in all_options if t.get("priority", 4) == top_priority]
    random.shuffle(top_tier)
    chosen = top_tier[0]

    topic      = chosen["t"]
    chosen_cat = chosen.get("cat", "smartphone")
    used_in_run.add(topic.lower().strip())
    print("Topic [" + chosen_cat + "] (" + chosen.get("source","?") + "): " + topic)

    ctx   = get_rss_context(chosen.get("k", [topic.split()[0]]))
    arts  = fetch_newsapi(topic)
    extra = arts[0].get("description","") if arts else ""

    return {
        "title":        topic,
        "description":  extra,
        "url":          "https://technewswithai.blogspot.com",
        "source":       "Tech News With AI — " + chosen.get("source","auto"),
        "published":    datetime.datetime.now().isoformat(),
        "specs":        "",
        "search_topic": topic,
        "keywords":     chosen.get("k", [topic.split()[0]]),
        "rss_context":  ctx,
        "category":     chosen_cat,
    }

def fix_bold(text):
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*",     r"<em>\1</em>",          text)
    text = re.sub(r"```html",       "",                       text)
    text = re.sub(r"```",           "",                       text)
    return text.strip()

# ================================================================
# STEP 1: GROQ TECHNICAL DRAFT  (v12 — Full SEO upgrade)
# ================================================================

# ── Internal link map: brand/category → your blog label URL ──────
INTERNAL_LINKS = {
    # Brands — smartphones
    "apple":      "https://technewswithai.blogspot.com/search/label/Apple",
    "samsung":    "https://technewswithai.blogspot.com/search/label/Samsung",
    "oneplus":    "https://technewswithai.blogspot.com/search/label/OnePlus",
    "xiaomi":     "https://technewswithai.blogspot.com/search/label/Xiaomi",
    "redmi":      "https://technewswithai.blogspot.com/search/label/Xiaomi",
    "poco":       "https://technewswithai.blogspot.com/search/label/Xiaomi",
    "realme":     "https://technewswithai.blogspot.com/search/label/Realme",
    "oppo":       "https://technewswithai.blogspot.com/search/label/OPPO",
    "vivo":       "https://technewswithai.blogspot.com/search/label/Vivo",
    "iqoo":       "https://technewswithai.blogspot.com/search/label/Vivo",
    "nothing":    "https://technewswithai.blogspot.com/search/label/Nothing",
    "google":     "https://technewswithai.blogspot.com/search/label/Google",
    "pixel":      "https://technewswithai.blogspot.com/search/label/Google",
    "motorola":   "https://technewswithai.blogspot.com/search/label/Motorola",
    "nokia":      "https://technewswithai.blogspot.com/search/label/Nokia",
    "honor":      "https://technewswithai.blogspot.com/search/label/Honor",
    "huawei":     "https://technewswithai.blogspot.com/search/label/Huawei",
    "infinix":    "https://technewswithai.blogspot.com/search/label/Infinix",
    "tecno":      "https://technewswithai.blogspot.com/search/label/Tecno",
    # Brands — laptops
    "dell":       "https://technewswithai.blogspot.com/search/label/Dell",
    "hp":         "https://technewswithai.blogspot.com/search/label/HP",
    "lenovo":     "https://technewswithai.blogspot.com/search/label/Lenovo",
    "asus":       "https://technewswithai.blogspot.com/search/label/ASUS",
    "acer":       "https://technewswithai.blogspot.com/search/label/Acer",
    "msi":        "https://technewswithai.blogspot.com/search/label/Laptops",
    "razer":      "https://technewswithai.blogspot.com/search/label/Laptops",
    "macbook":    "https://technewswithai.blogspot.com/search/label/Apple",
    # Brands — audio
    "boat":       "https://technewswithai.blogspot.com/search/label/boAt",
    "noise":      "https://technewswithai.blogspot.com/search/label/Noise",
    "jbl":        "https://technewswithai.blogspot.com/search/label/Earphones",
    "sony":       "https://technewswithai.blogspot.com/search/label/Sony",
    "bose":       "https://technewswithai.blogspot.com/search/label/Headphones",
    "sennheiser": "https://technewswithai.blogspot.com/search/label/Headphones",
    "anker":      "https://technewswithai.blogspot.com/search/label/Earphones",
    "skullcandy": "https://technewswithai.blogspot.com/search/label/Earphones",
    # Brands — wearables / power
    "garmin":     "https://technewswithai.blogspot.com/search/label/Smartwatch",
    "amazfit":    "https://technewswithai.blogspot.com/search/label/Smartwatch",
    "fitbit":     "https://technewswithai.blogspot.com/search/label/Smartwatch",
    # Categories
    "smartphone":  "https://technewswithai.blogspot.com/search/label/Smartphones",
    "laptop":      "https://technewswithai.blogspot.com/search/label/Laptops",
    "earphone":    "https://technewswithai.blogspot.com/search/label/Earphones",
    "headphone":   "https://technewswithai.blogspot.com/search/label/Headphones",
    "airpods":     "https://technewswithai.blogspot.com/search/label/AirPods",
    "powerbank":   "https://technewswithai.blogspot.com/search/label/Power+Bank",
    "smartwatch":  "https://technewswithai.blogspot.com/search/label/Smartwatch",
}

def build_internal_link_instructions(cat):
    """
    Returns the internal-link rule block for the current category.
    Tells the AI exactly which brand names to hyperlink and to what URL.
    """
    lines = [
        "INTERNAL LINKS — YOUR BLOG ONLY (technewswithai.blogspot.com):",
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
        '  "...the <a href="https://technewswithai.blogspot.com/search/label/boAt" target="_blank">boAt</a> Airdopes 141..."',
        '  "...check our full <a href="https://technewswithai.blogspot.com/search/label/Earphones" target="_blank">earphones reviews</a>..."',
        '  "...more on <a href="https://technewswithai.blogspot.com" target="_blank">Tech News With AI</a>..."',
    ]
    return "\n".join(lines)


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
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MANDATORY ARTICLE STRUCTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[A] H1 TITLE — SEO FORMAT:
    Best [Product] Under ₹[Price] in India ([Year]): Top 5 Picks Tested

[B] HOOK INTRO (2 lines only, problem + solution):
    Line 1: State the exact problem Indian buyers face.
    Line 2: Tell them this article solves it. Include primary keyword.
    → Primary keyword MUST appear in first 100 words.

[C] TABLE OF CONTENTS (plain border, no colours):
""" + TOC_HTML + """

[D] QUICK COMPARISON TABLE (id="comparison-table", real specs, no colour headers):
    Columns vary by category:
    • Earphones/Headphones: Model | Driver | ANC | Battery | Codec | Price
    • Smartphones: Model | Chip | RAM | Camera | Battery | Price
    • Laptops: Model | CPU | RAM | Storage | Display | Price
    • Smartwatch: Model | Display | Battery | GPS | SpO2 | Price
    • Power Bank: Model | Capacity | Max Watt | Ports | Weight | Price

[E] PER-PRODUCT SECTION (repeat EXACTLY for all 5 products — same H3 order):

<h2 id="product-N">N. [Brand + Model] — [10-word honest verdict]</h2>

  SPECS BOX (immediately under H2):
""" + SPECS_BOX_HTML + """

  <h3>Is the Design Worth It?</h3>
  → 3-5 bullet points. Max 12 words per bullet.
  → Real-life line: "comfortable during my 45-min Bengaluru metro commute"

  <h3>How Does It Actually [Perform / Sound / Feel]?</h3>
  → Use specific words: deep bass, clear vocals, 42dB ANC, 28ms latency
  → NEVER use: good, nice, amazing, great, excellent
  → Add numbers: battery hours, dB, ms, Hz, MP, W

  <h3>Battery — Does It Last Your Day?</h3>
  → Real-life test line: "lasted through IPL match + 2 hr college lecture"
  → State hours precisely: "32 hrs total (6 hrs earbuds + 4 charges from case)"

  <h3>Pros & Cons</h3>
""" + PROS_CONS_HTML + """

  <p><strong>🎯 Best For:</strong> [specific target user — e.g., "gym users who sweat heavily"]</p>
  <p><strong>💬 Mini Verdict:</strong> [1 honest sentence. Better than X. Cheaper than Y.]</p>
  <p>📌 <em>Check the latest price on
  <a href="https://technewswithai.blogspot.com/search/label/[Category]" target="_blank">Tech News With AI</a>.</em></p>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[F] ADVANCED ENGAGEMENT ELEMENTS (add throughout article):

  ① CURIOSITY HOOK after every H2 product section opener:
     "Here is what surprised me about this one."
     "This is where it gets better than the competition."
     "Most people miss this detail — I almost did too."

  ② READER ADDRESS (ask the reader directly — 1 per section):
     "If you are a student on a tight budget, this matters."
     "If you commute every day, you will love this."
     "Be honest — how often has your phone died at 2pm?"

  ③ SOCIAL PROOF TRIGGER (creates trust — 1 per article):
     "Thousands of Indians have already switched to this."
     "This model sold out in 2 days on Flipkart last sale."

  ④ SCARCITY / URGENCY LINE (add near price sections):
     "Prices tend to spike after big launches — check current price."
     "Stock was limited during last Flipkart sale — worth bookmarking."

  ⑤ COMPARISON ANCHOR (makes value clear):
     "Competitors at the same price give you less battery."
     "You would pay ₹2000 more for the same ANC from Sony."

  ⑥ PATTERN INTERRUPT between long sections (every 3rd H2):
     Add a bold callout box (HTML div, plain border):
     <div style="border:1px solid #ddd;padding:12px;margin:16px 0;">
     <strong>💡 Quick Tip:</strong> [1 actionable sentence]
     </div>

  ⑦ NUMBERED TAKEAWAY before final verdict:
     <h3>Top 3 Things to Remember Before You Buy</h3>
     <ol><li>...</li><li>...</li><li>...</li></ol>

[G] TRANSITION LINES between every product section:
    Use smooth bridges. Examples:
    "Now let us look at a better option if you want ANC."
    "If budget is tight, the next pick is made for you."
    "So far so good — but this next one changes things."

[G] FINAL VERDICT (id="final-verdict"):
<h2 id="final-verdict">🏆 Final Verdict — Which One Should You Buy?</h2>
""" + VERDICT_TABLE_HTML + """
    → Declare a clear winner. State WHY in one sentence.
    → Add CTA: "Read more [category] reviews on
       <a href="https://technewswithai.blogspot.com/search/label/[Category]" target="_blank">Tech News With AI</a>."

[H] FAQ (id="faq") — 3 questions minimum, question-based H3 subheadings:
<h3>Which is the best [product] under ₹[price] in India 2026?</h3>
<h3>Is [Product Name] worth buying in 2026?</h3>
<h3>What is the difference between [X] and [Y]?</h3>
"""

# ── Writing rules injected into every prompt ─────────────────────
WRITING_RULES = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WRITING & SEO RULES (apply to EVERY section)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WORD COUNT: Minimum 4000 words. More depth = better Google ranking.
SENTENCE LENGTH: Max 15 words per sentence. Short. Punchy. Clear.
FORMAT: Bullet points — NOT long paragraphs. Paragraphs max 3 lines.
SPECIFICITY: Never write "good sound". Write "deep bass with 10mm driver, clear vocals above 2kHz".
DATA: Always include numbers — hours, dB, ms latency, Hz refresh, MP camera, W charging, mAh, g weight.
COMPARISON: Use "better than X", "cheaper than Y by ₹NNN", "unlike Z which lacks ANC".
REAL LIFE: One Indian usage line per H3:
  → "survived my 1.5 hr Bengaluru metro ride with zero discomfort"
  → "handled PUBG Mobile for 3 hrs without thermal throttle"
  → "battery lasted through full IPL match + Hotstar binge after"
  → "never slipped during 40-min morning run"
CLIFFHANGER: End each product section with a 1-line teaser:
  → "But wait — the next pick does all this for ₹500 less."
  → "If that impressed you, the next one will genuinely surprise you."
STRUCTURE: H2 = product or major topic. H3 = question-based subheading. Never skip.
UNIQUE: Every product 100% unique text. Zero repeated sentences across article.
CATEGORY ACCURACY (STRICT):
  → Earphones/Headphones: ANC dB, codec (AAC/aptX/LDAC), driver mm, IP rating, latency ms
  → Smartphones: display type (AMOLED/IPS), processor name, RAM GB, camera MP, battery mAh, fast charge W
  → Laptops: CPU name+gen, RAM GB, SSD GB+type, display nits, battery Wh, weight kg
  → Smartwatch: display type+size, battery days, built-in GPS, SpO2/ECG, ATM rating
  → Power Bank: mAh real capacity, input W, output W, port count, weight g, PD/QC support
BOLD: <strong> on price, battery hours, ANC level, model names, key specs.

━━ ENGAGEMENT ELEMENTS (MANDATORY — ADD IN EVERY ARTICLE) ━━

① DID YOU KNOW BOX (add once, after section 3):
<div style="border:1px solid #ddd;padding:14px 16px;margin:16px 0;">
<strong>💡 Did You Know?</strong><br/>
[Surprising India-specific stat — e.g., "India became the 2nd largest TWS earbuds market in Asia in 2026."]
</div>

② QUICK POLL (add once, right after the comparison table):
<div style="border:1px solid #ddd;padding:14px 16px;margin:16px 0;">
<strong>📊 Quick Poll — Tell Us!</strong><br/>
Which matters most to you when buying [category]?<br/>
• 🔋 Battery life &nbsp;|&nbsp; 🔊 Sound / Performance &nbsp;|&nbsp; 💰 Price &nbsp;|&nbsp; 🎨 Design<br/>
<em>Drop your answer in the comments below 👇</em>
</div>

③ DATA CALLOUT BOX (1 per product — highlight the single most impressive spec):
<div style="border-left:3px solid #333;padding:10px 14px;margin:10px 0;background:#fafafa;">
<strong>[Key stat — e.g., "42dB ANC depth"]</strong> — [1 line: why this matters for Indian users]
</div>

④ ENGAGEMENT CTA (after every 2nd product):
<p>👉 <em>Finding this useful? Share with a friend who is confused about which [category] to buy!</em></p>

⑤ COMMENT HOOK (just before author bio, end of article):
<p style="font-size:15px;"><strong>💬 Which one would YOU pick?</strong> Drop your choice in the comments — I read every single one!</p>

NEVER: markdown bold, "good/nice/amazing/great/excellent", "In conclusion", "To summarize",
       two consecutive sections starting same way, generic sentences applicable to any product.
MINIMUM: 4000 words total.
"""


def groq_draft(story, is_search):
    client   = Groq(api_key=GROQ_API_KEY)
    cat      = story.get("category", "smartphone")
    struct   = CAT.get(cat, CAT["smartphone"])
    sections = "\n".join(struct["sections"])
    link_rules = build_internal_link_instructions(cat)

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
                "BUYING GUIDE.\n"
                "- List exactly 5 real products with full real India specs and prices.\n"
                "- Follow the MANDATORY ARTICLE STRUCTURE below for every product.\n"
                "- Same H3 subheading order for all 5 products (consistent format).\n"
                "- Add specs box + Pros & Cons table for every product.\n"
                "- Add transition line between each product.\n"
                "- Comparison table at top. Final verdict table at end.\n"
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
            "Write a comprehensive SEO-optimised guide for Indians searching: '" + topic + "'\n\n"
            "ARTICLE TYPE: " + mode + "\n\n"
            "REAL DATA FROM RSS AND REVIEW SOURCES:\n"
            + (ctx or "Use your latest India market 2026 knowledge.") + "\n\n"
            + BUYING_GUIDE_STRUCTURE + "\n\n"
            + WRITING_RULES + "\n\n"
            + link_rules + "\n\n"
            "WRITE THESE 12 SECTIONS:\n" + sections + "\n\n"
            "SEO CHECKLIST:\n"
            "✓ H1 contains exact search query\n"
            "✓ Primary keyword in first 100 words\n"
            "✓ Keyword in at least 3 H2 headings\n"
            "✓ Question-based H3 subheadings (improves SEO)\n"
            "✓ Real ₹ prices — Flipkart/Amazon India\n"
            "✓ Real product names — never invent specs\n"
            "✓ h1 h2 h3 p ul li table — HTML only, NEVER markdown\n"
            "✓ <strong> for specs, prices, key data\n"
            "✓ Brand names hyperlinked to your blog label pages only\n"
            "✓ FAQ section: first question = exact search query\n"
            "Write now:"
        )
    else:
        prompt = (
            "Write a detailed SEO-optimised article about: " + story["title"] + "\n"
            "CATEGORY: " + cat.upper() + "\n"
            "SOURCE: " + story["source"] + "\n"
            "REAL SPECS:\n" + (story.get("specs") or "Use your knowledge for this device.") + "\n"
            "DESCRIPTION: " + story.get("description", "") + "\n\n"

            "MANDATORY STRUCTURE:\n"
            "1. H1 — device name + India + 2026 + benefit keyword\n"
            "2. Hook intro — 2 lines: problem + solution. Primary keyword in first 100 words.\n"
            "3. Table of Contents — plain border, no colour:\n"
            + TOC_HTML + "\n"
            "4. Specs box for this device:\n"
            + SPECS_BOX_HTML + "\n"
            "5. Pros & Cons table — plain border, no colour:\n"
            + PROS_CONS_HTML + "\n"
            "6. Write 12 sections using H2/H3 hierarchy.\n"
            "   H2 = main topic. H3 = question-based subheading (improves SEO).\n\n"

            + WRITING_RULES + "\n\n"
            + link_rules + "\n\n"

            "WRITE THESE 12 SECTIONS:\n" + sections + "\n\n"
            "SEO CHECKLIST:\n"
            "✓ H1 has device name + India + 2026\n"
            "✓ Primary keyword in first 100 words\n"
            "✓ Question-based H3 subheadings\n"
            "✓ Real ₹ prices\n"
            "✓ <strong> for key specs\n"
            "✓ Brand names hyperlinked to your blog label pages only\n"
            "✓ Bullet points — not long paragraphs\n"
            "✓ Real-life India usage line in every section\n"
            "✓ FAQ with 7 questions Indians actually search\n"
            "✓ Strong final verdict with clear winner + CTA\n"
            "Write now:"
        )
    r = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=8000, temperature=0.7,
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
        '<p style="font-size:12px;color:#999;"><em>Published: ' + today + ' &bull; technewswithai.blogspot.com</em></p>'
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
        "• Table of Contents and all anchor links\n"
        "• All H1, H2, H3 headings\n"
        "• All internal links to technewswithai.blogspot.com\n"
        "• 'Best For' lines, 'Mini Verdict' lines, CTA lines\n\n"

        "━━━ FOR EVERY SECTION, DO ALL OF THESE ━━━\n\n"
        "① PERSONAL HOOK — start with your real experience:\n"
        "   Earphones: 'I wore these for my entire Bengaluru metro ride — here is what I noticed.'\n"
        "   Phone:     'I have been testing phones at this price for the last 3 months.'\n"
        "   Laptop:    'After a full week of coding and Netflix on this machine —'\n"
        "   Powerbank: 'My phone died mid-exam call. That is why I tested every power bank here.'\n"
        "   Watch:     'I wore this for 2 weeks straight — morning runs, office, gym, sleep.'\n\n"
        "② INDIA REAL-LIFE LINE — make every spec mean something:\n"
        "   ❌ Bad:  '5000mAh battery'\n"
        "   ✅ Good: '<strong>5000mAh</strong> = full IPL match + 6 hrs college + evening commute'\n"
        "   ❌ Bad:  '30hr battery'\n"
        "   ✅ Good: '<strong>30 hrs total</strong> = 5 days of my office commute without charging'\n\n"
        "③ HONEST REACTION (1 line per section):\n"
        "   'Genuinely surprised me for this price.'\n"
        "   'Honestly? I expected better from this brand.'\n"
        "   'This is where it gets interesting.'\n\n"
        "④ INDIA ADVICE (specific, actionable):\n"
        "   'Grab this during Flipkart Big Billion Days — extra ₹500 off bank discount.'\n"
        "   '8GB variant is worth ₹1500 more. Trust me on this one.'\n\n"
        "⑤ ONE LIKE + ONE DISLIKE (honest, product-specific):\n"
        "   '✅ Love: deep bass response on the 10mm driver.'\n"
        "   '❌ Dislike: call quality drops in wind above 20 kmph.'\n\n"

        "━━━ WRITING STYLE ━━━\n"
        "• Sentences: max 15 words. Short. Punchy.\n"
        "• Bullet points — not long paragraphs\n"
        "• Indian English: value for money, decent enough, not bad at all\n"
        "• Connectors: look, here is the thing, honestly, but wait, catch is\n"
        "• Questions: 'But does it hold up in real use?'\n"
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
        "• NEVER two consecutive sections starting the same way\n"
        "• NEVER repeat same sentence in different sections\n"
        "• NEVER remove or change any HTML table\n"
        "• NEVER link to any website except technewswithai.blogspot.com\n"
        "• NEVER write generic sentences that could apply to any product\n\n"

        "━━━ FINAL CHECKS ━━━\n"
        "✓ Minimum 4000 words\n"
        "✓ Hook intro — problem + solution in first 2 lines\n"
        "✓ Primary keyword in first 100 words\n"
        "✓ All 5 products have: specs box + pros/cons + best for + mini verdict + CTA\n"
        "✓ Strong final verdict with clear winner\n"
        "✓ Author bio added at the very end\n\n"

        "ADD AUTHOR BIO as absolute last element:\n"
        + author_bio + "\n\n"

        "NOW REWRITE — every word human, every spec accurate:\n\n"
        + draft
    )

    r = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=8000, temperature=0.88,
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
    save_log(log, title, url, words, atype, story.get("category","general"),
             story.get("search_topic",""))
    return True

# ================================================================
# MAIN
# ================================================================
def main():
    print("================================================")
    print(" TECH NEWS WITH AI - AUTO BLOG v13.0 ADVANCED")
    print(" Daily: 1 News + 2 Auto-generated Search Topics")
    print(" Topics: Google Trends + RSS extraction + Price brackets")
    print(" Content: 4000+ words, Engagement elements, Bullet-first")
    print(" technewswithai.blogspot.com")
    print("================================================")

    log         = load_log()
    used_in_run = set()
    success     = 0

    # Article 1 — Latest RSS News (phone/laptop priority)
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

    # Article 3 — Google Search Topic (different topic guaranteed)
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
