import asyncio

from aiogram import types
from aiogram.utils import executor
from datetime import datetime
import admin
import user
from LiqPay.checker import checker
from config.conf import dp, bot, ADMIN
from db.db import DB
from utils.utils import texts
from utils.utils import buttons

base = DB()


async def welcome(msg: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(buttons.get('balance'), buttons.get('service'))
    if msg.from_user.id == int(ADMIN):
        keyboard.add(buttons.get('mailing'))
    await bot.send_message(msg.from_user.id, texts.get('welcome'), reply_markup=keyboard)


@dp.message_handler(commands=["start"])
async def check_membership(msg: types.Message):
    if base.check_user(msg.from_user.id):
        await welcome(msg)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(buttons.get('send_phone'))
        await msg.answer(texts.get('send_phone'), reply_markup=keyboard)


@dp.callback_query_handler(text=buttons.get('menu').callback_data)
async def service(call: types.CallbackQuery):
    await welcome(call)


@dp.message_handler(content_types=['contact'])
async def contact_handler(msg: types.Message):
    if msg.contact is not None:
        phone_number = msg.contact.phone_number.replace('+', '')
        base.add_user([msg.from_user.id, True, msg.from_user.full_name, msg.from_user.username, phone_number])
        await welcome(msg)


@dp.message_handler(content_types=['document'])
async def handle_docs(msg: types.Message):
    if msg.from_user.id == int(ADMIN):
        document = msg.document
        document_id = document.file_id
        file_info = await bot.get_file(document_id)

        file_path = file_info.file_path
        date = datetime.now().date().strftime('%m-%Y')
        await bot.download_file(file_path, destination=f'media/{date}/{document.file_name}'.encode('utf-8'))


if __name__ == "__main__":
    base.init_table()
    loop = asyncio.get_event_loop()
    loop.create_task(checker())
    executor.start_polling(dp, skip_updates=True)
