from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
import os
import asyncio

# Загружаем переменные окружения из .env
load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(commands=["start"])
async def start_handler(message: types.Message):
    await message.reply("Привет! Я бот для уведомлений. Введите /notify, чтобы отправить уведомление.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
