from aiogram import Bot


async def send_notification(bot: Bot, user_id: int):
    notification_message = "Это ваше уведомление!"

    # Отправляем сообщение пользователю
    await bot.send_message(chat_id=user_id, text=notification_message)
