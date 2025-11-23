import requests
import time
from dotenv import dotenv_values


ENV = dotenv_values('.env')
API_URL = ENV.get('API_URL')
BOT_TOKEN = ENV.get('BOT_TOKEN')

if not API_URL or not BOT_TOKEN:
    raise ValueError('Missing required environment variables: API_URL and/or BOT_TOKEN')

offset = -2
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True: 
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    time.sleep(3)
    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')