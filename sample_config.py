from os import environ

from dotenv import load_dotenv

load_dotenv("config.env")

HEROKU = bool(
    environ.get("DYNO")
)  # NOTE Make it false if you're not deploying on heroku or docker.

if HEROKU:

    BOT_TOKEN = environ.get("BOT_TOKEN", None)
    API_ID = int(environ.get("API_ID", 6))
    API_HASH = environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    SESSION_STRING = environ.get("SESSION_STRING", None)
    USERBOT_PREFIX = environ.get("USERBOT_PREFIX", ".")
    SUDO_USERS_ID = [int(x) for x in environ.get("SUDO_USERS_ID", "").split()]
    LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", None))
    GROUP_SUPPORT = environ.get("GROUP_SUPPORT", ULTRON_X_SUPPORT)
    UPDATES_CHANNEL = int(environ.get("UPDATES_CHANNEL", ULTRON_X_UPDTAES))
    GBAN_LOG_GROUP_ID = int(environ.get("GBAN_LOG_GROUP_ID", None))
    MESSAGE_DUMP_CHAT = int(environ.get("MESSAGE_DUMP_CHAT", None))
    WELCOME_DELAY_KICK_SEC = int(environ.get("WELCOME_DELAY_KICK_SEC", None))
    MONGO_URL = environ.get("MONGO_URL", None)
    ARQ_API_URL = environ.get("ARQ_API_URL", None)
    ARQ_API_KEY = environ.get("ARQ_API_KEY", None)
    LOG_MENTIONS = bool(int(environ.get("LOG_MENTIONS", None)))
    RSS_DELAY = int(environ.get("RSS_DELAY", None))
    PM_PERMIT = bool(int(environ.get("PM_PERMIT", None)))
    ASSISTANT_NAME = environ.get("ASSISTANT_NAME", ᴜʟᴛʀᴏɴ)
    BOT_USERNAME = environ.get("BOT_USERNAME", @ULTRON_X_ROBOT)
    IMG_1 = environ.get("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
    IMG_2 = environ.get("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
    IMG_3 = environ.get("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
    IMG_4 = environ.get("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
    IMG_5 = environ.get("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png")
else:
    BOT_TOKEN = "467677575:YZfaakjwd545dfg-N6JStihhuw5gQeZHntc"
    API_ID = 123456
    API_HASH = "dfxcgs5s12hdcxfgdfz"
    USERBOT_PREFIX = "."
    PHONE_NUMBER = "+916969696969"  # Need for Userbot
    SUDO_USERS_ID = [
        4543744343,
        543214651351,
    ]  # Sudo users have full access to everything, don't trust anyone
    LOG_GROUP_ID = -100125431255
    GBAN_LOG_GROUP_ID = -100125431255
    MESSAGE_DUMP_CHAT = -1001181696437
    WELCOME_DELAY_KICK_SEC = 300
    MONGO_URL = "mongodb+srv://username:password@cluster0.ksiis.mongodb.net/YourDataBaseName?retryWrites=true&w=majority"
    ARQ_API_KEY = "Get this from @ARQRobot"
    ARQ_API_URL = "https://arq.hamker.in"
    LOG_MENTIONS = True
    RSS_DELAY = 300  # In seconds
    PM_PERMIT = True
