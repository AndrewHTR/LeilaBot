import discord
from discord.commands import slash_command
from discord.ext import commands

from modules.utils import get_guildid



class Comandos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[int(get_guildid())])
    async def falar(self, ctx, *, arg):
        await ctx.respond(''.join(arg))

    @slash_command(guild_ids=[int(get_guildid())])
    async def perfil(self, ctx, member: discord.Member = None):
        if not member: member = ctx.author

        embed = discord.Embed(title="Perfil de Usuario",description="Descrição de Usuario:")
        embed.set_author(name= member.id,
        url = "https://github.com/AndrewHTR")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Comandos(bot))