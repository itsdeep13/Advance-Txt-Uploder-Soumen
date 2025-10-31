#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22484497"))
API_HASH = environ.get("API_HASH", "c38cb053916c47a97590c244663cbaef")
BOT_TOKEN = environ.get("BOT_TOKEN", "8301299052:AAH0aBTXW89q7ALQSsY4z-Sq5Pd-GscEgqM")

OWNER = int(environ.get("OWNER", "6252997817"))
CREDIT = environ.get("CREDIT", "ADVANCE UPLOAD BOT BY SOUMEN")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '6252997817').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '6252997817').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
    # .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,
api_url = "http://master-api-v3.vercel.app/"
api_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzkxOTMzNDE5NSIsInRnX3VzZXJuYW1lIjoi4p61IFtvZmZsaW5lXSIsImlhdCI6MTczODY5MjA3N30.SXzZ1MZcvMp5sGESj0hBKSghhxJ3k1GTWoBUbivUe1I"
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.







