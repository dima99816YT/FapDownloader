import requests
import os
from bs4 import BeautifulSoup
URL = "https://media-files12.bunkr.la/"

def get_items_list(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    albums = soup.find_all('a', {"class": "grid-images_box-link"})
    urls = []

    for album in albums:
        url = album.get("href").split("/")[3]
        urls.append(url)
    return urls

def check_is_album(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    if soup.find('a', {"class": "grid-images_box-link"}):
        return True
    return False

def get_final_path(link, custom_path):
    if custom_path != None:
        final_path = os.path.join(custom_path, link)
        return final_path
    return link

def bunkr_downloader(url, custom_path=None):
    if check_is_album(url):
        urls = get_items_list(url)
        for link in urls:
            r = requests.get(URL+link, stream=True)
            link = get_final_path(link, custom_path)
            with open(link, "wb") as video:
                for chunk in r.iter_content(chunk_size=1024*1024):
                    if chunk:
                        video.write(chunk)
            print(link + " downloaded")
        return True
    
    link = url.split("/")[4].replace('\n', '')
    r = requests.get(URL+link, stream=True)
    link = get_final_path(link, custom_path)
    with open(link, "wb") as video:
        for chunk in r.iter_content(chunk_size=1024*1024):
            if chunk:
                video.write(chunk)
    print(link + " downloaded")
    return True
    
        
