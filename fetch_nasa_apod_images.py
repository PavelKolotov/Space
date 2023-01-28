import os
import requests
import argparse

from dotenv import load_dotenv
from general_function import loading_img, ext_file


def fetch_nasa_apod():
    load_dotenv()
    url = "https://api.nasa.gov/planetary/apod"
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
    links_nasa = response.json()
    for link_numbers, link in enumerate(links_nasa):
        url_link = link['url']
        ext_filename = ext_file(url_link)
        images_path = f'./images/nasa_apod_{link_numbers}{ext_filename}'
        if ext_filename:
            loading_img(url_link, images_path)



if __name__ == "__main__":
    fetch_nasa_apod()

