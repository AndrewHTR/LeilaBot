import discord, aiohttp, random, datetime
from discord.commands import command
from discord.commands.core import slash_command, user_command
from discord.ext import commands
from modules.utils import get_guildid
from urllib.request import urlopen

role_ids = [...]

class AddButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label = "nomes fodas",
            style = discord.enums.ButtonStyle.primary,
        )

class Moderation(commands.Cog):
    """
    COMANDOS PARA MODERAÇÃO DO SERVIDOR
    """
    def __init__(self, bot):
        self.bot = bot

    #@slash_command(guild_ids=[int(get_guildid())], description = "Faz com que o bot mande mensagem")
    @commands.command(aliases=['banir'])
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx:commands.Context, member: discord.Member):
        try:
            if(member != ctx.author):
                await ctx.guild.ban(member, reason='')
                await ctx.send(f'O usuario **{member.name}** foi banido por fazer assedio sexual!')

            else:
                await ctx.send('Você não pode banir a si próprio bobinho UwU')
        except:
            await ctx.send('Não foi possivel banir o usuario.')
        
    @commands.command(aliases=['chutar'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx:commands.Context, member: discord.Member):
        try:
            if(member != ctx.author):
                await ctx.guild.ban(member, reason='')
                await ctx.send(f'O usuario **{member.name}** foi retirado do servidor por ser propiscuo')
            else:
                await ctx.send('Você não pode retirar a si próprio UwU')
        except:
            await ctx.send('Não foi possivel retirar o usuario.')

    #@slash_command(guild_ids=[int(get_guildid())])
    @commands.command()
    async def debug(self, ctx):
        """Teste com botões"""

        # timeout is None because we want this view to be persistent.
        view = discord.ui.View(timeout=None)

        # Loop through the list of roles and add a new button to the view for each role.
        for role_id in role_ids:
            # Get the role from the guild by ID.
            role = ctx.guild.get_role(role_id)
            view.add_item(AddButton())
        embed = discord.Embed(title='Testezada')
        await ctx.send(embed=embed, view=view)
        
def setup(bot):
    bot.add_cog(Moderation(bot))