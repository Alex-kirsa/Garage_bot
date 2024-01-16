from aiogram import types
from aiogram.utils import executor

from conf import dp
from db import DB
from until import text
from until import buttons
base = DB()


@dp.message_handler(commands=["start"])
async def check_membership(msg: types.Message):
    if base.check_user(msg.from_user.id):
        await msg.answer('hey')
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(buttons.get('send_phone'))
        await msg.answer(text.get('send_phone'))


@dp.message_handler(content_types=['contact'])
async def contact_handler(message: types.Message):
    if message.contact is not None:
        phone_number = message.contact.phone_number
        await message.reply(f"Спасибо, ваш номер: {phone_number}")


if __name__ == "__main__":
    base.init_table()
    executor.start_polling(dp, skip_updates=True)
