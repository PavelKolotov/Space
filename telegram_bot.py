import telegram


bot = telegram.Bot(token='5700058966:AAHE1BskR3-eEwvakuckuMocNILrV5P8Z1E')
print(bot.get_me())


bot.send_document(chat_id='@pavelsergeevich84', document=open('images/nasa_epic_0.png', 'rb'))
