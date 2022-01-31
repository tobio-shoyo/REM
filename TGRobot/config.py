# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/TGRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]



class Config(object):
    LOGGER = True
    API_ID = 7426647
    API_HASH = "6fb040192f120dabb810cc7ebbb1e857"
    TOKEN = "5275308569:AAGxW6SikyZUlTWRgeI2CQqVyeseSwi2Lfc" 
    OWNER_ID = 1007196749 
    OWNER_USERNAME = "INTERVIER_RRRR"
    SUPPORT_CHAT = "Rem_Support"  
    JOIN_LOGGER = (-1001774536726)
    EVENT_LOGS = (-1001597613556)
    SQLALCHEMY_DATABASE_URI = "sqldbtype://username:pw@hostname:port/db_name"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "Q7fkrZmh41zum0Gvy4ueINGzggcJXnN3GJ3qXKfRdKneqS_BOqUKDfKfednj1vDD"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    
    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    DONATION_LINK = None
    CERT_PATH = None
    DEL_CMDS = True  
    STRICT_GBAN = True
    WORKERS = (8)
    BAN_STICKER = "CAACAgIAAxkBAAFZJ0phbOUj_DO3OBj2TCnWV1X3SIKq_QACbgADJ--KHPzNmg619o2pIQQ"  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True 
    CASH_API_KEY = ("awoo")  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = "NCVXIXGDRFH5"  # Get your API key from https://timezonedb.com/api
    WALL_API = ("awoo")  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    ALLOW_CHATS = True
    MONGO_DB_URI = "mongodb+srv://Shoyo:shoyo123@shoyo.lwslq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    ARQ_API_KEY = "QQYGAV-QXCTIT-SZDAGG-ZQPHDF-ARQ"
    ARQ_API_URL = "https://thearq.tech"
    OPENWEATHERMAP_ID = "8c62bed60110267c2a039756f6cdddef"
    ERROR_LOGS = (-1001597613556)
    DB_URL = ""
    TEMP_DOWNLOAD_DIRECTORY = "./"
    MONGO_DB = "mongodb"
    MONGO_DB_URL = "mongodb+srv://Shoyo:shoyo123@shoyo.lwslq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    REDIS_URL = "redis://Falco:Bhanubhai123_@redis-13865.c99.us-east-1-4.ec2.cloud.redislabs.com:13865/Falco"
    REM_BG_API_KEY = "q4HcjNjJDJic8Gw6xUoAhgxq"
    BOT_ID = 2135830536
    BOT_USERNAME = "remtestiengbot"
    BOT_NAME = "Rem"
    YOUTUBE_API_KEY = "AIzaSyBnaLtVGHt2BfQLEsTyVGb2Sq-USHIDfrM"
    STRING_SESSION = "1BVtsOMQBuw-XRnaQbzbmtsRyAZ8__C4EN9EL45aTNDZTFPW9o_XsPHi0OAhy2_D0KxbII5Rue30eOCqMTr39viyDb5QDMXFzyQJdfz-q7JCCFVTIWBTgslRtnC2lXLUTxuiLGUaI2mUQgdsQFz0DSW30vIr1mwOCAxJqu5qTc2_Ihw9c8AQrisdOd_IftFs5bUl748EluA_2qaNZVBfNlDV5XDEFTgAbT6UrgUZJu0zm7s8ji1Uwn8O_S4NqCLBj2qMeRkLkmfM_1rwmvLQjbzqf7GplagaBQ8AYfsgd4SWqd7Ej__VCFCo_esXxpLquu-RpuwIf-cZYeSRVm08p6tf3o3I05z0="
    DB_URI = "postgresql://pgnkbrve:sDwcC5w5wFzIqCmmVMCtkTZw-DMzro03@castor.db.elephantsql.com/pgnkbrve"
    PORT = 5000
    



class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
