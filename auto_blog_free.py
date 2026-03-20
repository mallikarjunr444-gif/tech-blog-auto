import os,sys,json,time,random,requests,datetime,re,smtplib,xml.etree.ElementTree as ET
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GROQ_API_KEY=os.environ.get("GROQ_API_KEY","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")
NEWS_API_KEY=os.environ.get("NEWS_API_KEY","673bca5ceab54fa8bb7ed0344c8f6d13")
BLOG_ID="6974086222747114440"
BLOG_URL="https://www.technewsai.me"
BLOGGER_EMAIL="mallikarjunr444.technewswithai6361@blogger.com"
GMAIL_ADDRESS="mallikarjunr444@gmail.com"
GMAIL_PASS=os.environ.get("GMAIL_APP_PASSWORD","oeirtosmlhuwntka")
ARTICLES=3
INSTAGRAM="https://www.instagram.com/mallikarjunr_8055"
LINKEDIN="https://in.linkedin.com/in/mallikarjun-r-a85685367"
WHATSAPP="https://whatsapp.com/channel/0029VazWwdn0wajoizN5PY3Q"
BIO="Mallikarjun R is a first-year Computer Science Engineering student at DSATM, Bengaluru, India. He is passionate about technology, smartphones, and AI. He runs Tech News With AI (technewsai.me) to bring the latest tech news and honest reviews to Indian readers."

INTERNAL=[
    {"title":"Samsung Galaxy A37 and A57 Review","url":"https://www.technewsai.me/2026/03/the-wait-is-over-galaxy-a37-and-a57.html","kw":["samsung","galaxy","android"]},
    {"title":"OPPO Find N6 Review: Gold Standard of Foldables","url":"https://www.technewsai.me/2026/03/oppo-find-n6-review-gold-standard-of.html","kw":["oppo","foldable"]},
    {"title":"ROG Strix Scar 18: Beast Gaming Laptop 2026","url":"https://www.technewsai.me/2026/03/new-rog-strix-scar-18-unleashing-beast.html","kw":["rog","gaming","laptop","asus"]},
    {"title":"Best Battery and Performance Phones 2026","url":"https://www.technewsai.me/2026/03/get-ready-for-battery-and-performance.html","kw":["battery","performance","best phone"]},
]

TOPICS=[
    "best smartphone under 20000 India 2026","best smartphone under 30000 India 2026",
    "best laptop under 50000 India 2026","iPhone 16 price India review 2026",
    "Samsung Galaxy S25 review India price","OnePlus 13 review India price specs",
    "best gaming phone India 2026","best camera phone India 2026",
    "MacBook Air M4 review India price","Xiaomi 15 Ultra review India specs",
    "Poco X7 Pro review India price","Redmi Note 14 Pro review India",
    "Vivo X200 Pro review India price","iQOO 13 review India price specs",
    "Google Pixel 9 Pro review India","Motorola Edge 50 review India",
    "Nothing Phone 3 review India specs","best TWS earbuds under 5000 India 2026",
    "best smartwatch under 10000 India 2026","Dell XPS 15 review India price 2026",
    "HP Spectre review India price 2026","ASUS Zenbook review India 2026",
    "best Android tablet India 2026","5G phone under 15000 India 2026",
    "best phone for students India 2026","Apple vs Samsung flagship India 2026",
    "Realme GT 7 Pro review India","Samsung Galaxy A launch India specs 2026",
]

RSS=[
    ("The Verge","https://www.theverge.com/rss/index.xml"),
    ("TechCrunch","https://techcrunch.com/feed/"),
    ("CNET","https://www.cnet.com/rss/news/"),
    ("GSMArena","https://www.gsmarena.com/rss-news-articles.php3"),
    ("AndroidAuthority","https://www.androidauthority.com/feed/"),
    ("XDA Developers","https://www.xda-developers.com/feed/"),
    ("91Mobiles","https://www.91mobiles.com/hub/feed/"),
    ("MySmartPrice","https://www.mysmartprice.com/feed/"),
    ("GizmoChina","https://www.gizmochina.com/feed/"),
    ("GadgetsNow","https://www.gadgetsnow.com/rssfeedstopstories.cms"),
]

def fetch_rss(name,url,kw):
    try:
        r=requests.get(url,timeout=8,headers={"User-Agent":"Mozilla/5.0"})
        if r.status_code!=200:return[]
        root=ET.fromstring(r.content)
        ns={"atom":"http://www.w3.org/2005/Atom"}
        items=root.findall(".//item") or root.findall(".//atom:entry",ns)
        arts=[]
        for item in items[:10]:
            t=item.find("title")
            title=t.text if t is not None else ""
            if not title:continue
            if kw.lower().split()[0] not in title.lower():continue
            d=item.find("description") or item.find("summary")
            desc=re.sub(r"<[^>]+>","",d.text if d is not None else "")[:400]
            l=item.find("link")
            link=l.text if l is not None else url
            p=item.find("pubDate") or item.find("published")
            pub=p.text if p is not None else "2026-03-20T00:00:00Z"
            if title and desc:
                arts.append({"title":title.strip(),"description":desc.strip(),"content":desc.strip(),"url":link.strip(),"source":name,"published":pub})
        return arts[:3]
    except:return[]

def fetch_newsapi(q,n=3):
    try:
        r=requests.get("https://newsapi.org/v2/everything",params={"q":q,"language":"en","sortBy":"publishedAt","pageSize":n,"apiKey":NEWS_API_KEY},timeout=10)
        d=r.json()
        if d.get("status")!="ok":return[]
        return [{"title":a["title"],"description":a.get("description") or "","content":a.get("content") or "","url":a["url"],"source":a["source"]["name"],"published":a["publishedAt"]} for a in d.get("articles",[]) if a.get("title") and a.get("description")]
    except:return[]

def fetch(q,n=3):
    print("  Searching: "+q)
    arts=[]
    kw=q.split()[0]
    feeds=RSS[:]
    random.shuffle(feeds)
    for name,url in feeds[:8]:
        arts.extend(fetch_rss(name,url,kw))
        if len(arts)>=3:break
    if len(arts)<2:arts.extend(fetch_newsapi(q,n))
    seen=set()
    unique=[a for a in arts if not (a["title"] in seen or seen.add(a["title"]))]
    print("    "+str(len(unique))+" found")
    return unique[:n]

def pick():
    topics=TOPICS[:]
    random.shuffle(topics)
    for t in topics:
        arts=fetch(t)
        if arts:
            s=arts[0]
            print("  Picked: "+s["title"])
            return s
    return None

def get_links(title,desc):
    text=(title+" "+desc).lower()
    rel=[l for l in INTERNAL if any(k in text for k in l["kw"])]
    if not rel:rel=random.sample(INTERNAL,min(2,len(INTERNAL)))
    return rel[:2]

def author_box():
    h='<div style="background:#f8f9fa;border:1px solid #e0e0e0;padding:20px;margin:32px 0;border-radius:8px;">'
    h+='<p style="font-size:18px;font-weight:bold;">About the Author</p>'
    h+='<p style="color:#333;">'+BIO+'</p>'
    h+='<p><strong>Follow Mallikarjun:</strong> '
    h+='<a href="'+INSTAGRAM+'" target="_blank" style="color:#E1306C;margin-right:12px;">Instagram</a>'
    h+='<a href="'+LINKEDIN+'" target="_blank" style="color:#0077B5;margin-right:12px;">LinkedIn</a>'
    h+='<a href="'+WHATSAPP+'" target="_blank" style="color:#25D366;">WhatsApp</a></p></div>'
    return h

def social_footer(story):
    src=story["source"]
    pub=story["published"][:10]
    url=story["url"]
    h='<hr><p><em><strong>Source:</strong> '+src+' | <strong>Published:</strong> '+pub
    h+=' | <a href="'+url+'" target="_blank">Read original</a></em></p>'
    h+='<div style="background:#111111;color:#fff;padding:24px;border-radius:8px;margin:24px 0;text-align:center;">'
    h+='<p style="font-size:18px;font-weight:bold;color:#fff;">Stay Connected with Tech News With AI</p>'
    h+='<p style="color:#ccc;">Daily tech news and reviews from India</p><p>'
    h+='<a href="'+BLOG_URL+'" style="background:#fff;color:#111;padding:10px 16px;border-radius:5px;text-decoration:none;margin:4px;display:inline-block;font-weight:bold;">Visit Blog</a> '
    h+='<a href="'+INSTAGRAM+'" target="_blank" style="background:#E1306C;color:#fff;padding:10px 16px;border-radius:5px;text-decoration:none;margin:4px;display:inline-block;font-weight:bold;">Instagram</a> '
    h+='<a href="'+LINKEDIN+'" target="_blank" style="background:#0077B5;color:#fff;padding:10px 16px;border-radius:5px;text-decoration:none;margin:4px;display:inline-block;font-weight:bold;">LinkedIn</a> '
    h+='<a href="'+WHATSAPP+'" target="_blank" style="background:#25D366;color:#fff;padding:10px 16px;border-radius:5px;text-decoration:none;margin:4px;display:inline-block;font-weight:bold;">WhatsApp</a>'
    h+='</p></div>'
    return h

PROMPT_SYS="You are Mallikarjun R, a first-year CS student from Bengaluru who runs a tech blog technewsai.me. Write as a real Indian person with opinions. EEAT: show experience, expertise, authority, trust. Use personal hooks. Mention India prices in INR (USD x 85). Reference Flipkart, Amazon India, EMI options. Compare 2 competitors. BANNED words: Furthermore, Moreover, In conclusion, It is worth noting. NO bullet points. NO markdown. NO asterisks. Clean HTML only using h2 h3 p strong tags. Min 2800 words. Include sections: Opening Hook, Design, Display, Performance, Camera, Battery, Software, India Price, Pros and Cons, Comparison, Who Should Buy, Final Verdict, FAQ."

def write(story):
    prompt=("Write complete expert tech article for Indian readers.\n"
            "TOPIC: "+story["title"]+"\n"
            "SUMMARY: "+story["description"]+"\n"
            "DETAILS: "+(story["content"][:600] if story["content"] else "Use knowledge")+"\n"
            "SOURCE: "+story["source"]+"\n\n"
            "RULES: H2 title with keyword. 2800+ words. 13 sections. "
            "Indian journalist voice. INR prices with EMI. "
            "Compare 2 competitors. Pros paragraph. Cons paragraph. "
            "5 FAQ paragraphs. strong tags for specs. Clean HTML only.\n\n"
            "Write full article now:")
    print("  Writing with Groq...")
    from groq import Groq
    client=Groq(api_key=GROQ_API_KEY)
    resp=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"system","content":PROMPT_SYS},{"role":"user","content":prompt}],
        max_tokens=4096,temperature=0.75)
    raw=resp.choices[0].message.content
    raw=re.sub(r"```html\s*","",raw)
    raw=re.sub(r"```\s*","",raw)
    raw=re.sub(r"\*\*(.+?)\*\*",r"<strong>\1</strong>",raw)
    raw=re.sub(r"\*(.+?)\*",r"<em>\1</em>",raw)
    raw=re.sub(r"<h1[^>]*>.*?</h1>","",raw,flags=re.IGNORECASE|re.DOTALL)
    raw=raw.strip()
    title=story["title"]
    m=re.search(r"<h2[^>]*>(.*?)</h2>",raw,re.IGNORECASE|re.DOTALL)
    if m:title=re.sub(r"<[^>]+>","",m.group(1)).strip()
    words=len(re.sub(r"<[^>]+>","",raw).split())
    print("  Words: "+str(words))
    links=get_links(title,story["description"])
    lhtml="<h3>Related Articles</h3><p>Also read: "
    lhtml+=", ".join(['<a href="'+l["url"]+'">'+l["title"]+"</a>" for l in links])+".</p>"
    final=raw+"\n"+lhtml+"\n"+author_box()+"\n"+social_footer(story)
    return title,final

def labels(title,html):
    text=(title+" "+html[:400]).lower()
    labs=["Tech News","India"]
    lmap={"iphone":["iPhone","Apple"],"macbook":["MacBook","Laptop"],"samsung":["Samsung","Android"],"oneplus":["OnePlus","Android"],"realme":["Realme","Android"],"xiaomi":["Xiaomi","Android"],"poco":["Poco","Android"],"redmi":["Redmi","Android"],"vivo":["Vivo","Android"],"iqoo":["iQOO","Android"],"google":["Google"],"pixel":["Google Pixel"],"motorola":["Motorola"],"nothing":["Nothing Phone"],"oppo":["OPPO","Android"],"laptop":["Laptop"],"gaming":["Gaming"],"foldable":["Foldable"],"ai":["AI"],"earbuds":["Earbuds"],"smartwatch":["Smartwatch"]}
    for k,v in lmap.items():
        if k in text:
            for t in v:
                if t not in labs:labs.append(t)
    labs.append(str(datetime.datetime.now().year))
    return labs[:10]

def post(title,html,labs):
    print("  Posting via email...")
    pw=os.environ.get("GMAIL_APP_PASSWORD",GMAIL_PASS)
    msg=MIMEMultipart("alternative")
    msg["Subject"]=title
    msg["From"]=GMAIL_ADDRESS
    msg["To"]=BLOGGER_EMAIL
    msg.attach(MIMEText(html,"html"))
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as s:
        s.login(GMAIL_ADDRESS,pw)
        s.sendmail(GMAIL_ADDRESS,BLOGGER_EMAIL,msg.as_string())
    print("  Posted! "+BLOG_URL)
    return BLOG_URL

def save(title,url):
    f="posted_articles.json"
    log=[]
    if os.path.exists(f):
        with open(f) as fp:log=json.load(fp)
    log.append({"title":title,"url":url,"posted_at":datetime.datetime.now().isoformat()})
    with open(f,"w") as fp:json.dump(log,fp,indent=2)
    print("  Saved ("+str(len(log))+" total)")

def main():
    print("="*50)
    print("  TECH NEWS WITH AI v5.0 - "+BLOG_URL)
    print("="*50)
    ok=0
    for i in range(ARTICLES):
        try:
            print("\n--- Article "+str(i+1)+" of "+str(ARTICLES)+" ---")
            story=pick()
            if not story:continue
            title,html=write(story)
            labs=labels(title,html)
            url=post(title,html,labs)
            save(title,url)
            ok+=1
            if i<ARTICLES-1:
                print("  Waiting 20s...")
                time.sleep(20)
        except KeyboardInterrupt:break
        except Exception as e:
            print("  Error: "+str(e))
    print("\n"+"="*50)
    print("  DONE! "+str(ok)+"/"+str(ARTICLES)+" posted!")
    print("="*50)

if __name__=="__main__":
    main()
  
