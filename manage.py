import sys
import os
import argparse
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from M3U8.bin.download import Downloader

def main():
    options = argparse.ArgumentParser()
    options.add_argument("-f", "--file", type = str, required = True)
    options.add_argument("-u", "--url", type = str, required = True)
    args = options.parse_args()

    downloader = Downloader(args.url, args.file)
    downloader.start()


if __name__ == "__main__":
    main()

