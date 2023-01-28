import io
import os
import random
import time
import argparse
import telegram

from dotenv import load_dotenv
from io import BytesIO


def telegram_sending():
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    bot = telegram.Bot(token=telegram_token)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'delay',
        nargs='?',
        default=14400,
        help='Время задержки в секундах (по умолчанию 4 часа)'
    )
    args = parser.parse_args()
    delay = args.delay
    while True:
        images = os.walk('images')
        for img in images:
            foto = random.choice(img[2])
            chat_id = os.environ['TELEGRAM_CHAT_ID']

            with open(f'images/{foto}', 'rb') as file:
                file_obj = io.BytesIO(file.read())
                file_obj.name = foto
                bot.send_document(chat_id=chat_id, document=file_obj)
            time.sleep(int(delay))


if __name__ == '__main__':
    telegram_sending()
