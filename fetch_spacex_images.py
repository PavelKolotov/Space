import requests
import argparse

from general_function import download_img, separate_extension


def fetch_spacex_last_launch():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'spacex_key',
        nargs='?',
        default='5eb87d19ffd86e000604b366',
        help='Ваш ключ (по умолчанию 5eb87d19ffd86e000604b366)'
    )
    args = parser.parse_args()
    spacex_key = args.spacex_key
    url = f'https://api.spacexdata.com/v5/launches/{spacex_key}'
    response = requests.get(url)
    response.raise_for_status()
    res_links = response.json()['links']['flickr']['original']

    for link_number, link in enumerate(res_links):
        filename_ext = separate_extension(link)
        images_path = f'./images/spacex_{link_number}{filename_ext}'
        download_img(link, images_path)


if __name__ == '__main__':
    fetch_spacex_last_launch()
