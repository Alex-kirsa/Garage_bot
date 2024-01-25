from aiogram import types
from aiogram.types import InlineKeyboardButton, WebAppInfo

from config.conf import dp, bot
from utils.sheets import Sheets
from db.db import DB
from utils.utils import texts, buttons

sheets = Sheets()
base = DB()


@dp.callback_query_handler(text=buttons.get('service').callback_data)
async def service(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(buttons.get('menu'))
    await bot.send_message(call.from_user.id, texts.get('service'), reply_markup=keyboard,
                           parse_mode='MarkdownV2')


@dp.callback_query_handler(text=buttons.get('balance').callback_data)
async def balance(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    receipt = base.get_user_receipts(call.from_user.id)
    if receipt:
        web_app_button = InlineKeyboardButton(text="Сплатити",
                                              web_app=WebAppInfo(url=receipt[2]))
        keyboard.add(web_app_button)
        keyboard.add(buttons.get('menu'))
        message_text = (f'Квитанція за {receipt[-1].replace("-", "/")} '
                        f'сума: {receipt[3]} грн\.')
        await bot.send_message(call.from_user.id, message_text, reply_markup=keyboard,
                               parse_mode='MarkdownV2')
    else:
        await call.answer(texts.get('empty_balance'), show_alert=True)
