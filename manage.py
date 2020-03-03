import sys
import os
import argparse

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from bin.twitter import Twitter
from bin.default import Default
from bin.demo import Demo

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", type = str, help = "m3u8 url", required = True)
    parser.add_argument("-f", "--file", type = str, help = "output file name", required = True)
    parser.add_argument("-m", "--mode", type = str, help = "download mode", required = False)
    args = parser.parse_args()

    if args.mode == "twitter":
        downloader = Twitter(args.url, args.file)
        downloader.start()
    elif args.mode == "own":
        downloader = Demo(args.url, args.file)
        downloader.start()
    else:
        downloader = Default(args.url, args.file)
        downloader.start()

if __name__ == "__main__":
    main()

