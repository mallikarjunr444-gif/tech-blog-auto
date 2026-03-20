# TECH NEWS WITH AI — AUTO BLOG
# technewswithai.blogspot.com

GROQ_API_KEY       = "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"
NEWS_API_KEY       = "673bca5ceab54fa8bb7ed0344c8f6d13"
BLOGGER_POST_EMAIL = "mallikarjunr444.technewswithai6361@blogger.com"
GMAIL_ADDRESS      = "mallikarjunr444@gmail.com"
GMAIL_APP_PASSWORD = "oeirtosmlhuwntka"
ARTICLES_PER_RUN   = 1

TOPICS = [
    "Samsung Galaxy launch India 2026",
    "iPhone launch specs India 2026",
    "OPPO phone launch India 2026",
    "OnePlus launch India 2026",
    "Xiaomi Redmi launch India 2026",
    "Realme phone launch India 2026",
    "Vivo iQOO launch India 2026",
    "Nothing phone launch 2026",
    "Honor Huawei launch 2026",
    "Google Pixel launch India 2026",
    "Motorola launch India 2026",
    "MacBook launch price India 2026",
    "Dell HP Lenovo laptop launch India 2026",
    "ASUS Acer laptop launch India 2026",
    "AirPods launch specs India 2026",
    "Sony headphones launch India 2026",
    "Samsung Galaxy Buds launch 2026",
    "OnePlus Buds launch India 2026",
    "Boat earphones launch India 2026",
    "smartwatch launch India 2026",
    "Apple Watch launch India 2026",
    "iPad launch specs India 2026",
    "Samsung Galaxy Tab launch India 2026",
    "smart TV launch India 2026",
]

import os, sys, json, time, random, requests, datetime, re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
    from groq import Groq
except ImportError:
    print("Run: pip install groq")
    sys.exit(1)

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def fetch_news(query):
    try:
        r = requests.get(
            "https://newsapi.org/v2/everything",
            params={"q": query, "language": "en", "sortBy": "publishedAt",
                    "pageSize": 5, "apiKey": NEWS_API_KEY},
            timeout=10)
        data = r.json()
        if data.get("status") != "ok":
            return []
        return [a for a in data.get("articles", [])
                if a.get("title") and a.get("description")]
    except Exception:
        return []

def get_specs(device):
    try:
        q = device.replace(" ", "+")
        r = requests.get(f"https://www.gsmarena.com/search.php3?sQuickSearch={q}",
                        headers=HEADERS, timeout=8)
        links = re.findall(r'href="([a-z0-9_]+-\d+\.php)"', r.text)
        if not links:
            return ""
        r2 = requests.get(f"https://www.gsmarena.com/{links[0]}",
                         headers=HEADERS, timeout=8)
        pairs = re.findall(
            r'<td class="ttl">.*?<a[^>]*>([^<]+)</a>.*?</td>\s*<td class="nfo">([^<]+)',
            r2.text, re.DOTALL)
        specs = "\n".join([f"{k.strip()}: {v.strip()}" for k, v in pairs[:30]])
        return specs
    except Exception:
        return ""

def pick_story():
    topics = TOPICS.copy()
    random.shuffle(topics)
    for topic in topics:
        articles = fetch_news(topic)
        if articles:
            a = articles[0]
            specs = get_specs(a["title"])
            return {
                "title": a["title"],
                "description": a.get("description", ""),
                "url": a["url"],
                "source": a["source"]["name"],
                "published": a["publishedAt"],
                "specs": specs,
            }
    return None

SYSTEM = """You are Mallikarjun R — a 19-year-old CSE student and tech blogger from Bengaluru, India running technewswithai.blogspot.com.

WRITE LIKE A REAL HUMAN — NOT AI:
- Use first person: "I think", "honestly", "in my opinion", "I noticed"
- Natural Indian English: "quite good", "value for money", "not bad at all"
- Mix short and long sentences — vary your rhythm
- Ask questions: "But is it worth your money?"
- Be honest about flaws — nothing is perfect
- Reference India: "using this in Bengaluru traffic", "watching IPL on it"
- Add predictions: "I think by 2027..."
- Never say "In conclusion", "To summarize", "It is worth noting"
- Never sound like a robot or product brochure

ADSENSE QUALITY — MANDATORY:
- Minimum 3000 words
- Every section minimum 4 paragraphs of 4-5 sentences
- Use ONLY real specs provided — never invent
- Real world examples in every section
- Compare with 3 competitors by name and price
- India pricing with Flipkart/Amazon and EMI
- Bold important keywords with <strong> tags

SEO STRUCTURE:
- 3 strong intro paragraphs before first heading
- H2 for main sections, H3 for subsections
- FAQ section with 7 questions and detailed answers
- Author bio at the very end

FORMAT: Clean HTML only — h2, h3, p, strong tags. No markdown. No bullet points. No tables."""

def write_post(story):
    print(f"  Writing article: {story['title'][:50]}...")
    client = Groq(api_key=GROQ_API_KEY)
    today = datetime.datetime.now().strftime("%B %d, %Y")

    prompt = f"""Write a complete 3000+ word AdSense-ready blog article.

DEVICE: {story['title']}
SOURCE: {story['source']}

REAL SPECS FROM GSMARENA:
{story['specs'] if story['specs'] else 'Specs not available — use what you know'}

EXTRA INFO: {story['description']}

WRITE AS MALLIKARJUN R — real human blogger from Bengaluru.

MANDATORY SECTIONS (4+ paragraphs each):
1. Introduction (3 paragraphs before first h2 — powerful hook)
2. Design and First Impressions
3. Display Quality (h3: Panel Technology, h3: Real World Use)
4. Camera System (h3: Photos, h3: Videos)
5. Performance and Gaming (h3: Daily Use, h3: Gaming)
6. Battery Life (h3: Real World Hours, h3: Charging)
7. Software and AI Features
8. Price in India (h3: All Variants and EMI, h3: Buy Now or Wait?)
9. Who Should Buy and Who Should Avoid
10. Top 3 Alternatives with Honest Comparison
11. My Final Verdict
12. FAQ — 7 questions with 3-4 sentence answers each

END WITH THIS AUTHOR BIO:
<div style="background:#f0f7ff;border-left:4px solid #1a73e8;padding:20px;margin:30px 0;border-radius:8px;">
<p><strong>Written by Mallikarjun R</strong><br/>CSE Student &amp; Tech Blogger, Bengaluru, India<br/><em>Published: {today}</em></p>
<p>I cover smartphones, laptops and audio gear with honest India-focused reviews. Follow on <a href="https://www.instagram.com/mallikarjunr_8055">Instagram</a> | <a href="https://whatsapp.com/channel/0029VazWwdn0wajoizN5PY3Q">WhatsApp</a></p>
</div>

Write the full article now in clean HTML:"""

    try:
        r = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": prompt}
            ],
            max_tokens=7000,
            temperature=0.8,
        )
        raw = re.sub(r"```html|```", "", r.choices[0].message.content).strip()

        title = story["title"]
        m = re.search(r"<h2[^>]*>(.*?)</h2>", raw, re.IGNORECASE | re.DOTALL)
        if m:
            title = re.sub(r"<[^>]+>", "", m.group(1)).strip()

        words = len(re.sub(r"<[^>]+>", "", raw).split())
        print(f"  Done — {words} words")

        if words < 2000:
            print(f"  Extending article...")
            r2 = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": SYSTEM},
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": raw},
                    {"role": "user", "content": "Too short for AdSense. Add 1000 more words: expand Camera and Performance sections with 3 more paragraphs each, add 3 more FAQ answers. Output only additional HTML."}
                ],
                max_tokens=3000,
                temperature=0.8,
            )
            extra = re.sub(r"```html|```", "", r2.choices[0].message.content).strip()
            raw = raw + extra
            words = len(re.sub(r"<[^>]+>", "", raw).split())
            print(f"  Extended to {words} words")

        footer = f"""
<hr/>
<p><em>Source: {story['source']} | <a href="{story['url']}" target="_blank">Original Article</a> | <a href="https://technewswithai.blogspot.com">More on Tech News With AI</a></em></p>"""

        return title, raw + footer

    except Exception as e:
        print(f"  Error: {e}")
        raise

def post_email(title, html):
    print(f"  Posting via email...")
    pw = os.environ.get("GMAIL_APP_PASSWORD", GMAIL_APP_PASSWORD)
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = title
        msg["From"] = GMAIL_ADDRESS
        msg["To"] = BLOGGER_POST_EMAIL
        msg.attach(MIMEText(html, "html"))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
            s.login(GMAIL_ADDRESS, pw)
            s.sendmail(GMAIL_ADDRESS, BLOGGER_POST_EMAIL, msg.as_string())
        print(f"  Posted! https://technewswithai.blogspot.com")
        return "https://technewswithai.blogspot.com"
    except Exception as e:
        print(f"  Email error: {e}")
        raise

def save_log(title, url):
    log = []
    if os.path.exists("posted_articles.json"):
        try:
            with open("posted_articles.json") as f:
                log = json.load(f)
        except Exception:
            log = []
    log.append({"title": title, "url": url,
                "posted_at": datetime.datetime.now().isoformat()})
    with open("posted_articles.json", "w") as f:
        json.dump(log, f, indent=2)
    print(f"  Log saved — total {len(log)} posts")

def main():
    print("""
╔══════════════════════════════════════════╗
║  TECH NEWS WITH AI — AUTO BLOG          ║
║  technewswithai.blogspot.com            ║
╚══════════════════════════════════════════╝""")

    success = 0
    for i in range(ARTICLES_PER_RUN):
        try:
            print(f"\n Article {i+1}/{ARTICLES_PER_RUN}")
            story = pick_story()
            if not story:
                print("  No story found!")
                continue
            title, html = write_post(story)
            url = post_email(title, html)
            save_log(title, url)
            success += 1
            if i < ARTICLES_PER_RUN - 1:
                time.sleep(30)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"  Failed: {e}")
            continue

    print(f"\n Done! {success}/{ARTICLES_PER_RUN} posted!")

if __name__ == "__main__":
    main()
        
