import discord
from discord.ext import commands



class Coisas(commands.Cog):
    @commands.command()
    async def falar(self, ctx, *, arg):
        await ctx.message.delete()
        await ctx.send(''.join(arg))

    @commands.command()
    async def ajuda(self, ctx,pessoa):
        await discord.send_friend_request(pessoa)

def setup(bot):
    bot.add_cog(Coisas(bot))