"""
TECH NEWS WITH AI - AUTO BLOG SYSTEM v3.0
Blog    : technewsai.me
Author  : Mallikarjun R, Bengaluru
AI      : Groq Llama 3.3 70B (FREE) with Grok fallback
Features: AdSense-ready, EEAT, SEO, Internal Linking, Human Writing
"""

import os
import sys
import json
import time
import random
import requests
import datetime
import re
import smtplib
import xml.etree.ElementTree as ET
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ══════════════════════════════════════════════════════
#  SETTINGS
# ══════════════════════════════════════════════════════

GROQ_API_KEY       = os.environ.get("GROQ_API_KEY", "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")
NEWS_API_KEY       = os.environ.get("NEWS_API_KEY", "673bca5ceab54fa8bb7ed0344c8f6d13")
XAI_API_KEY        = os.environ.get("XAI_API_KEY", "")
BLOG_ID            = "6974086222747114440"
BLOGGER_POST_EMAIL = "mallikarjunr444.technewswithai6361@blogger.com"
GMAIL_ADDRESS      = "mallikarjunr444@gmail.com"
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "oeirtosmlhuwntka")
ARTICLES_PER_RUN   = 3
BLOG_URL           = "https://www.technewsai.me"
AUTHOR_NAME        = "Mallikarjun R"
AUTHOR_BIO         = (
    "Mallikarjun R is a tech enthusiast and Computer Science Engineering student "
    "specializing in Cyber Security at DSATM, Bengaluru, India. "
    "He covers smartphones, laptops, and AI news for Indian readers on technewsai.me."
)
INSTAGRAM_URL      = "https://www.instagram.com/mallikarjunr_8055"
LINKEDIN_URL       = "https://in.linkedin.com/in/mallikarjun-r-a85685367"
WHATSAPP_URL       = "https://whatsapp.com/channel/0029VazWwdn0wajoizN5PY3Q"

# ══════════════════════════════════════════════════════
#  INTERNAL LINKS — fetched from your real blog posts
# ══════════════════════════════════════════════════════

INTERNAL_LINKS = [
    {
        "title": "Samsung Galaxy A37 and A57 Review",
        "url":   "https://www.technewsai.me/2026/03/the-wait-is-over-galaxy-a37-and-a57.html",
        "keywords": ["samsung", "galaxy", "mid-range", "android"],
    },
    {
        "title": "OPPO Find N6 Review: Gold Standard of Foldables",
        "url":   "https://www.technewsai.me/2026/03/oppo-find-n6-review-gold-standard-of.html",
        "keywords": ["oppo", "foldable", "find n6"],
    },
    {
        "title": "ROG Strix Scar 18: Beast Gaming Laptop 2026",
        "url":   "https://www.technewsai.me/2026/03/new-rog-strix-scar-18-unleashing-beast.html",
        "keywords": ["rog", "gaming laptop", "asus", "laptop"],
    },
    {
        "title": "Best Battery and Performance Phones 2026",
        "url":   "https://www.technewsai.me/2026/03/get-ready-for-battery-and-performance.html",
        "keywords": ["battery", "performance", "best phone"],
    },
]

# ══════════════════════════════════════════════════════
#  HIGH CPC NEWS TOPICS WITH SEO KEYWORDS
# ══════════════════════════════════════════════════════

NEWS_TOPICS = [
    "best smartphone under 20000 India 2026",
    "best smartphone under 30000 India 2026",
    "best laptop under 50000 India 2026",
    "iPhone 16 price India review 2026",
    "Samsung Galaxy S25 review India price",
    "OnePlus 13 review India price specs",
    "Realme GT 7 Pro review India",
    "best gaming phone India 2026",
    "best camera phone India 2026",
    "best foldable phone India 2026",
    "MacBook Air M4 review India price",
    "iPad Pro 2026 review India",
    "Samsung Galaxy A launch India specs 2026",
    "Xiaomi 15 Ultra review India specs",
    "Poco X7 Pro review India price",
    "Redmi Note 14 Pro review India",
    "Vivo X200 Pro review India price",
    "iQOO 13 review India price specs",
    "Google Pixel 9 Pro review India",
    "Motorola Edge 50 review India",
    "Nothing Phone 3 review India specs",
    "Infinix GT 20 Pro review India",
    "best TWS earbuds under 5000 India 2026",
    "best smartwatch under 10000 India 2026",
    "Dell XPS 15 review India price 2026",
    "HP Spectre review India price 2026",
    "Lenovo ThinkPad review India 2026",
    "ASUS Zenbook review India 2026",
    "best Android tablet India 2026",
    "AI phone features comparison India 2026",
    "5G phone under 15000 India 2026",
    "best phone for students India 2026",
    "best phone for gaming India budget 2026",
    "NVIDIA laptop GPU review India 2026",
    "Apple vs Samsung flagship comparison India 2026",
]

# ══════════════════════════════════════════════════════
#  RSS FEEDS
# ══════════════════════════════════════════════════════

RSS_FEEDS = [
    ("The Verge",        "https://www.theverge.com/rss/index.xml"),
    ("TechCrunch",       "https://techcrunch.com/feed/"),
    ("Engadget",         "https://www.engadget.com/rss.xml"),
    ("CNET",             "https://www.cnet.com/rss/news/"),
    ("GSMArena",         "https://www.gsmarena.com/rss-news-articles.php3"),
    ("AndroidAuthority", "https://www.androidauthority.com/feed/"),
    ("9to5Google",       "https://9to5google.com/feed/"),
    ("XDA Developers",   "https://www.xda-developers.com/feed/"),
    ("NotebookCheck",    "https://www.notebookcheck.net/News.rss"),
    ("91Mobiles",        "https://www.91mobiles.com/hub/feed/"),
    ("MySmartPrice",     "https://www.mysmartprice.com/feed/"),
    ("GizmoChina",       "https://www.gizmochina.com/feed/"),
    ("GadgetsNow",       "https://www.gadgetsnow.com/rssfeedstopstories.cms"),
]

# ══════════════════════════════════════════════════════
#  NEWS FETCHER
# ══════════════════════════════════════════════════════

def fetch_from_rss(feed_name, feed_url, keyword):
    try:
        r = requests.get(feed_url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        if r.status_code != 200:
            return []
        root = ET.fromstring(r.content)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        items = root.findall(".//item") or root.findall(".//atom:entry", ns)
        articles = []
        for item in items[:10]:
            title_el = item.find("title")
            title = title_el.text if title_el is not None else ""
            if not title:
                continue
            if keyword.lower().split()[0] not in title.lower():
                continue
            desc_el = item.find("description") or item.find("summary")
            description = desc_el.text if desc_el is not None else ""
            if description:
                description = re.sub(r"<[^>]+>", "", description)[:500]
            link_el = item.find("link")
            link = link_el.text if link_el is not None else feed_url
            date_el = item.find("pubDate") or item.find("published")
            published = date_el.text if date_el is not None else ""
            if title and description:
                articles.append({
                    "title":       title.strip(),
                    "description": description.strip(),
                    "content":     description.strip(),
                    "url":         link.strip() if link else feed_url,
                    "source":      feed_name,
                    "published":   published or "2026-03-19T00:00:00Z",
                })
        return articles[:3]
    except Exception:
        return []


def fetch_from_newsapi(query, count=3):
    try:
        r = requests.get(
            "https://newsapi.org/v2/everything",
            params={
                "q":        query,
                "language": "en",
                "sortBy":   "publishedAt",
                "pageSize": count,
                "apiKey":   NEWS_API_KEY,
            },
            timeout=10,
        )
        data = r.json()
        if data.get("status") != "ok":
            return []
        return [
            {
                "title":       a["title"],
                "description": a.get("description") or "",
                "content":     a.get("content") or "",
                "url":         a["url"],
                "source":      a["source"]["name"],
                "published":   a["publishedAt"],
            }
            for a in data.get("articles", [])
            if a.get("title") and a.get("description")
        ]
    except Exception:
        return []


def fetch_news(query, count=3):
    print("  Searching: " + query)
    all_articles = []
    keyword = query.split()[0]
    feeds = RSS_FEEDS[:]
    random.shuffle(feeds)
    for feed_name, feed_url in feeds[:8]:
        articles = fetch_from_rss(feed_name, feed_url, keyword)
        all_articles.extend(articles)
        if len(all_articles) >= 3:
            break
    if len(all_articles) < 2:
        all_articles.extend(fetch_from_newsapi(query, count))
    seen = set()
    unique = []
    for a in all_articles:
        if a["title"] not in seen:
            seen.add(a["title"])
            unique.append(a)
    print("    " + str(len(unique)) + " articles found")
    return unique[:count]


def pick_story():
    topics = NEWS_TOPICS[:]
    random.shuffle(topics)
    for topic in topics:
        articles = fetch_news(topic)
        if articles:
            s = articles[0]
            print("  Picked : " + s["title"])
            print("  Source : " + s["source"])
            return s
    return None

# ══════════════════════════════════════════════════════
#  INTERNAL LINK BUILDER
# ══════════════════════════════════════════════════════

def get_relevant_internal_links(title, content):
    text = (title + " " + content).lower()
    relevant = []
    for link in INTERNAL_LINKS:
        for kw in link["keywords"]:
            if kw in text and link not in relevant:
                relevant.append(link)
    if not relevant:
        relevant = random.sample(INTERNAL_LINKS, min(2, len(INTERNAL_LINKS)))
    return relevant[:3]


def build_internal_links_html(links):
    if not links:
        return ""
    html = "<h3>Related Articles You Might Like</h3>"
    html += "<p>If you found this article helpful, you will also enjoy reading these:"
    for i, link in enumerate(links):
        html += ' <a href="' + link["url"] + '">' + link["title"] + "</a>"
        if i < len(links) - 1:
            html += ","
    html += ".</p>"
    return html

# ══════════════════════════════════════════════════════
#  AI WRITER SYSTEM PROMPT
# ══════════════════════════════════════════════════════

SYSTEM_PROMPT = (
    "You are Mallikarjun R, a passionate tech journalist and CS student from Bengaluru, India. "
    "You write for your blog technewsai.me. You are a real human who loves gadgets, "
    "has opinions, and writes from personal experience. "
    "You are NOT an AI assistant. You are a person.\n\n"

    "EEAT REQUIREMENTS (Critical for Google AdSense approval):\n"
    "Experience: Write as someone who has personally handled devices. "
    "Expertise: Show deep technical knowledge explained simply. "
    "Authority: Give clear confident recommendations. "
    "Trust: Be honest about flaws, never just praise everything.\n\n"

    "HUMAN WRITING STYLE:\n"
    "Open with a personal story or strong opinion. "
    "Use phrases like: I have been testing this, Honestly speaking, "
    "Let me be straight with you, Here is what really matters, "
    "After using this for a week, In my honest opinion. "
    "Include frustrations: The one thing that bothered me, "
    "I wish they had fixed, This is where it falls short. "
    "Vary sentence lengths. Short punchy sentences matter. "
    "Then longer analytical ones that go deeper into the topic. "
    "FORBIDDEN words: Furthermore, Moreover, In conclusion, It is worth noting, "
    "Transitioning to, It is important to note, In summary.\n\n"

    "INDIA CONTEXT (Mandatory):\n"
    "Always mention India price in INR. Convert USD to INR at 85 rupees per dollar. "
    "Mention EMI options on Flipkart and Amazon India. "
    "Compare with alternatives at similar India price points. "
    "Reference Indian usage: Bengaluru traffic, Mumbai commute, Delhi heat, "
    "college student budget, office professional needs. "
    "Mention availability: Flipkart, Amazon India, brand stores, "
    "offline retail in India.\n\n"

    "ARTICLE STRUCTURE (follow exactly):\n"
    "H1 handled by blog theme - do not add H1.\n"
    "Start with H2 title that includes main keyword.\n"
    "Section 1 H2: Opening - personal hook and why this matters in India now\n"
    "Section 2 H2: Design and Build Quality\n"
    "Section 3 H2: Display and Visual Experience\n"
    "Section 4 H2: Performance and Gaming\n"
    "Section 5 H2: Camera System Analysis\n"
    "Section 6 H2: Battery Life and Charging\n"
    "Section 7 H2: Software and Features\n"
    "Section 8 H2: Price in India and Value for Money\n"
    "Section 9 H2: Pros and Cons\n"
    "Section 10 H2: Comparison with Competitors\n"
    "Section 11 H2: Who Should Buy This\n"
    "Section 12 H2: Final Verdict\n"
    "Section 13 H2: Frequently Asked Questions\n\n"

    "PROS AND CONS FORMAT:\n"
    "Write Pros as a paragraph starting: What genuinely impressed me about this device...\n"
    "Write Cons as a paragraph starting: However I have to be honest about the downsides...\n"
    "Do NOT use bullet points or lists anywhere.\n\n"

    "FAQ FORMAT:\n"
    "Write 5 questions and answers as flowing paragraphs.\n"
    "Questions must be what real Indian buyers ask on Flipkart reviews.\n\n"

    "SEO RULES:\n"
    "Include the main keyword in the first H2, first paragraph, and 2-3 subheadings. "
    "Use related keywords naturally throughout. "
    "Minimum 2800 words. Aim for 3200 words. "
    "Every paragraph adds unique new information.\n\n"

    "FORMAT RULES:\n"
    "Clean HTML only. No markdown. No asterisks. No bullet points anywhere. "
    "Use h2 for main sections. Use h3 for sub-points within sections. "
    "Every paragraph wrapped in p tags. "
    "Use strong tags for important specs and numbers. "
    "Do not include html, head, or body tags."
)

# ══════════════════════════════════════════════════════
#  ARTICLE BUILDER
# ══════════════════════════════════════════════════════

def build_prompt(story):
    lines = [
        "Write a complete expert-level tech article for Indian readers.",
        "",
        "TOPIC     : " + story["title"],
        "SUMMARY   : " + story["description"],
        "DETAILS   : " + (story["content"][:700] if story["content"] else "Use your knowledge"),
        "SOURCE    : " + story["source"],
        "",
        "MANDATORY REQUIREMENTS:",
        "1. Start with H2 containing the main SEO keyword in the title",
        "2. Write minimum 2800 words - aim for 3200",
        "3. Include all 13 sections listed in your instructions",
        "4. Sound like a real Indian tech journalist with genuine opinions",
        "5. Include India price in INR with EMI options",
        "6. Compare with 2 specific competitors at similar India price",
        "7. Write Pros section as a paragraph (no bullets)",
        "8. Write Cons section as a paragraph (no bullets)",
        "9. Include 5 FAQ questions Indian buyers actually ask",
        "10. Every section must have at least 2 paragraphs",
        "11. Use strong tags for specs and numbers",
        "12. No markdown, no asterisks, clean HTML only",
        "",
        "Write the complete article now:",
    ]
    return "\n".join(lines)


def build_author_box():
    return (
        '<div style="background:#f8f9fa;border:1px solid #e0e0e0;'
        'padding:20px;margin:32px 0;border-radius:8px;">'
        '<p style="font-size:18px;font-weight:bold;margin-bottom:8px;">'
        'About the Author</p>'
        '<p style="font-size:15px;color:#333;margin-bottom:12px;">'
        + AUTHOR_BIO +
        '</p>'
        '<p style="margin:0;">'
        '<strong>Follow Mallikarjun:</strong> '
        '<a href="' + INSTAGRAM_URL + '" target="_blank" rel="noopener" '
        'style="color:#E1306C;margin-right:12px;">Instagram</a> '
        '<a href="' + LINKEDIN_URL + '" target="_blank" rel="noopener" '
        'style="color:#0077B5;margin-right:12px;">LinkedIn</a> '
        '<a href="' + WHATSAPP_URL + '" target="_blank" rel="noopener" '
        'style="color:#25D366;">WhatsApp Channel</a>'
        '</p>'
        '</div>'
    )


def build_footer(story):
    src = story["source"]
    pub = story["published"][:10]
    url = story["url"]
    parts = [
        "<hr>",
        '<p><em><strong>Source:</strong> ' + src +
        ' | <strong>Published:</strong> ' + pub +
        ' | <a href="' + url + '" target="_blank" rel="noopener">Read original article</a></em></p>',
        '<div style="background:#1a73e8;color:white;padding:20px;'
        'border-radius:8px;margin:24px 0;text-align:center;">',
        '<p style="font-size:18px;font-weight:bold;margin-bottom:8px;">'
        'Stay Connected with Tech News With AI</p>',
        '<p style="margin-bottom:16px;">Get daily tech news, reviews and updates!</p>',
        '<p>'
        '<a href="' + BLOG_URL + '" style="background:white;color:#1a73e8;'
        'padding:8px 16px;border-radius:4px;text-decoration:none;margin:4px;'
        'display:inline-block;font-weight:bold;">Visit Blog</a> '
        '<a href="' + INSTAGRAM_URL + '" target="_blank" rel="noopener" '
        'style="background:#E1306C;color:white;padding:8px 16px;border-radius:4px;'
        'text-decoration:none;margin:4px;display:inline-block;font-weight:bold;">'
        'Instagram</a> '
        '<a href="' + LINKEDIN_URL + '" target="_blank" rel="noopener" '
        'style="background:#0077B5;color:white;padding:8px 16px;border-radius:4px;'
        'text-decoration:none;margin:4px;display:inline-block;font-weight:bold;">'
        'LinkedIn</a> '
        '<a href="' + WHATSAPP_URL + '" target="_blank" rel="noopener" '
        'style="background:#25D366;color:white;padding:8px 16px;border-radius:4px;'
        'text-decoration:none;margin:4px;display:inline-block;font-weight:bold;">'
        'WhatsApp Channel</a>'
        '</p>',
        '</div>',
    ]
    return "\n".join(parts)


def clean_and_parse(raw, story):
    # Remove markdown code fences
    raw = re.sub(r"```html\s*", "", raw)
    raw = re.sub(r"```\s*", "", raw)
    raw = raw.strip()

    # Convert any leftover markdown bold to HTML
    raw = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", raw)

    # Convert any leftover markdown italic to HTML
    raw = re.sub(r"\*(.+?)\*", r"<em>\1</em>", raw)

    # Remove any h1 tags (blog theme handles h1)
    raw = re.sub(r"<h1[^>]*>.*?</h1>", "", raw, flags=re.IGNORECASE | re.DOTALL)

    # Remove duplicate h2 if appears at very top before content
    h2_list = re.findall(r"<h2[^>]*>.*?</h2>", raw, re.IGNORECASE | re.DOTALL)
    if len(h2_list) > 1:
        first_h2_pos = raw.lower().find("<h2")
        second_h2_pos = raw.lower().find("<h2", first_h2_pos + 1)
        if second_h2_pos - first_h2_pos < 200:
            raw = raw[:first_h2_pos] + raw[second_h2_pos:]

    # Get article title from first h2
    title = story["title"]
    m = re.search(r"<h2[^>]*>(.*?)</h2>", raw, re.IGNORECASE | re.DOTALL)
    if m:
        title = re.sub(r"<[^>]+>", "", m.group(1)).strip()

    # Count words
    word_count = len(re.sub(r"<[^>]+>", "", raw).split())
    print("    Words: " + str(word_count))

    return title, raw


def write_post(story):
    prompt = build_prompt(story)

    raw = None

    # Try Grok first if key available
    if XAI_API_KEY:
        try:
            print("  Writing with Grok (xAI)...")
            from openai import OpenAI as OpenAIClient
            grok = OpenAIClient(api_key=XAI_API_KEY, base_url="https://api.x.ai/v1")
            resp = grok.chat.completions.create(
                model="grok-3",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user",   "content": prompt},
                ],
                max_tokens=4096,
                temperature=0.75,
            )
            raw = resp.choices[0].message.content
            print("  Grok writing done!")
        except Exception as e:
            print("  Grok error: " + str(e) + " - using Groq...")

    # Fallback: Groq Llama
    if raw is None:
        print("  Writing with Groq Llama 3.3 70B...")
        from groq import Groq
        client = Groq(api_key=GROQ_API_KEY)
        resp = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": prompt},
            ],
            max_tokens=4096,
            temperature=0.75,
        )
        raw = resp.choices[0].message.content
        print("  Groq writing done!")

    # Parse and clean the response
    title, article_html = clean_and_parse(raw, story)

    # Build internal links section
    internal_links = get_relevant_internal_links(title, story["description"])
    internal_links_html = build_internal_links_html(internal_links)

    # Build author box
    author_box = build_author_box()

    # Build footer
    footer = build_footer(story)

    # Assemble final HTML
    final_html = (
        article_html +
        "\n" + internal_links_html +
        "\n" + author_box +
        "\n" + footer
    )

    return title, final_html

# ══════════════════════════════════════════════════════
#  LABELS / TAGS
# ══════════════════════════════════════════════════════

def auto_labels(title, html):
    text = (title + " " + html[:500]).lower()
    labels = ["Tech News", "India"]
    label_map = {
        "iphone":    ["iPhone", "Apple"],
        "macbook":   ["MacBook", "Laptop", "Apple"],
        "ipad":      ["iPad", "Apple"],
        "airpods":   ["AirPods", "Apple"],
        "samsung":   ["Samsung", "Android"],
        "oneplus":   ["OnePlus", "Android"],
        "realme":    ["Realme", "Android"],
        "xiaomi":    ["Xiaomi", "Android"],
        "poco":      ["Poco", "Android"],
        "redmi":     ["Redmi", "Android"],
        "vivo":      ["Vivo", "Android"],
        "iqoo":      ["iQOO", "Android"],
        "google":    ["Google", "Android"],
        "pixel":     ["Google Pixel"],
        "motorola":  ["Motorola", "Android"],
        "nokia":     ["Nokia"],
        "nothing":   ["Nothing Phone"],
        "infinix":   ["Infinix"],
        "oppo":      ["OPPO", "Android"],
        "honor":     ["Honor", "Android"],
        "laptop":    ["Laptop"],
        "gaming":    ["Gaming"],
        "android":   ["Android"],
        "apple":     ["Apple"],
        "foldable":  ["Foldable Phone"],
        "ai":        ["Artificial Intelligence"],
        "earbuds":   ["Earbuds", "Audio"],
        "smartwatch": ["Smartwatch", "Wearables"],
        "tablet":    ["Tablet"],
        "under 20000": ["Budget Phone"],
        "under 30000": ["Mid Range Phone"],
    }
    for kw, tags in label_map.items():
        if kw in text:
            for t in tags:
                if t not in labels:
                    labels.append(t)
    labels.append(str(datetime.datetime.now().year))
    return labels[:10]

# ══════════════════════════════════════════════════════
#  POST TO BLOGGER VIA EMAIL
# ══════════════════════════════════════════════════════

def post_via_email(title, html, labels):
    print("  Sending to Blogger...")
    gmail_password = os.environ.get("GMAIL_APP_PASSWORD", GMAIL_APP_PASSWORD)
    msg = MIMEMultipart("alternative")
    msg["Subject"] = title
    msg["From"]    = GMAIL_ADDRESS
    msg["To"]      = BLOGGER_POST_EMAIL
    msg.attach(MIMEText(html, "html"))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_ADDRESS, gmail_password)
        server.sendmail(GMAIL_ADDRESS, BLOGGER_POST_EMAIL, msg.as_string())
    print("  Posted: " + BLOG_URL)
    return BLOG_URL


def post_article(title, html, labels):
    print("  Posting: " + title[:65] + "...")
    return post_via_email(title, html, labels)


def save_log(title, url):
    log_file = "posted_articles.json"
    log = []
    if os.path.exists(log_file):
        with open(log_file) as f:
            log = json.load(f)
    log.append({
        "title":     title,
        "url":       url,
        "posted_at": datetime.datetime.now().isoformat(),
    })
    with open(log_file, "w") as f:
        json.dump(log, f, indent=2)
    print("  Log saved (" + str(len(log)) + " total posts)")

# ══════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════

def main():
    print("=" * 58)
    print("  TECH NEWS WITH AI - AUTO BLOG v3.0")
    print("  " + BLOG_URL)
    print("  AdSense-Ready | EEAT | SEO | Human Writing")
    print("=" * 58)

    success = 0
    for i in range(ARTICLES_PER_RUN):
        try:
            print("\n--- Article " + str(i + 1) + " of " + str(ARTICLES_PER_RUN) + " ---")
            story = pick_story()
            if not story:
                print("No story found, skipping...")
                continue
            title, html = write_post(story)
            labels = auto_labels(title, html)
            url = post_article(title, html, labels)
            save_log(title, url)
            success += 1
            if i < ARTICLES_PER_RUN - 1:
                print("  Waiting 25 seconds...")
                time.sleep(25)
        except KeyboardInterrupt:
            print("\nStopped by user.")
            break
        except Exception as e:
            print("  Error: " + str(e))
            continue

    print("\n" + "=" * 58)
    print("  DONE! " + str(success) + "/" + str(ARTICLES_PER_RUN) + " articles posted!")
    print("  " + BLOG_URL)
    print("=" * 58)


if __name__ == "__main__":
    main()
