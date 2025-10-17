import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Я буду напоминать тебе о паузах 🕐")

async def reminder():
    while True:
        await bot.send_message(chat_id=int(CHAT_ID), text="⏰ Пора сделать паузу, размяться и подышать 🌿")
        await asyncio.sleep(3600)  # 3600 секунд = 1 час (для теста можно 10)

async def main():
    asyncio.create_task(reminder())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
