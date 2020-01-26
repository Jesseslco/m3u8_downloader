import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from M3U8.bin.download import Downloader

def main():
    downloader = Downloader()
    downloader.start()


if __name__ == "__main__":
    main()

