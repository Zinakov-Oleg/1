import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message

TOKEN = 

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def start_handler(message: Message):
    await message.answer('Привет, я бот, который подскажет расписание 120-ой школы! Создатель @olezhekop')

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Помощь", callback_data="help")],
        [InlineKeyboardButton(text="О боте", callback_data="about")]
    ]
)

@dp.message(Command("menu"))
async def show_inline_menu(message: Message):
    await message.answer("Выберите:", reply_markup=inline_kb)

@dp.callback_query()
async def handle_callback(callback_query):
    if callback_query.data == "help":
        await callback_query.message.answer("Вот список команд: /start /help")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
