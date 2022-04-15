import discord
from discord.ext import commands, ipc
from modules.utils import get_token, get_prefix
import os

class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ipc = ipc.Server(self, secret_key='Andrew')
    
    async def on_ready(self):
        print("Bot is ready.")
    
    async def on_ipc_ready(self):
        print("Ipc server is ready.")

    async def on_ipc_error(self, endpoint, error):
        print(endpoint, "raised", error)

intents = discord.Intents().all()

bot = MyBot(command_prefix=get_prefix(), intents=intents)

@bot.ipc.route()
async def get_guild_count(data):
    return len(bot.guilds)



@bot.command()
async def ola(ctx):
    await ctx.send("Ola!")
        
bot.ipc.start()
bot.run(get_token()) 