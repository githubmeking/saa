import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQD59P4AgDoiwKRIyqxwzdJ-_BpOp4e6P0upnPXgGKVuoZuVmhn5RUwMpn3KJ3ajMdD2s5CJDgdM3LZJIpUYVxgefNCyLw7ZbJ_FsIRjpU5jqRPYW09lGfE-sxT3j8SMXXqlGcLZHC4oVmnjwNXe8oZYQHBOYmo88RuTKEMoYHDiZgYQscL-Y8G00zzzjK8nw9q0U26rzaDpjo7qgd5i-zerYyFJ4BgCgOPjTzGSnXFKNE_ybYsbuC_Q1JLo7myY0Y-WnNFRpqUuC5h4WKDm44r9GCU7qfiPZwhvW0bquw4nk8yxkQzNkI21L6XJx-w6PtMCoaK1c-rTI2UidiM1k_1Sg3U7vgAAAAEqb5LmAA")
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
