from bin.download import Downloader
from lib import exceptions
import m3u8
import requests

class Twitter(Downloader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _parse_file(self, file):
        with open(input, "r") as f:
            raw = f.read()
        m3u8_obj = m3u8.loads(raw)
        return m3u8_obj.segments.uri

    def _parse_url(self, url):
        proxies = {"http":"http://127.0.0.1:7890",
                   "https":"http://127.0.0.1:7890"}

        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
                   'method': "GET"}

        raw = requests.get(url, proxies = proxies, headers = headers).content.decode("utf-8")
        m3u8_obj = m3u8.loads(raw)
        playlists = m3u8_obj.segments.uri
        return list(map(self.parse_ts_url, playlists))

    def parse_ts_url(self, url):
        from urllib.parse import urljoin
        url = urljoin("https://video.twimg.com", url)
        return url

    def _parse_content(self, content):
        return content

