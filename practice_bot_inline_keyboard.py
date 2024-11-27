from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardButton
from aiogram.types import CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from aiogram import Dispatcher, Bot, F
from aiogram.types import Message


import asyncio

# import asyncio

bot = Bot('7061646789')
dp = Dispatcher()

class UserState(StatesGroup):
    groth = State()
    gender = State()
    age = State()
    weight = State()

test_keyboard = ReplyKeyboardMarkup(keyboard=[[ReplyKeyboardButton(text='Расчитать')]])

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет я бот помогающий твоему здоровью',reply_markup=test_keyboard)

@dp.callback_query(F.text == 'Расчитать')
async def set_age(call: CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(call.id)
    await state.set_state(UserState.age)
    await call.message.answer('Введите свой возраст:')

@dp.message(UserState.age)
async def set_groth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(UserState.groth)
    await message.answer('Введите свой рост в см:')

@dp.message(UserState.groth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(groth=message.text)
    await state.set_state(UserState.weight)
    await message.answer('Введите свой вес в кг:')

@dp.message(UserState.weight)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    await state.set_state(UserState.gender)
    await message.answer('Введите свой пол:')

@dp.message(UserState.gender)
async def calculate(message: Message, state: FSMContext):
    await state.update_data(gender=message.text)
    data = await state.get_data()
    user_gender = data['gender']
    user_age = int(data['age'])
    user_groth = int(data['groth'])
    user_weight = int(data['weight'])
    if user_age < 13 or user_age > 80:
        await message.answer('Данный калькулятор не подходит под ваш возраст')
        return
    print(user_age, user_groth, user_weight, user_gender)
    
    if user_gender.lower() == 'женский':
        calc_callories = 10 * user_weight + 6.25 * user_groth - 5 * user_age - 161
        await message.answer(f'Ваша норма каллорий: {calc_callories}')
    elif user_gender.lower() == 'мужской':
        calc_callories = 10 * user_weight + 6.25 * user_groth - 5 * user_age + 5
        await message.answer(f'Ваша норма каллорий: {calc_callories}', reply_markup=test_keyboard)
async def main():
   await dp.start_polling(bot)

@dp.callback_query(F.data == 'formula')
async def formula(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await call.message.answer('Для женщин: \n(10 х вес в кг) + (6,25 х рост в см) – (5 х возраст в г) – 161\n'
                              'Для мужчин: \n(10 х вес в кг) + (6,25 х рост в см) – (5 х возраст в г) + 5')

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot deactivated')
