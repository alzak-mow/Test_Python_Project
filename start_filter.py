from aiogram import Bot, Dispatcher
from aiogram.types import Message
from dotenv import dotenv_values


ENV = dotenv_values('.env')
API_URL = ENV.get('API_URL')
BOT_TOKEN = ENV.get('BOT_TOKEN')

##
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def my_start_filter(message: Message) -> bool:
    return message.text and message.text == '/start'

def custom_filter(some_list):
    integers = [item for item in some_list if isinstance(item, int)]
    divisible_by_7 = [num for num in integers if num % 7 == 0]
    total_sum = sum(divisible_by_7)
    return total_sum <= 83

def anonymous_filter(s) -> bool:
    return s.lower().count('я') >= 23

@dp.message(my_start_filter)
async def process_start_command(message: Message):
    await message.answer(text='Это команда /start')

if __name__ == '__main__':
    dp.run_polling(bot)