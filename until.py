from aiogram import types

text = {
    'send_phone': 'Для продолжения, подтвердите номер телефона',
    'welcome': 'Приветствую в боте',
    'mailing': 'Запустил рассылку, по окончанию напишу',
    'finish_mailing': 'Рассылка завершенна, данные обновленны в таблице'

}

buttons = {
    'send_phone': types.KeyboardButton(text="Отправить номер телефона", request_contact=True),
    'number_security': types.InlineKeyboardButton(text='Телефон охраны', callback_data='number_security'),
    'help_center': types.InlineKeyboardButton(text='Cлужба поддержки', callback_data='help_center'),
    'mailing': types.InlineKeyboardButton(text='Pассылка', callback_data='mailing'),
}