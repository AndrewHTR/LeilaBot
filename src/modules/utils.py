from dotenv import load_dotenv
import os
from discord.ext import commands, tasks

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

def get_prefix():
    prefix = os.getenv("prefix")
    if prefix == None:
        return os.environ["prefix"]
    return prefix