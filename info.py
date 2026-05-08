import re
from os import environ
from Script import script
from pyrogram import utils as pyroutils

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


#update here
DATABASE_URI = "mongodb+srv://AYU:AYU@cluster0.bxkuzfk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_URI2 = "mongodb+srv://AYU2:AYU2@cluster0.gi1dpjc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DATABASE_URI3 = "mongodb+srv://AYU3:AYU3@cluster0.bv3pk88.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
ADMINS = [7579162275, 7756047880]


async def load_config():
    global DATABASE_URI, DATABASE_URI2, DATABASE_URI3, ADMINS
    data = await db.config.find_one({"_id": "CONFIG"}) or {}
    DATABASE_URI = data.get("DATABASE1") #Dont touch here
    DATABASE_URI2 = data.get("DATABASE2") #Dont touch here
    DATABASE_URI3 = data.get("DATABASE3") #Dont touch here

    ADMINS = data.get("ADMINS", [])
    
# Bot information
SESSION = environ.get('SESSION', 'autodelete')
API_ID = int(environ.get("API_ID", "26826540"))
API_HASH = environ.get("API_HASH", "32d454f51fc7b3b3c7d51c4f80f628b5")
BOT_TOKEN = environ.get("BOT_TOKEN", "7555371731:AAEUhAnDh2EU1qG1i4p3o-qkrG9A")
BOT_IS_PUBLIC = bool(environ.get('BOT_IS_PUBLIC', True))
# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://i.ibb.co/5Xxppj9N/c9107a63bb49.jpg https://i.ibb.co/mC2HZTqw/8ae320b5fd94.jpg https://i.ibb.co/5hm9C6xv/abe61c1c4ed2.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7579162275 7756047880').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002287749434').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

SET_SYDSEC = 30 #Seconds till which auto edit will be done
FSUB = True 
REQ_CHANNEL1=environ.get("REQ_CHANNEL1")
REQ_CHANNEL1 = (int(REQ_CHANNEL1) if REQ_CHANNEL1 and id_pattern.search(REQ_CHANNEL1) else False) if REQ_CHANNEL1 is not None else None
REQ_CHANNEL2=environ.get("REQ_CHANNEL2")
REQ_CHANNEL2 = (int(REQ_CHANNEL2) if REQ_CHANNEL2 and id_pattern.search(REQ_CHANNEL2) else False) if REQ_CHANNEL2 is not None else None

# MongoDB information
DATABASE_NAME = environ.get('DATABASE_NAME', "CGM_Files")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'CGM_Files')

#Auto approve
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '-1002303772763').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour request has been approved")
APPROVED = environ.get("APPROVED_WELCOME", "off").lower()

#peer id fix 
pyroutils.MIN_CHAT_ID = -999999999999
pyroutils.MIN_CHANNEL_ID = -100999999999999

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', "-1002530405053"))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1002448950000').split()]
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Cyber_Fcracker')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CUSTOM_FILE_CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌‌‌‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
