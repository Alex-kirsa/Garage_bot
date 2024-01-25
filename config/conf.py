import os
from dotenv import load_dotenv
from aiogram import Bot
from aiogram.dispatcher import Dispatcher

DEBUG = False

load_dotenv()

TOKEN = os.getenv("TEST_TOKEN") if DEBUG else os.getenv("WORK_TOKEN")
ADMIN = os.getenv('ADMIN')
sheet_id = os.getenv('SHEETS_ID')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
PUBLIC_KEY = os.getenv('PUBLIC_KEY')
bot = Bot(token=TOKEN, disable_web_page_preview=True)
dp = Dispatcher(bot)
