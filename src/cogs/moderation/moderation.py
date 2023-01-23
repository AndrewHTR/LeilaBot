import discord, aiohttp, random, datetime
from discord import app_commands
from discord.ext import commands
from modules.utils import get_guildid

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
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command()
    async def falar(self, inter: discord.Interaction, *, args: str):
        args.join(' ')
        await inter.response.send_message().send(args)
    
    @app_commands.command()
    #@bridge.has_permissions(ban_members = True)
    async def ban(self, inter: discord.Interaction, member: discord.Member):
        try:
            if(member != inter.user):
                await inter.guild.ban(member, reason='')
                await inter.response.send_message(f'O usuario **{member.name}** foi banido por fazer assedio sexual!')

            else:
                await inter.response.send_message('Você não pode banir a si próprio bobinho UwU')
        except:
            await inter.response.send_message('Não foi possivel banir o usuario. Meu cargo pode estar abaixo ao dele.')
            
    @app_commands.command()
    # ! @bridge.has_permissions(kick_members=True)
    async def kick(self, inter: discord.Interaction, member: discord.Member):
        try:
            if(member != inter.user):
                await inter.guild.ban(member, reason='')
                await inter.response.send_message(f'O usuario **{member.name}** foi retirado do servidor por ser propiscuo')

            else:
                await inter.response.send_message('Você não pode retirar a si próprio UwU')

        except:
            await inter.response.send_message('Não foi possivel retirar o usuario. Meu cargo pode estar abaixo ao dele.')

    @app_commands.command()
    async def debug(self, inter: discord.Interaction):
        """Testes"""
        await inter.response.send_message('Me diz teu nome.')
        guess = await self.bot.wait_for('message', check=lambda message: message.author == inter.user)

        await inter.response.send_message(f"Opa {str(guess.content)}")
        await inter.response.send_message(f"Espero que você tome no seu cu {guess.content}. :hugging:")
