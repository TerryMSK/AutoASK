from aiogram import Router, types
from aiogram.filters import Command

router = Router()

# Обработчик всех бизнес-сообщений
@router.business_message()
async def process_business_msg(message: types.Message):
    await message.answer(f'ghbdtn {message.from_user.id}')

# Можно обрабатывать конкретные команды
@router.business_message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать!")