import requests
import argparse

from general_function import loading_img, ext_file
def fetch_spacex_last_launch():
    i = 0
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'key_spacex',
        nargs='?',
        default='5eb87d19ffd86e000604b366',
        help='Ваш ключ (по умолчанию 5eb87d19ffd86e000604b366)'
    )
    args = parser.parse_args()
    key_spacex = args.key_spacex
    url = f'https://api.spacexdata.com/v5/launches/{key_spacex}'
    response = requests.get(url)
    links_res = response.json()['links']['flickr']['original']

    for link in links_res:
        ext_filename = ext_file(link)
        images_path = f'./images/spacex_{i}{ext_filename}'
        loading_img(link, images_path)
        i += 1

if __name__ == "__main__":
    fetch_spacex_last_launch()


