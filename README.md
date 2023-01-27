# Space

## Описание работы скрипта:
Скрипт скачивает с ресурса NASA и SpaceX фотографии, связанные с космической тематикой.

## Зависимости
Python3:
```
pip install -r requirements.txt
```
## Окружение
.env

TOKEN авторизации NASA
```
NASA_TOKEN=BqnssG5NGr0h61pd0zCkeLQJIBJgd5cX9rAtHMDt
```
## Запуск скрипта в консоли
```
python3 fetch_spacex_images.py 5eb87d47ffd86e000604b38a
# (номер ID, по умолчанию 5eb87d19ffd86e000604b366)

python3 fetch_nasa_apod_images.py 13
# (количество случайных фото, по умолчанию 10)

python3 fetch_nasa_epic_images.py
```
