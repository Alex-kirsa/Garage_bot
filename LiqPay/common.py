from datetime import datetime, timedelta

from LiqPay.liqpay import LiqPay
from config.conf import PRIVATE_KEY, PUBLIC_KEY

liqpay = LiqPay(PUBLIC_KEY, PRIVATE_KEY)


def generate_link(**data):
    params = {
        "action": "pay",
        "amount": "125",
        "currency": "UAH",
        "description": "",
        "order_id": "123",
        "version": "3"
    }
    params.update(data)

    current_date = datetime.now() + timedelta(days=30)
    original_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    params.update({'expired_date': original_date})
    data = liqpay.cnb_data(params)
    signature = liqpay.str_to_sign(PRIVATE_KEY + data + PRIVATE_KEY)

    url = f"https://www.liqpay.ua/api/3/checkout?data={data}&signature={signature}"
    return url


def check_status(order_id):
    params = {
        'action': 'status',
        'version': '3',
        'order_id': f'{order_id}'
    }

    response = liqpay.api("request", params)
    return response

