import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", None)
BOT_TOKEN = getenv("BOT_TOKEN", "6091203582:AAEhAgvRn7kv4tfFMxhECVS461e1JQfJAwA")
BOT_NAME = getenv("BOT_NAME", "StetchFy")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/6790864f5fe27471bdc8d.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/e9a4d6655e5ddf51f9160.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/91034f175d41040d45b38.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/c8a0e9c544c5ea689caf9.jpg")
API_ID = int(getenv("API_ID", "14837825"))
API_HASH = getenv("API_HASH", "0ed849f5e7ab2df61d969317de2ca64c")
BOT_USERNAME = getenv("BOT_USERNAME", "stetchmubot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", None)
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TXNX5")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "its_stetch")
OWNER_NAME = getenv("OWNER_NAME", "STETCH") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("OWNER_ID", "1404114574")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001849104618")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")
