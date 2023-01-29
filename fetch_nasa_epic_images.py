import os
import requests

from dotenv import load_dotenv
from general_function import download_img, separate_extension


def fetch_nasa_epic():
    load_dotenv()
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    nasa_token = os.environ['NASA_TOKEN']
    params = {
        'api_key': nasa_token,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_links = response.json()
    for link_number, link in enumerate(epic_links):
        img_name = link['image']
        datetime_img = link['date']
        date_time_img = datetime_img.split(' ')
        date_img = date_time_img[0].split('-')
        img_url = f'https://api.nasa.gov/EPIC/archive/natural/{date_img[0]}/{date_img[1]}/{date_img[2]}/' \
                  f'png/{img_name}.png'
        img_resp = requests.get(img_url, params=params)
        img_resp.raise_for_status()
        img_link = img_resp.url
        filename_ext = separate_extension(img_link)
        images_path = f'./images/nasa_epic_{link_number}{filename_ext}'
        download_img(img_link, images_path)


if __name__ == '__main__':
    fetch_nasa_epic()
