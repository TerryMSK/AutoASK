import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers import router

load_dotenv()  # ← ОБЯЗАТЕЛЬНО

async def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN не найден в .env")
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(
        bot,
        allowed_updates=[
            "message",
            "business_message",          # ← без этого бизнес-сообщения не придут
            "edited_business_message"    # если хочешь редактированные
        ]
    )

if __name__ == "__main__":
    asyncio.run(main())