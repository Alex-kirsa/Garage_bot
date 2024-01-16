from aiogram import types

text = {
    'send_phone': 'Для продолжения, подтвердите номер телефона',

}

buttons = {
    'send_phone': types.KeyboardButton(text="Отправить номер телефона", request_contact=True),
    'number_security': types.InlineKeyboardButton(text='Телефон охрани', callback_data='button1'),
    'help_center': types.InlineKeyboardButton(text='Cлужба поддержки', callback_data='button1')
}