import os
import requests

from dotenv import load_dotenv
from general_function import download_img, extraction_extension


def fetch_nasa_epic():
    load_dotenv()
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    nasa_token = os.environ['NASA_TOKEN']
    params = {
        'api_key': nasa_token,
    }
    response = requests.get(url, params=params)
    epic_links = response.json()
    for link_number, link in enumerate(epic_links):
        img_name = link['image']
        date_time_str = link['date']
        date_time_list = date_time_str.split(' ')
        date_list = date_time_list[0].split('-')
        img_url = f'https://api.nasa.gov/EPIC/archive/natural/{date_list[0]}/{date_list[1]}/{date_list[2]}/' \
                  f'png/{img_name}.png'
        img_resp = requests.get(img_url, params=params)
        img_link = img_resp.url
        filename_ext = extraction_extension(img_link)
        images_path = f'./images/nasa_epic_{link_number}{filename_ext}'
        download_img(img_link, images_path)


if __name__ == '__main__':
    fetch_nasa_epic()
