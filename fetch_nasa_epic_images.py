import os
import requests

from dotenv import load_dotenv
from general_function import loading_img, ext_file

def fetch_nasa_epic():
    load_dotenv()
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    nasa_token = os.environ['NASA_TOKEN']
    params = {
        'api_key': nasa_token,
    }
    i = 0
    response = requests.get(url, params=params)
    links_epic = response.json()
    for link in links_epic:
        img_name = link['image']
        datetime_epic = link['date']
        datetime_parse = datetime_epic.split(' ')
        date_parse = datetime_parse[0].split('-')
        url_img = f'https://api.nasa.gov/EPIC/archive/natural/{date_parse[0]}/{date_parse[1]}/{date_parse[2]}/' \
                  f'png/{img_name}.png?api_key={nasa_token}'
        ext_filename = ext_file(url_img)
        images_path = f'./images/nasa_epic_{i}{ext_filename}'
        loading_img(url_img, images_path)
        i += 1


if __name__ == "__main__":
    fetch_nasa_epic()
