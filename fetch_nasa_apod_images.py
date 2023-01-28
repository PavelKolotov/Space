import os
import requests
import argparse

from dotenv import load_dotenv
from general_function import download_img, extraction_extension


def fetch_nasa_apod():
    load_dotenv()
    url = 'https://api.nasa.gov/planetary/apod'
    nasa_token = os.environ['NASA_TOKEN']
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'count',
        nargs='?',
        default=10,
        help='Количество случайных фото (по умолчанию 10)'
    )
    args = parser.parse_args()
    count = args.count
    params = {
        'api_key': nasa_token,
        'count': count
    }

    response = requests.get(url, params=params)
    nasa_links = response.json()
    for link_number, link in enumerate(nasa_links):
        url_link = link['url']
        filename_ext = extraction_extension(url_link)
        images_path = f'./images/nasa_apod_{link_number}{filename_ext}'
        if filename_ext:
            download_img(url_link, images_path)


if __name__ == '__main__':
    fetch_nasa_apod()
