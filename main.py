# from aiogram import Bot, Dispatcher
# from aiogram.types import Message
# from aiogram.utils import executor
# from config import TOKEN
# import random
# import asyncio

# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)
# active_games = {}

# @dp.message_handler(commands=["start"])
# async def start_command(message: Message):
#     await message.answer(
#         "Привет! Я  телеграм бот-рандомайзер. Введи диапазон чисел в формате 'минимум максимум', "
#         "например: '1 100', чтобы я загадал число. Ты попробуешь его отгадать!"
#     )

# def is_range_message(message: Message):
#     parts = message.text.split()
#     return len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit()

# @dp.message_handler(is_range_message)
# async def process_range(message: Message):
#     user_id = message.from_user.id
#     try:
#         min_val, max_val = map(int, message.text.split())
#         if min_val >= max_val:
#             raise ValueError
#         random_number = random.randint(min_val, max_val)
#         active_games[user_id] = random_number
#         await message.answer(f"Я загадал число от {min_val} до {max_val}. Попробуй угадать!")
#     except ValueError:
#         await message.answer("Отдуши и пожалуйста, введи два числа, где первое меньше второго, например: '1 100'.")

# def is_guess_message(message: Message):
#     return message.text.isdigit()

# @dp.message_handler(is_guess_message)
# async def process_guess(message: Message):
#     user_id = message.from_user.id
#     if user_id not in active_games:
#         await message.answer("Ты ещё не начал игру. Введи диапазон чисел, чтобы начать Мудила! ")
#         return

#     try:
#         guess = int(message.text)
#         correct_number = active_games[user_id]

#         if guess < correct_number:
#             await message.answer("Моё число больше!")
#         elif guess > correct_number:
#             await message.answer("Моё число меньше!")
#         else:
#             await message.answer(
#                 "Поздравляю! Ты угадал число. Можешь начать новую игру, введя диапазон чисел."
#             )
#             del active_games[user_id]
#     except ValueError:
#         await message.answer("По братски, введи число!")

# if __name__ == "__main__":
#     executor.start_polling(dp, skip_updates=True)

