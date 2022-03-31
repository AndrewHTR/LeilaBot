from discord import Webhook, slash_command
import discord
from discord.ext import commands 
import aiohttp

class NotifyHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(NotifyHandler(bot))