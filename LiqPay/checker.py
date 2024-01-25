import asyncio

from LiqPay.common import check_status
from db.db import DB
from utils.sheets import Sheets

base = DB()
sheets = Sheets()


async def checker():
    while True:
        receipts = base.get_receipts()
        for receipt in receipts:
            order_id = receipt[5]
            if check_status(order_id)['status'] in ['success', 'failure']:
                base.update_receipts(order_id, check_status(order_id)['status'])
                sheets.write_receipt([[receipt[4], 'Оплаченно', receipt[-1]]])
        await asyncio.sleep(3600)
