import logging
import asyncio

from bot_config import bot, dp, database
from aiogram import Bot
from handlers.start import start_router
from handlers.dialog_dz import dialog_router


async def on_startup(bot: Bot):
    database.create_table()


async def main():
    dp.startup.register(on_startup)
    dp.include_router(start_router)
    dp.include_router(dialog_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
