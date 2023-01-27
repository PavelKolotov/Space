import os
import urllib.parse
import requests


from pathlib import Path
from dotenv import load_dotenv


Path("images").mkdir(parents=True, exist_ok=True)

def loading_img(url_img, images_path):
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

def fetch_spacex_last_launch():
    i = 0
    key_spacex = '5eb87d19ffd86e000604b366'
    url = f'https://api.spacexdata.com/v5/launches/{key_spacex}'
    response = requests.get(url)
    links_res = response.json()['links']['flickr']['original']

    for link in links_res:
        ext_filename = ext_file(link)
        images_path = f'./images/spacex_{i}{ext_filename}'
        loading_img(link, images_path)
        i += 1

def fetch_nasa_apod():
    load_dotenv()
    url = "https://api.nasa.gov/planetary/apod"
    nasa_token = os.environ['NASA_TOKEN']
    params = {
        'api_key': nasa_token,
        'count': 30
    }
    i = 0
    response = requests.get(url, params=params)
    links_nasa = response.json()
    for link in links_nasa:
        url_link = link['url']
        ext_filename = ext_file(url_link)
        images_path = f'./images/nasa_apod_{i}{ext_filename}'
        if ext_filename:
            loading_img(url_link, images_path)
        i += 1

def fetch_nasa_epik():
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

def main():
    fetch_spacex_last_launch()
    fetch_nasa_apod()
    fetch_nasa_epik()


if __name__ == "__main__":
    main()


