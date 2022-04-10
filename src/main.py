import discord
from discord.ext import commands
from modules.utils import get_token, get_prefix
import os
import logging
from modules.bot import NewHelpName

intents = discord.Intents().all()
activity = discord.Activity(type=discord.ActivityType.watching, name=" o Lar dos Cornos :D")
bot = commands.Bot(command_prefix=get_prefix(), intents=intents, help_command=NewHelpName(no_category = 'Sem categoria'), activity=activity, status=discord.Status.idle)

for filename in os.listdir('./src/entertaiment'):
    if filename.endswith('.py'):
        print(f'Carregando entertaiment {filename}')
        bot.load_extension(f'entertaiment.{filename[:-3]}')
for filename in os.listdir('./src/events'):
    if filename.endswith('.py'):
        print(f'Carregando event {filename}')
        bot.load_extension(f'events.{filename[:-3]}')
for filename in os.listdir('./src/cogs'):
    if filename.endswith('.py'):
        print(f'Carregando cogs {filename}')
        bot.load_extension(f'cogs.{filename[:-3]}')
        
bot.run(get_token()) 