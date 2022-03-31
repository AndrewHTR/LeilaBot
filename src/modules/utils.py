from dotenv import load_dotenv
import os

load_dotenv()

def get_guildid():
    guild = os.getenv("guild_id")
    if guild == None:
        return os.environ["guild_id"]
    return guild

def get_token():
    token = os.getenv("token")
    if token == None:
        return os.environ["token"]
    return token
