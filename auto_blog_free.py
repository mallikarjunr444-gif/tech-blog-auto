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
            # (Consider appending the article to articles here, e.g. articles.append({...}))
    except Exception as e:
        print(f"Error in scrape_rss: {e}")
        return []
