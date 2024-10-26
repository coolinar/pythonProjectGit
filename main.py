import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

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
    # Здесь можно добавить логику отправки уведомления
    await send_notification(message.from_user.id)

async def send_notification(user_id: int):
    # Логика отправки уведомления
    notification_message = "Это ваше уведомление!"
    await bot.send_message(chat_id=user_id, text=notification_message)

async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    asyncio.run(main())
