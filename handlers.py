from aiogram import Router, types
from aiogram.filters import Command
from aiogram import F
from aiogram import Bot

router = Router()

@router.business_message()
async def all_pick_message(message: types.Message, bot: Bot):
    connection = await bot.get_business_connection(message.business_connection_id)
    owner_id = connection.user.id
    if message.from_user.id == owner_id:
        whoisit = f"@{message.chat.username}" if message.chat.username else message.chat.first_name
        text = f"Ваше сообщение для {whoisit}:\n{message.text}"
    else:
        whoisit = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
        text = f"Сообщение от {whoisit}:\n{message.text}"
    await bot.send_message(chat_id=owner_id, text=text)

@router.deleted_business_messages()
async def on_deleted(event: types.BusinessMessagesDeleted, bot: Bot):
    connection = await bot.get_business_connection(event.business_connection_id)
    owner_id = connection.user.id
    chat = f"@{event.chat.username}" if event.chat.username else event.chat.first_name

    await bot.send_message(
        chat_id=owner_id,
        text=f"{chat} удалил сообщений: {len(event.message_ids)}"
    )