import os
import requests

from dotenv import load_dotenv
from general_function import loading_img, file_ext

def fetch_nasa_epic():
    load_dotenv()
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    nasa_token = os.environ['NASA_TOKEN']
    params = {
        'api_key': nasa_token,
    }
    response = requests.get(url, params=params)
    epic_links = response.json()
    for link_number, link in enumerate(epic_links):
        img_name = link['image']
        datetime_epic = link['date']
        datetime_parse = datetime_epic.split(' ')
        date_parse = datetime_parse[0].split('-')
        img_url = f'https://api.nasa.gov/EPIC/archive/natural/{date_parse[0]}/{date_parse[1]}/{date_parse[2]}/' \
                  f'png/{img_name}.png?api_key={nasa_token}'
        filename_ext = file_ext(img_url)
        images_path = f'./images/nasa_epic_{link_number}{filename_ext}'
        loading_img(img_url, images_path)


if __name__ == "__main__":
    fetch_nasa_epic()
