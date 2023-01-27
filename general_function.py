import os
import urllib.parse
import requests


from pathlib import Path


def loading_img(url_img, images_path):
    Path("images").mkdir(parents=True, exist_ok=True)
    response = requests.get(url_img)
    response.raise_for_status()

    with open(f'{images_path}', 'wb') as file:
        file.write(response.content)

def ext_file(link):
    url_encoding = urllib.parse.unquote(link)
    url_parse = urllib.parse.urlsplit(url_encoding)
    filename = os.path.split(url_parse.path)[1]
    ext_filename = os.path.splitext(filename)[1]
    return ext_filename