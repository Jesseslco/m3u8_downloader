def parse_content(content):
    return content

def parse_ts_url(url):
    from urllib.parse import urljoin
    url = urljoin("https://video.twimg.com", url)
    return url
