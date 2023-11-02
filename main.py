from aiogram import Bot, Dispatcher
# from pathlib import Path
import basic
import asyncio
from get_keys import BOT_KEY


bot = Bot(token=BOT_KEY)
dp = Dispatcher()

async def start():
    dp.include_routers(basic.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
