from lib.engine import M3U8
import logging
from urllib.parse import urlparse
from pathlib import Path
from lib import exceptions
from lib.engine import M3U8

class Downloader(object):

    def __init__(self, url, file):
        self._logger = self._config_logger()
        self._url = url
        self._file = file

    def _config_logger(self):
        logging.basicConfig()
        logger = logging.getLogger(name = __file__)
        logger.setLevel(logging.INFO)
        return logger

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
            return self._parse_file(input)

        elif Downloader.is_url(input):
            return self._parse_url(input)

        else:
            raise exceptions.InvalidInput()

    def _parse_file(self, file):
        raise exceptions.NotImplementedException

    def _parse_url(self, url):
        raise exceptions.NotImplementedException()

    def _parse_content(self, content):
        raise exceptions.NotImplementedException()

    def start(self):
        playlists = self._get_playlists(self._url)

        self._logger.info(f"length of playlists : {len(playlists)}")

        engine = M3U8(playlists, self._file, self._parse_content)
        engine.start()

