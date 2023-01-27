import os
import random
import time
import argparse
import telegram


def telegram_sending():
    bot = telegram.Bot(token='5700058966:AAHE1BskR3-eEwvakuckuMocNILrV5P8Z1E')
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
            bot.send_document(chat_id='@pavelsergeevich84', document=open(f'images/{foto}', 'rb'))
            time.sleep(int(delay))

if __name__ == "__main__":
    telegram_sending()
