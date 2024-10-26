from aiogram import Bot, Dispatcher, types, F
from dotenv import load_dotenv
import os
import asyncio
from notifications import send_notification  # Убедитесь, что этот импорт корректен

# Загружаем переменные окружения из .env
load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(F.command("start"))
async def start_handler(message: types.Message):
    await message.reply("Привет! Я бот для уведомлений. Введите /notify, чтобы отправить уведомление.")

@dp.message(F.command("notify"))
async def notify_handler(message: types.Message):
    # Здесь вызываем функцию отправки уведомления
    await send_notification(message)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
