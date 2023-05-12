import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BABeoPb8_V9H6tvmz3bdDuWQJ_eHVWjOL1Fnpiaioua8xW4kVgt4GW3f4IP8wLtPgyrZMXhHZRpCg8dKb8daR5U2o9iKX_olDr4Jj9K29LhUdr7WXu-WyNEQAv95TQj_V89NULLqcgzOe43TE-65-MuQrWV4VZD_9u7n_G_rNjwFjE1RSQeQhkssAYc3hTIoF5tkwehRPzPfnXpu1DxkMjtrzVQ7nbhzOgKzkCSO9GXLRSLDA2l1gURoU1TPjV2qyAkiFdLWOO-xcb7Tp--Ae_S6a8-oURC1VgfeJ6EathAUYS_SjZqdcty3laSAyOM7jTP0lf42ekvcTDaJAYF6Y42mAAAAAW3f2RcA")
BOT_TOKEN = getenv("BOT_TOKEN", "6208176104:AAFfhRHFpIvb0h_Jc8Mum-yz-ZH0RgMFPJU")
BOT_NAME = getenv("BOT_NAME", "StetchFy")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/6790864f5fe27471bdc8d.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/e9a4d6655e5ddf51f9160.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/91034f175d41040d45b38.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/c8a0e9c544c5ea689caf9.jpg")
API_ID = int(getenv("API_ID", "14837825"))
API_HASH = getenv("API_HASH", "0ed849f5e7ab2df61d969317de2ca64c")
BOT_USERNAME = getenv("BOT_USERNAME", "stetchfybot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", None)
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TXNX5")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "its_stetch")
OWNER_NAME = getenv("OWNER_NAME", "STETCH") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("OWNER_ID", "1404114574")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://joepsychoo:<password>@cluster0.q0ox4m3.mongodb.net/?retryWrites=true&w=majority") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "its_stetch")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")
