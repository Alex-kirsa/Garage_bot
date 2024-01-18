from datetime import datetime

from aiogram import types

from conf import dp, bot
from sheets import Sheets
from db import DB
from until import text

sheets = Sheets()
base = DB()


@dp.callback_query_handler(text='mailing')
async def admin(call: types.CallbackQuery):
    date = datetime.now().date().strftime('%m-%Y')
    sheets_datas = sheets.read_sheet()
    await call.answer(text.get('mailing'))
    for sheets_user in sheets_datas:
        try:
            user = base.get_user([sheets_user[2].replace('+', "").replace(" ", ''), sheets_user[3].replace('@', "")])
            if len(sheets_user) == 6 and user:
                with open(f'media/{date}/{sheets_user[0]}.pdf', 'rb') as file:
                    await bot.send_document(user[1], file, caption=sheets_user[5])
                sheets_user[4] = "Отправлено"
                sheets_user[2] = user[5]
                sheets_user[3] = user[4]
            else:
                raise IndexError
        except IndexError:
            sheets_user[4] = "Ошибка отправления"
        except FileNotFoundError:
            sheets_user[4] = "Нет нужного файла"
    sheets.rewrite_sheet(sheets_datas)
    await bot.send_message(call.from_user.id, text.get('finish_mailing'))

