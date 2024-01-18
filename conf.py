import os
from dotenv import load_dotenv
from aiogram import Bot
from aiogram.dispatcher import Dispatcher

DEBUG = True

load_dotenv()

TOKEN = os.getenv("TEST_TOKEN") if DEBUG else os.getenv("WORK_TOKEN")
ADMIN = os.getenv('ADMIN')
sheet_id = os.getenv('SHEETS_ID')
bot = Bot(token=TOKEN, disable_web_page_preview=True)
dp = Dispatcher(bot)
