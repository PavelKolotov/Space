import os
import urllib.parse
import requests

from pathlib import Path


def download_img(img_url, images_path):
    Path('images').mkdir(parents=True, exist_ok=True)
    response = requests.get(img_url)
    response.raise_for_status()

    with open(f'{images_path}', 'wb') as file:
        file.write(response.content)


def separate_extension(link):
    url_encoding = urllib.parse.unquote(link)
    url_parse = urllib.parse.urlsplit(url_encoding)
    filename = os.path.split(url_parse.path)[1]
    filename_ext = os.path.splitext(filename)[1]
    return filename_ext
