from M3U8.lib.engine import M3U8
import logging
import requests
from urllib.parse import urlparse
from pathlib import Path
from M3U8.lib import exceptions
from M3U8.lib.engine import M3U8
from M3U8.lib.utils import parse_ts_url
from M3U8.config.setting import proxy, headers
import m3u8

class Downloader(object):

    def __init__(self, url, file):
        self._logger = self._config_logger()
        self._config = self._config_request()
        self._file_name = file
        self._url = url

    def _config_logger(self):
        logging.basicConfig()
        logger = logging.getLogger(name = __file__)
        logger.setLevel(logging.INFO)
        return logger

    def _config_request(self):
        if proxy is not None:
            return {"headers" : headers,
                    "proxies" : proxy,}
        return {"headers" : headers}

    @staticmethod
    def is_url(i):
       try:
           result = urlparse(i)
           return True
       except:
           return False

    @staticmethod
    def is_file(i):
        file = Path(i)
        if file.is_file():
            return True
        else:
            return False

    def _get_playlists(self, input):
        if Downloader.is_file(input):
            with open(input, "r") as f:
                raw = f.read()
            n3u8_obj = m3u8.loads(raw)
            return  n3u8_obj.segments.uri

        elif Downloader.is_url(input):
            return self._request_for_m3u8(input)

        else:
            raise exceptions.InvalidInput()

    def _request_for_m3u8(self, url):
        raw = requests.get(url, **self._config).content.decode("utf-8")
        m3u8_obj = m3u8.loads(raw)
        return m3u8_obj.segments.uri

    def start(self):
        playlists = self._get_playlists(self._url)
        playlists = [parse_ts_url(url) for url in playlists]
        engine = M3U8(playlists, self._file_name)
        engine.start()

