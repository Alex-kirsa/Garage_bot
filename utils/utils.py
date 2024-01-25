from aiogram import types

texts = {
    'send_phone': 'Для продовження, відправте номер телефону',
    'welcome': 'Вітаю в ГБК Східний, бот',
    'mailing': 'Запустил розсилку, по закінченню напишу',
    'finish_mailing': 'Розсилка заверена, дані оновленно в таблиці',
    'service': ('*Керівник/Бухгалтер*: `+380 67 280 0770`\n\n'
                '*Регулювання воріт Олександр*: `+380 67 772 5544`\n\n'
                '*Електрик Сергій*: `+380 96 737 7698`\n\n'
                '*Охорона гбк*: `+380 98 800 4419`'),
    'empty_balance': 'Всі квитанції оплачені'

}

buttons = {
    'send_phone': types.KeyboardButton(text="Відправити номер телефону", request_contact=True),
    'balance': types.InlineKeyboardButton(text='Баланс💳', callback_data='balance'),
    'mailing': types.InlineKeyboardButton(text='Розсилка', callback_data='mailing'),
    'service': types.InlineKeyboardButton(text='Сервіс🧰', callback_data='service'),
    'menu': types.InlineKeyboardButton(text='Головна сторінка🏠', callback_data='menu')
}
