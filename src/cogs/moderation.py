import discord, aiohttp, random, datetime
from discord.commands import command
from discord.commands.core import slash_command, user_command
from discord.ext import commands, bridge
from discord.ext.bridge import BridgeContext, BridgeExtContext, BridgeApplicationContext
from modules.utils import get_guildid
from googlesearch import search

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

    @bridge.bridge_command()
    async def falar(self, ctx: BridgeContext, *, args: str):
        args.join(' ')
        if isinstance(ctx, BridgeExtContext):
            await ctx.send(args)
        else:
            await ctx.respond(args)

    #@slash_command(guild_ids=[int(get_guildid())], description = "Faz com que o bot mande mensagem")
    @bridge.bridge_command(aliases=['banir'])
    #@bridge.has_permissions(ban_members = True)
    async def ban(self, ctx: BridgeContext, member: discord.Member):
        try:
            if(member != ctx.author):
                await ctx.guild.ban(member, reason='')
                await ctx.send(f'O usuario **{member.name}** foi banido por fazer assedio sexual!')

            else:
                if isinstance(ctx, BridgeApplicationContext):
                    await ctx.respond('Você não pode banir a si próprio bobinho UwU')
                elif isinstance(ctx, BridgeExtContext):
                    await ctx.send('Você não pode banir a si próprio bobinho UwU')
        except:
            if isinstance(ctx, BridgeApplicationContext):
                await ctx.respond('Não foi possivel banir o usuario. Meu cargo pode estar abaixo ao dele.')
            elif isinstance(ctx, BridgeExtContext):
                await ctx.send('Não foi possivel banir o usuario. Meu cargo pode estar abaixo ao dele.')
        
    @bridge.bridge_command(aliases=['chutar'])
    # ! @bridge.has_permissions(kick_members=True)
    async def kick(self, ctx: BridgeContext, member: discord.Member):
        try:
            if(member != ctx.author):
                await ctx.guild.ban(member, reason='')

                if isinstance(ctx, BridgeApplicationContext):
                    await ctx.respond(f'O usuario **{member.name}** foi retirado do servidor por ser propiscuo')
                elif isinstance(ctx, BridgeExtContext):
                    await ctx.send(f'O usuario **{member.name}** foi retirado do servidor por ser propiscuo')
            else:
                if isinstance(ctx, BridgeApplicationContext):
                    await ctx.respond('Você não pode retirar a si próprio UwU')
                elif isinstance(ctx, BridgeExtContext):
                    await ctx.send('Você não pode retirar a si próprio UwU')
        except:
            if isinstance(ctx, BridgeApplicationContext):
                await ctx.respond('Não foi possivel retirar o usuario. Meu cargo pode estar abaixo ao dele.')
            elif isinstance(ctx, BridgeExtContext):
                await ctx.send('Não foi possivel retirar o usuario. Meu cargo pode estar abaixo ao dele.')

    #@slash_command(guild_ids=[int(get_guildid())])
    @commands.command()
    async def debug(self, ctx):
        """Testes"""
        await ctx.respond('Me diz teu nome.')
        guess = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)

        await ctx.send(f"Opa {str(guess.content)}")
        await ctx.send(f"Espero que você tome no seu cu {guess.content}. :hugging:")

    @commands.command()
    async def search(self, ctx: commands.Context, *, pesquisa):
        for resultado in search(pesquisa, tld='co.in', num=3, stop=3, pause=2):
            await ctx.send(resultado)

def setup(bot):
    bot.add_cog(Moderation(bot))