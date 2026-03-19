"""
TECH NEWS WITH AI - AUTO BLOG SYSTEM v4.0
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
    "Mallikarjun R is a first-year Computer Science Engineering student at DSATM, "
    "Bengaluru, India. He is passionate about technology, smartphones, and AI. "
    "He runs Tech News With AI (technewsai.me) to bring the latest tech news "
    "and honest reviews to Indian readers."
)
INSTAGRAM_URL  = "https://www.instagram.com/mallikarjunr_8055"
LINKEDIN_URL   = "https://in.linkedin.com/in/mallikarjun-r-a85685367"
WHATSAPP_URL   = "https://whatsapp.com/channel/0029VazWwdn0wajoizN5PY3Q"

# ══════════════════════════════════════════════════════
#  INTERNAL LINKS
# ══════════════════════════════════════════════════════

INTERNAL_LINKS = [
    {
        "title":    "Samsung Galaxy A37 and A57 Review",
        "url":      "https://www.technewsai.me/2026/03/the-wait-is-over-galaxy-a37-and-a57.html",
        "keywords": ["samsung", "galaxy", "mid-range", "android"],
    },
    {
        "title":    "OPPO Find N6 Review: Gold Standard of Foldables",
        "url":      "https://www.technewsai.me/2026/03/oppo-find-n6-review-gold-standard-of.html",
        "keywords": ["oppo", "foldable", "find n6"],
    },
    {
        "title":    "ROG Strix Scar 18: Beast Gaming Laptop 2026",
        "url":      "https://www.technewsai.me/2026/03/new-rog-strix-scar-18-unleashing-beast.html",
        "keywords": ["rog", "gaming laptop", "asus", "laptop"],
    },
    {
        "title":    "Best Battery and Performance Phones 2026",
        "url":      "https://www.technewsai.me/2026/03/get-ready-for-battery-and-performance.html",
        "keywords": ["battery", "performance", "best phone"],
    },
]

# ══════════════════════════════════════════════════════
#  HIGH CPC NEWS TOPICS
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
#  INTERNAL LINKS
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
#  SYSTEM PROMPT
# ══════════════════════════════════════════════════════

SYSTEM_PROMPT = (
    "You are Mallikarjun R, a passionate tech journalist and CS student from Bengaluru, India. "
    "You write for your blog technewsai.me. You are a real human who loves gadgets, "
    "has opinions, and writes from personal experience. "
    "You are NOT an AI assistant. You are a person.\n\n"
    "EEAT REQUIREMENTS:\n"
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
    "Vary sentence lengths. "
    "FORBIDDEN words: Furthermore, Moreover, In conclusion, It is worth noting, "
    "Transitioning to, It is important to note, In summary.\n\n"
    "INDIA CONTEXT:\n"
    "Always mention India price in INR at USD x 85. "
    "Mention EMI on Flipkart and Amazon India. "
    "Reference: Bengaluru traffic, Mumbai commute, Delhi heat, college budgets.\n\n"
    "ARTICLE STRUCTURE:\n"
    "Start with H2 title with main keyword.\n"
    "Section 1 H2: Opening Hook\n"
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
    "PROS AND CONS:\n"
    "Pros paragraph starts: What genuinely impressed me about this device...\n"
    "Cons paragraph starts: However I have to be honest about the downsides...\n"
    "No bullet points anywhere.\n\n"
    "FAQ: 5 questions and answers as flowing paragraphs.\n\n"
    "SEO: Include main keyword in first H2, first paragraph, and 2-3 subheadings. "
    "Minimum 2800 words. Every paragraph adds unique new information.\n\n"
    "FORMAT: Clean HTML only. No markdown. No asterisks. No bullet points. "
    "h2 for sections. h3 for sub-points. p tags for paragraphs. "
    "strong tags for specs. No html head body tags."
)

# ══════════════════════════════════════════════════════
#  PROMPT BUILDER
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
        "MANDATORY:",
        "1. H2 title with main SEO keyword",
        "2. Minimum 2800 words",
        "3. All 13 sections",
        "4. Real Indian journalist voice with opinions",
        "5. India price in INR with EMI",
        "6. Compare 2 competitors at similar India price",
        "7. Pros as paragraph no bullets",
        "8. Cons as paragraph no bullets",
        "9. 5 FAQ questions Indian buyers ask",
        "10. Min 2 paragraphs per section",
        "11. strong tags for specs",
        "12. Clean HTML only no markdown",
        "",
        "Write the full article now:",
    ]
    return "\n".join(lines)

# ══════════════════════════════════════════════════════
#  HTML BUILDERS
# ══════════════════════════════════════════════════════

def build_author_box():
    box = '<div style="background:#f8f9fa;border:1px solid #e0e0e0;padding:20px;margin:32px 0;border-radius:8px;">'
    box += '<p style="font-size:18px;font-weight:bold;margin-bottom:8px;">About the Author</p>'
    box += '<p style="font-size:15px;color:#333;margin-bottom:12px;">' + AUTHOR_BIO + '</p>'
    box += '<p style="margin:0;"><strong>Follow Mallikarjun:</strong> '
    box += '<a href="' + INSTAGRAM_URL + '" target="_blank" rel="noopener" style="color:#E1306C;margin-right:12px;">Instagram</a>'
    box += '<a href="' + LINKEDIN_URL + '" target="_blank" rel="noopener" style="color:#0077B5;margin-right:12px;">LinkedIn</a>'
    box += '<a href="' + WHATSAPP_URL + '" target="_blank" rel="noopener" style="color:#25D366;">WhatsApp Channel</a>'
    box += '</p></div>'
    return box


def build_footer(story):
    src = story["source"]
    pub = story["published"][:10]
    url = story["url"]

    # Source line
    source_line = '<hr><p><em><strong>Source:</strong> ' + src
    source_line += ' | <strong>Published:</strong> ' + pub
    source_line += ' | <a href="' + url + '" target="_blank" rel="noopener">Read original article</a></em></p>'

    # Social banner — BLACK background
    banner = '<div style="background:#111111;color:#ffffff;padding:24px;border-radius:8px;margin:24px 0;text-align:center;">'
    banner += '<p style="font-size:20px;font-weight:bold;margin-bottom:8px;color:#ffffff;">Stay Connected with Tech News With AI</p>'
    banner += '<p style="margin-bottom:20px;color:#cccccc;">Get daily tech news, reviews and updates from India!</p>'
    banner += '<p style="margin:0;">'

    # Visit Blog button — white
    banner += '<a href="' + BLOG_URL + '" style="background:#ffffff;color:#111111;padding:10px 18px;'
    banner += 'border-radius:5px;text-decoration:none;margin:4px;display:inline-block;font-weight:bold;">Visit Blog</a> '

    # Instagram button — pink
    banner += '<a href="' + INSTAGRAM_URL + '" target="_blank" rel="noopener" style="background:#E1306C;color:#ffffff;'
    banner += 'padding:10px 18px;border-radius:5px;text-decoration:none;margin:4px;display:inline-block;font-weight:bold;">Instagram</a> '

    # LinkedIn button — blue
    banner += '<a href="' + LINKEDIN_URL + '" target="_blank" rel="noopener" style="background:#0077B5;color:#ffffff;'
    banner += 'padding:10px 18px;border-radius:5px;text-decoration:none;margin:4px;display:inline-block;font-weight:bold;">LinkedIn</a> '

    # WhatsApp button — green
    banner += '<a href="' + WHATSAPP_URL + '" target="_blank" rel="noopener" style="background:#25D366;color:#ffffff;'
    banner += 'padding:10px 18px;border-radius:5px;text-decoration:none;margin:4px;display:inline-block;font-weight:bold;">WhatsApp Channel</a>'

    banner += '</p></div>'

    return source_line + "\n" + banner

# ══════════════════════════════════════════════════════
#  RESPONSE CLEANER
# ══════════════════════════════════════════════════════

def clean_and_parse(raw, story):
    raw = re.sub(r"```html\s*", "", raw)
    raw = re.sub(r"```\s*", "", raw)
    raw = raw.strip()
    raw = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", raw)
    raw = re.sub(r"\*(.+?)\*", r"<em>\1</em>", raw)
    raw = re.sub(r"<h1[^>]*>.*?</h1>", "", raw, flags=re.IGNORECASE | re.DOTALL)
    h2_list = re.findall(r"<h2[^>]*>.*?</h2>", raw, re.IGNORECASE | re.DOTALL)
    if len(h2_list) > 1:
        first_pos = raw.lower().find("<h2")
        second_pos = raw.lower().find("<h2", first_pos + 1)
        if second_pos - first_pos < 200:
            raw = raw[:first_pos] + raw[second_pos:]
    title = story["title"]
    m = re.search(r"<h2[^>]*>(.*?)</h2>", raw, re.IGNORECASE | re.DOTALL)
    if m:
        title = re.sub(r"<[^>]+>", "", m.group(1)).strip()
    word_count = len(re.sub(r"<[^>]+>", "", raw).split())
    print("    Words: " + str(word_count))
    return title, raw

# ══════════════════════════════════════════════════════
#  META DESCRIPTION
# ══════════════════════════════════════════════════════

def generate_meta_description(title, html):
    clean = re.sub(r"<[^>]+>", "", html)
    clean = re.sub(r"\s+", " ", clean).strip()
    if clean.lower().startswith(title.lower()[:20].lower()):
        clean = clean[len(title):].strip()
    desc = clean[:147].rsplit(" ", 1)[0] + "..."
    return desc

# ══════════════════════════════════════════════════════
#  AI WRITER
# ══════════════════════════════════════════════════════

def write_post(story):
    prompt = build_prompt(story)
    raw = None

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
            print("  Grok done!")
        except Exception as e:
            print("  Grok error: " + str(e) + " - using Groq...")

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
    
