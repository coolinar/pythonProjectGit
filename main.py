import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from notifications import send_notification

# Загружаем переменные окружения из .env
load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))  # Исправленный фильтр
async def start_handler(message: types.Message):
    await message.reply("Привет! Я бот для уведомлений. Введите /notify, чтобы отправить уведомление.")

@dp.message(Command("notify"))
async def notify_handler(message: types.Message):
    # Здесь передаем bot в send_notification
    await send_notification(bot, message.from_user.id)

async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    asyncio.run(main())
