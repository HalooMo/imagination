from aiogram import Dispatcher, Router, Bot
from aiogram.fsm.storage.memory import MemoryStorage
from  aiogram.enums.parse_mode import ParseMode
import Handlers
import asyncio
from  aiogram.utils.chat_action import ChatActionMiddleware


TOKEN = "6085089059:AAG_OnQiU6cvdXGe9ZA8GGNSx-5JLS4q4yI"

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
async def main():
    dp = Dispatcher(storage=MemoryStorage())
    dp.message.middleware(ChatActionMiddleware())
    dp.include_router(Handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates = dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())

