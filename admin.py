from datetime import datetime

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from config.conf import dp, bot
from utils.sheets import Sheets
from db.db import DB
from utils.utils import texts
from LiqPay.common import generate_link

sheets = Sheets()
base = DB()


@dp.callback_query_handler(text='mailing')
async def admin(call: types.CallbackQuery):
    date = datetime.now().date().strftime('%m-%Y')
    sheets_datas = sheets.read_sheet()
    await call.answer(texts.get('mailing'))
    for sheets_user in sheets_datas:
        try:
            user = base.get_user([sheets_user[2].replace('+', "").replace(" ", ''), sheets_user[3].replace('@', "")])
            if len(sheets_user) == 7 and user:
                order_id = f'{user[1]}-{date}'
                link = generate_link(amount=sheets_user[5], description=sheets_user[0], order_id=order_id)
                keyboard = InlineKeyboardMarkup()
                web_app_button = InlineKeyboardButton(text="Открыть веб-приложение",
                                                      web_app=WebAppInfo(url=link))
                keyboard.add(web_app_button)
                with open(f'media/{date}/{sheets_user[0]}.pdf', 'rb') as file:
                    await bot.send_document(user[1], file,
                                            caption=f'{sheets_user[6]}\n[Оплатити за посиланням]({link})',
                                            parse_mode='MarkdownV2', reply_markup=keyboard)
                sheets_user[4] = "Отправлено"
                sheets_user[2] = user[5]
                sheets_user[3] = user[4]
                receipt_data = [user[1], 'Open', link, sheets_user[5], sheets_user[0], order_id]
                base.add_receipts(receipt_data)
            else:
                raise IndexError
        except IndexError:
            sheets_user[4] = "Ошибка отправления"
        except FileNotFoundError:
            sheets_user[4] = "Нет нужного файла"
    sheets.rewrite_sheet(sheets_datas)
    await bot.send_message(call.from_user.id, texts.get('finish_mailing'))

