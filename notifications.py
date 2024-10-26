from aiogram import types

async def send_notification(message: types.Message):
    # Пример отправки уведомления
    await message.answer("Это уведомление было отправлено!")
