import asyncio
from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv
import os
from handlers.user_private import router
load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()




async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


asyncio.run(main())
