import argparse
from pathlib import Path
import sys
from downloader.bunkr import bunkr_downloader

def parse_args():
    parser = argparse.ArgumentParser(sys.argv[1:])
    parser.add_argument("-u", help="Urls to fetch (comma sep.)", type=str)
    parser.add_argument("-i", help="File with urls", type=Path)
    parser.add_argument("-p", help="Path to custom downloads folder")
    args = parser.parse_args()
    return args

def download(url, custom_path):
    if url.find("Bunkr"): return bunkr_downloader(url, custom_path)

def downloader(args, urls):
    urls_list = urls.split(',') if urls is not None else []
    custom_path = args.p
    if urls_list:
        for url in urls_list: 
            try: 
                download(url, custom_path)
            except Exception:
                print(url + " is not a valid link")

    if args.i:
        with open(args.i, "r", encoding="utf-8") as f:
            while True:
                url = f.readline()
                if not url: break
                download(url)
    return None

def main():
    args = parse_args()
    urls = args.u
    downloader(args, urls)
main()

