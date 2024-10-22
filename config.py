import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQDNvmIAZEOhE36eqs5X2MCzdiFC8Bz2eP1PRXQVvIex63cJmWjQBTyMgD1zLQ1iG6NodFwCdpfMeLNa5uWJpLzYU5jV6uQoCVxAKDMO-45mJdUQhLC1YJLxnZvkm5bMIJna7TTzThU_anybVymqBu3MnXLsNzEMi9YwjsnhjyMpy9Sr-qb6voFEoKRqaQHwFG-axYHNj0TaHAzXMBfxXNDHHsFG1TunQlT8MeHmjsk1z5fZyuScTYTaN5w736c0XKbpUynRKoKkPJQM4NmFtdES4HSVwhvm3HsgTolCm1Nk-1nEd7jHp__yyms_CDQr21MnuhSbp77ZhP-KNL82_Mf2cDFZJwAAAAEqb5LmAA")
BOT_TOKEN = getenv("BOT_TOKEN","8197433189:AAEBLi_ma4UXrrSzBhchJyM_ccPJAFhGBIQ")
BOT_NAME = getenv("BOT_NAME", "Talia Müzik Projesi")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cd0b87484429704c7b935.png")
THUMB_IMG = getenv("THUMB_IMG", "https://i.ibb.co/VQd4HSH/Photo-1629477903701.jpg")
AUD_IMG = getenv("AUD_IMG", "https://i.ibb.co/VQd4HSH/Photo-1629477903701.jpg")
QUE_IMG = getenv("QUE_IMG", "https://i.ibb.co/VQd4HSH/Photo-1629477903701.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "@Denek99bot ")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Onedio Asistan1")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Sohbetdestek")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "EfsaneMusicProject")
OWNER_NAME = getenv("OWNER_NAME", "@hurkole") # kullanıcı adınızı semboller olmadan doldurma @
DEV_NAME = getenv("DEV_NAME", "hurkole")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "250"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
