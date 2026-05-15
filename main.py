import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers import router
from aiogram.client.session.aiohttp import AiohttpSession

load_dotenv()

async def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router) 

    await dp.start_polling(
        bot,
        allowed_updates=[
            "message",
            "business_message",
            "edited_business_message",
            "deleted_business_messages"
        ]
    )

if __name__ == "__main__":
    asyncio.run(main())