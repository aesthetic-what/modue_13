from aiogram.types import Message

from aiogram import Dispatcher, Bot
from aiogram.utils import executor

# import asyncio

bot = Bot('token')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_message(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')
    print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)