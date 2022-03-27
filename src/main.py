import discord
from discord import file
from discord.ext import commands
from modules.utils import get_token
import os

intents = discord.Intents().all()

bot = commands.Bot(command_prefix="!", intents=intents)

for filename in os.listdir('./src/entertaiment'):
    if filename.endswith('.py'):
        print(f'Loading entertaiment {filename}')
        bot.load_extension(f'ent.{filename[:-3]}')
for filename in os.listdir('./src/events'):
    if filename.endswith('.py'):
        print(f'Loading event {filename}')
        bot.load_extension(f'events.{filename[:-3]}')
for filename in os.listdir('./src/cogs'):
    if filename.endswith('.py'):
        print(f'Loading cogs {filename}')
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(get_token()) 

