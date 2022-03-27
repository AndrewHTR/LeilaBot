import discord
from discord.ext import commands

class NotifyHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, ctx):
        print("a")



def setup(bot):
    bot.add_cog(NotifyHandler(bot))