from discord import Webhook, slash_command
import discord
from discord.ext import commands, tasks
import aiohttp

class NotifyHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @tasks.loop(seconds=1.0)
    async def myloop(self, word):
        channel = self.bot.get_channel(959082477555679232)
        print(channel)
        await channel.send(word)


def setup(bot):
    bot.add_cog(NotifyHandler(bot))