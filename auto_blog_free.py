# TECH NEWS WITH AI - AUTO BLOG v14.0 ADVANCED FINAL
# technewswithai.blogspot.com - Mallikarjun R, Bengaluru
# ================================================================
# SCHEDULE:
#   Daily   → 1 Smartphone/Laptop news + 2 Google search topics
#   Weekly  → Earphones Headphones AirPods PowerBank Smartwatch
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
    fresh, trending search topics for the given category.
    Returns list of {"t": "...", "k": ["...", "..."]} dicts.
    """
    try:
        from groq import Groq
        client = Groq(api_key=GROQ_API_KEY)

        headlines = fetch_rss_headlines_for_cat(cat, max_headlines=25)
        if not headlines:
            return []

        year = datetime.datetime.now().year
        used_list = "\n".join(list(used_combined)[:40]) if used_combined else "None yet"
        templates = "\n".join(TOPIC_TEMPLATES.get(cat, TOPIC_TEMPLATES["smartphone"]))
        headlines_text = "\n".join(f"- {h}" for h in headlines)

        prompt = (
            f"You are an India tech SEO expert. Category: {cat.upper()}\n\n"
            f"TODAY'S LIVE RSS HEADLINES (use these to find trending topics):\n"
            f"{headlines_text}\n\n"
            f"TOPIC TEMPLATES (use as format guides, fill with real data from headlines):\n"
            f"{templates}\n\n"
            f"ALREADY POSTED TOPICS (DO NOT repeat these):\n"
            f"{used_list}\n\n"
            f"TASK: Generate exactly {count} fresh, unique, trending search topics for Indian buyers in {year}.\n\n"
            f"Rules:\n"
            f"- Topics must be based on what is trending in the headlines above\n"
            f"- Each topic must be a real Google search query Indians type\n"
            f"- Mix of: buying guides (best X under ₹Y), comparisons (X vs Y), worth-it (is X worth buying)\n"
            f"- Include real product names from the headlines\n"
            f"- Include India {year} in every topic\n"
            f"- Each topic must be completely different from the others\n"
            f"- NEVER repeat any topic from the 'Already Posted' list above\n\n"
            f"OUTPUT FORMAT — respond ONLY with valid JSON, nothing else:\n"
            f'[{{"t": "topic text here", "k": ["keyword1", "keyword2"]}}, ...]\n\n'
            f"Generate {count} topics now:"
        )

        r = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1200,
            temperature=0.75,
        )
        raw = r.choices[0].message.content.strip()
        # Strip any markdown fences
        raw = re.sub(r"```json|```", "", raw).strip()
        # Extract JSON array
        m = re.search(r"\[.*\]", raw, re.DOTALL)
        if not m:
            return []
        topics = json.loads(m.group(0))
        # Validate + filter
        valid = []
        for t in topics:
            if isinstance(t, dict) and "t" in t and "k" in t:
                if t["t"] not in used_combined:
                    valid.append({"t": str(t["t"]), "k": [str(k) for k in t["k"]]})
        print(f"[DynamicTopics] Generated {len(valid)} fresh topics for [{cat}]")
        return valid
    except Exception as e:
        print(f"[DynamicTopics] Failed for [{cat}]: {e}")
        return []


    if os.path.exists("posted_articles.json"):
        try:
            with open("posted_articles.json") as f:
                return json.load(f)
        except Exception:
            pass
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
            model="llama-3.3-70b-versatile",
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
def build_image_block(alt_text, caption="", position="product"):
    """
    Blogger-safe image placeholder.
    Replace src with your actual uploaded image URL in Blogger.
    Google Discover needs real 1200px images — add via Blogger image tool.
    """
    slug = re.sub(r'[^a-z0-9]+', '-', alt_text.lower())[:40]
    return (
        f'<figure style="margin:16px 0;text-align:center;">'
        f'<!-- REPLACE WITH REAL IMAGE: Upload 1200x628px to Blogger, '
        f'alt="{alt_text}" -->'
        f'<img src="https://via.placeholder.com/1200x628?text={slug}" '
        f'alt="{alt_text}" width="1200" height="628" '
        f'style="max-width:100%;height:auto;border-radius:6px;" '
        f'loading="lazy"/>'
        + (f'<figcaption style="font-size:12px;color:#666;margin-top:6px;">{caption}</figcaption>' if caption else '')
        + '</figure>\n'
    )

# ================================================================
# v14: SOCIAL SHARE BLOCK — WhatsApp, Telegram, Reddit, Quora
# ================================================================
def build_social_block(title, url="https://technewswithai.blogspot.com"):
    encoded_title = requests.utils.quote(title[:100])
    encoded_url   = requests.utils.quote(url)
    return (
        '<div style="border:1px solid #ddd;padding:16px;margin:24px 0;text-align:center;">'
        '<p style="margin:0 0 10px;font-size:14px;font-weight:bold;">📢 Found this helpful? Share it!</p>'
        '<p style="margin:0;font-size:13px;">'
        f'<a href="https://wa.me/?text={encoded_title}%20{encoded_url}" '
        'target="_blank" rel="noopener" style="margin:0 8px;color:#25d366;">📱 WhatsApp</a> | '
        f'<a href="https://t.me/share/url?url={encoded_url}&text={encoded_title}" '
        'target="_blank" rel="noopener" style="margin:0 8px;color:#0088cc;">✈️ Telegram</a> | '
        f'<a href="https://reddit.com/submit?url={encoded_url}&title={encoded_title}" '
        'target="_blank" rel="noopener" style="margin:0 8px;color:#ff4500;">🔗 Reddit</a> | '
        '<a href="https://technewswithai.blogspot.com" '
        'target="_blank" rel="noopener" style="margin:0 8px;color:#1a73e8;">🏠 More Reviews</a>'
        '</p></div>\n'
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
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MANDATORY ARTICLE STRUCTURE (v14 — AdSense + Traffic)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[A] H1 TITLE — CLICKBAIT-BUT-HONEST FORMAT:
    • Use "Top 5" or "Top 10" for lists
    • Use "vs" for comparisons
    • Use "Worth Buying?" for reviews
    • Include: India + year + price + benefit
    Examples:
      "Top 5 Earphones Under ₹2000 in India (2026): ANC Tested, Battery Ranked"
      "Stop Buying the Wrong Phone! Best 5G Picks Under ₹15000 India 2026"
      "I Tested 7 Laptops Under ₹40000. Only 3 Are Worth It — India 2026"

[B] HOOK INTRO (2 sentences MAX — MOBILE FRIENDLY):
    Sentence 1: State the exact pain point Indians face right now.
    Sentence 2: Promise this article solves it with a number (Top 5, 2 weeks tested).
    → Primary keyword in first 100 words — no exceptions.
    → SHORT paragraph. Max 3 lines. Indian readers use mobile phones.

[C] TABLE OF CONTENTS (plain border, no colours):
""" + TOC_HTML + """

[D] QUICK COMPARISON TABLE (id="comparison-table"):
    • Plain border only — no colour on headers
    • All specs must be real — never invent numbers
    • Add a "Rating" column (e.g., 8.5/10) for easy scanning
    Columns by category:
    • Earphones/Headphones: Model | Driver | ANC | Battery | Codec | Rating | Price
    • Smartphones: Model | Chip | RAM | Camera | Battery | Rating | Price
    • Laptops: Model | CPU | RAM | SSD | Display | Rating | Price
    • Smartwatch: Model | Display | Battery | GPS | Health | Rating | Price
    • Power Bank: Model | mAh | Max W | Ports | Weight | Rating | Price
    • AI topic: Tool | Free Plan | Best For | India Available | Rating

[E] PER-PRODUCT SECTION (repeat for all 5 products — SAME H3 order every time):

<h2 id="product-N">N. [Brand + Model] — [10-word honest verdict]</h2>

  IMAGE HINT (write this comment so blog editor knows where to add image):
  <!-- ADD IMAGE: [Product Name] 1200x628px — required for Google Discover -->

  SPECS BOX (immediately under H2 — no colour, plain border):
""" + SPECS_BOX_HTML + """

  <h3>Is the Design and Build Worth It?</h3>
  → 3-5 bullets. Max 12 words each. MOBILE READABLE.
  → One real-life India line per H3.

  <h3>How Does It Actually [Perform / Sound / Feel]?</h3>
  → Specific words: deep bass, clear vocals, 42dB ANC, 28ms latency
  → Add numbers: hours, dB, ms, Hz, MP, W
  → Long-tail keyword naturally in one bullet (e.g., "best ANC earphones under ₹2000 India")

  <h3>Battery Life — Does It Survive Your Full Day?</h3>
  → Exact hours: "32 hrs (6 earbuds + 4 case charges)"
  → India real-life: "lasted full IPL match + 2 hr college lecture"

  <h3>Pros & Cons</h3>
""" + PROS_CONS_HTML + """

  <p><strong>🎯 Best For:</strong> [very specific user — "students on 1.5 hr metro commute"]</p>
  <p><strong>🏅 Verdict Label:</strong> [Top Pick / Value Pick / Budget Champion / Premium Pick]</p>
  <p><strong>💬 Mini Verdict:</strong> [1 sentence. Include comparison: "Better than X. Cheaper than Y by ₹NNN."]</p>

  Expert Tip callout:
  <div style="border-left:3px solid #333;padding:10px 14px;margin:12px 0;background:#f9f9f9;">
  <strong>💡 Expert Tip:</strong> [India-specific buying advice: timing, variant, cashback]
  </div>

  Should You Buy box:
  <div style="border:1px solid #ddd;padding:12px 16px;margin:14px 0;">
  <strong>🤔 Should You Buy This?</strong><br/>
  ✅ Buy if: [case 1] | [case 2]<br/>
  ❌ Skip if: [reason 1] | [reason 2]
  </div>

  <p>📌 <em>Read more reviews on <a href="https://technewswithai.blogspot.com/search/label/[Category]" target="_blank">Tech News With AI</a>.</em></p>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[F] TRANSITION LINES between every product:
    "Now if that price is still tight, the next one will surprise you."
    "Different category of value — keep reading, this one is interesting."
    "That was the safe pick. Now here is the one for real enthusiasts."

[G] FINAL VERDICT (id="final-verdict"):
<h2 id="final-verdict">🏆 Final Verdict — The Clear Winner in India 2026</h2>
""" + VERDICT_TABLE_HTML + """
    → Declare ONE winner clearly. One sentence why.
    → Add "Value Pick" (best for budget) and "Top Pick" (best overall).
    → CTA: "Explore all [Category] reviews →
       <a href="https://technewswithai.blogspot.com/search/label/[Category]" target="_blank">Tech News With AI</a>"

[H] FAQ (id="faq") — 5 question-based H3 subheadings (Google rich results):
    • First question = exact search query (mandatory)
    • Mix of: which/what/how/is/are questions
    • Keep answers under 60 words each (Google snippet optimal)
    • Each answer must be complete and standalone
    Examples:
    <h3>Which is the best [product] under ₹[price] in India 2026?</h3>
    <h3>Is [Product Name] worth buying in India 2026?</h3>
    <h3>What is the difference between [X] and [Y]?</h3>
    <h3>How long does [Product] battery last in real use?</h3>
    <h3>Where is the best place to buy [Product] in India?</h3>

[I] LONG-TAIL KEYWORD PLACEMENT (SEO):
    Place these naturally in the text — not forced:
    • In first 100 words (primary keyword)
    • In at least 2 H2 headings (secondary keywords)
    • In 1 H3 per product (long-tail variant)
    • In conclusion/verdict section
    Examples of long-tail patterns:
    "best [product] under ₹[price] for [use case] in India [year]"
    "which [product] is best for [use case] India [year]"
    "[product1] vs [product2] which is better India [year]"
"""


# ── Writing rules injected into every prompt ─────────────────────
WRITING_RULES = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WRITING, SEO & ENGAGEMENT RULES — APPLY TO EVERY SECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TARGET: 4000+ words total. Every section must be rich and full.

─── STRUCTURE ───────────────────────────────────────
• H2 = product or main section header
• H3 = question-based feature subheading (improves SEO ranking)
• Bullet points for all feature lists — NOT long paragraphs
• Every H3: 1 opening sentence + 4-6 bullets + 1 closing line
• Bold: <strong>price</strong>, <strong>battery hrs</strong>, key spec values

─── SENTENCE RULES ──────────────────────────────────
• Max 15 words per sentence. Mix short (5 words) with medium (12-15 words).
• NEVER two consecutive sentences of the same length.

─── ENGAGEMENT TECHNIQUES ───────────────────────────
① HOOK every H2 with a curiosity gap:
   "Here is what the spec sheet does NOT tell you."
   "I tested this for 2 weeks. The result surprised me."
   "This one thing makes it stand out from every competitor."

② CLIFFHANGER after intro of each product:
   "But there is one big problem. Keep reading."
   "Before you add it to cart — read section 4 first."
   "Sounds perfect, right? Wait until you see the battery test."

③ TRANSITION BRIDGE between every product:
   "Now if that price is still too high, the next pick will surprise you."
   "Different budget, completely different experience — here we go."
   "This next one is polarising. Some love it. Some hate it. Here is why."

④ EXPERT TIP CALLOUT inside each product section (use this exact HTML):
<div style="border-left:3px solid #333;padding:10px 14px;margin:12px 0;background:#f9f9f9;">
<strong>💡 Expert Tip:</strong> [Specific actionable India tip for this product — price timing, variant choice, where to buy]
</div>

⑤ SHOULD YOU BUY BOX at end of each product (use this exact HTML):
<div style="border:1px solid #ddd;padding:12px 16px;margin:14px 0;">
<strong>🤔 Should You Buy This?</strong><br/>
✅ Buy if: [specific use case 1] | [specific use case 2]<br/>
❌ Skip if: [specific reason 1] | [specific reason 2]
</div>

─── DATA & SPECIFICITY ──────────────────────────────
• NEVER: good, nice, amazing, great, excellent, decent, solid
• ALWAYS use specifics: deep bass, punchy mids, 42dB ANC, 28ms latency, 120Hz AMOLED
• Every section: minimum 2 real numbers (hours, dB, ms, Hz, MP, W, g, mAh)
• Comparison line in every product: "beats X in battery", "₹NNN cheaper than Z"

─── REAL-LIFE INDIA USAGE ───────────────────────────
One real-life India scenario per H3. Rotate through:
• "through my 1.5 hr Bengaluru metro commute without any discomfort"
• "during PUBG Mobile session at 90fps — no thermal throttle for 2 hrs"
• "battery lasted full IPL match + 2 hr Hotstar binge, still 20% left"
• "worked perfectly on hostel WiFi at 2 Mbps — zero stutter on Spotify"
• "survived 40-min morning run, IP54 handled the sweat without issue"
• "powered through 3 engineering exam prep days on a single charge"
• "6-hr offline lecture recording with zero heating on this laptop"
• "crystal clear call quality even in Bengaluru traffic noise"

─── CATEGORY ACCURACY ───────────────────────────────
NEVER mix categories. Only use specs that belong to this device:
• Earphones:   ANC dB | codec (AAC/aptX/LDAC) | driver mm | IP rating | latency ms
• Headphones:  clamping force | earcup depth | ANC dB | fold design | wired backup port
• Smartphones: SoC name | display type+Hz | camera sensor size | battery mAh | charge W
• Laptops:     CPU name+gen | RAM GB | SSD GB+type | nits brightness | Wh battery | kg weight
• Smartwatch:  display size+type | battery days | GPS type | SpO2/ECG | ATM rating
• Power Bank:  real mAh output | input W | output W | PD/QC version | port count | g weight

─── ABSOLUTE NEVER ──────────────────────────────────
• NO **markdown bold** — ONLY <strong>HTML</strong> tags
• NO: "In conclusion", "To summarize", "It is worth noting", "Overall"
• NO two consecutive sections starting the same way
• NO repeated sentence anywhere in the article
• NO wrong-category specs (AMOLED in earphone article = instant disqualification)
• NO links to any external website — ONLY technewswithai.blogspot.com label pages

─── MINIMUM REQUIREMENTS (CHECKLIST) ────────────────
✓ 4000+ words
✓ Hook intro: problem line 1, solution line 2
✓ Primary keyword in first 100 words
✓ Comparison table at top (real specs, no colour headers)
✓ Specs box per product
✓ Pros/Cons table per product
✓ Expert Tip callout per product
✓ Should You Buy box per product
✓ Transition bridge between every product
✓ Best For line per product
✓ Mini Verdict per product (comparison word included)
✓ CTA per product (links to your blog label)
✓ Final Verdict table (plain border)
✓ FAQ with 5+ questions (first = exact search query)

─── ADSENSE APPROVAL REQUIREMENTS ──────────────────
• ORIGINAL content only — never copy from any source
• Every sentence must add NEW information — no filler
• <p> tags: max 3 sentences each (mobile-friendly)
• No broken HTML — all tags must be properly closed
• No thin sections — every H3 must have 4+ bullet points
• Write like a real person, not a tool — AdSense rejects AI-sounding content
• DO NOT repeat the same idea in different words anywhere

─── GOOGLE DISCOVER OPTIMIZATION ────────────────────
• First image must be 1200px wide (placeholder block is already added by code)
• Use descriptive, emotional language in first 100 words
• Include trending angle: AI features, India price, value-for-money

─── LONG-TAIL KEYWORDS (inject naturally, not stuffed) ──
These must appear organically in the article text:
[LONGTAIL_KEYWORDS_PLACEHOLDER]
"""


def groq_draft(story, is_search):
    client   = Groq(api_key=GROQ_API_KEY)
    cat      = story.get("category", "smartphone")
    struct   = CAT.get(cat, CAT["smartphone"])
    sections = "\n".join(struct["sections"])
    link_rules = build_internal_link_instructions(cat)

    # Build longtail keywords from live context
    ctx_text    = story.get("rss_context", "")
    topic_text  = story.get("search_topic") or story.get("title", "")
    longtail_kw = build_longtail_keywords(cat, ctx_text, topic_text)
    kw_list     = "\n".join(f"  • {k}" for k in longtail_kw)

    # Inject longtail into WRITING_RULES dynamically
    rules_with_kw = WRITING_RULES.replace(
        "[LONGTAIL_KEYWORDS_PLACEHOLDER]", kw_list
    )

    # Use pre-generated SEO title if present
    seo_title = story.get("seo_title", "")
    title_instruction = (
        f'USE THIS EXACT H1 TITLE (already SEO-optimised):\n<h1>{seo_title}</h1>\n\n'
        if seo_title else
        "Generate H1 title: number hook + primary keyword + India + year. Max 65 chars.\n\n"
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
            title_instruction +
            "Write a comprehensive SEO-optimised guide for Indians searching: '" + topic + "'\n\n"
            "ARTICLE TYPE: " + mode + "\n\n"
            "REAL DATA FROM RSS AND REVIEW SOURCES:\n"
            + (ctx or "Use your latest India market 2026 knowledge.") + "\n\n"
            + BUYING_GUIDE_STRUCTURE + "\n\n"
            + rules_with_kw + "\n\n"
            + link_rules + "\n\n"
            "WRITE THESE 12 SECTIONS:\n" + sections + "\n\n"
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
            + PROS_CONS_HTML + "\n"
            "6. Write 12 sections using H2/H3 hierarchy.\n"
            "   H2 = main topic. H3 = question-based subheading (improves SEO).\n\n"

            + rules_with_kw + "\n\n"
            + link_rules + "\n\n"

            "WRITE THESE 12 SECTIONS:\n" + sections + "\n\n"
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
        "• Expert Tip callout divs and Should You Buy boxes\n"
        "• Table of Contents and all anchor links\n"
        "• All H1, H2, H3 headings\n"
        "• All internal links to technewswithai.blogspot.com\n"
        "• Best For lines, Mini Verdict lines, CTA lines\n\n"

        "━━━ FOR EVERY SECTION, DO ALL OF THESE ━━━\n\n"
        "① PERSONAL HOOK — start H2 with a curiosity gap:\n"
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
        "✓ 4000+ words\n"
        "✓ Hook intro — problem line 1, solution line 2\n"
        "✓ Primary keyword in first 100 words\n"
        "✓ Curiosity gap hook on every H2\n"
        "✓ Cliffhanger after first line of every product\n"
        "✓ Transition bridge between every product section\n"
        "✓ All 5 products: specs box + pros/cons + expert tip + should-you-buy + best for + mini verdict + CTA\n"
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
    blog_url = "https://technewswithai.blogspot.com"

    # Step 3 — Inject hero image block (Google Discover: 1200px)
    hero_img = build_image_block(
        alt_text=title,
        caption="Image: " + title + " | technewswithai.blogspot.com",
        position="hero"
    )
    # Insert hero image after H1 (before first <p>)
    final = re.sub(
        r'(<h1[^>]*>.*?</h1>)',
        r'\1\n' + hero_img,
        final, count=1, flags=re.DOTALL|re.IGNORECASE
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
    social_block = build_social_block(title, blog_url)

    # Step 7 — Footer
    footer = (
        "<hr/>"
        + social_block
        + "<p style='font-size:12px;color:#888;text-align:center;padding:10px;'>"
        "<em>Published by Mallikarjun R | "
        "<a href='" + blog_url + "' target='_blank'>Tech News With AI</a>"
        " | technewswithai.blogspot.com</em></p>"
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

    # Article 3 — Different dynamic search topic
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
