import discord
from discord.commands import slash_command
from discord.ext import commands
import random
import datetime
from modules.utils import get_guildid



class Comandos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[int(get_guildid())], help="Faz com que o bot mande mensagem")
    async def falar(self, ctx, *, arg):
        await ctx.respond(''.join(arg))
        

    @slash_command(guild_ids=[int(get_guildid())], help="Mostra informações do usuário" )
    async def perfil(self, ctx, member: discord.Member):    
        time = datetime.datetime.now() 
        avatar = member.avatar
        embed = discord.Embed(color = random.randint(0, 0xffffff),title=f"Perfil do Usuário {member.name}")
        embed.set_thumbnail(url = avatar)
        embed.set_author(name=f"Bot criado por: Andrew Kauã",
        url = "https://github.com/AndrewHTR",
        icon_url="https://cdn.discordapp.com/avatars/500456611073228821/481f96ffc73c973188e9595317256e94.png")

        embed.add_field(name="__**Informações da conta:**__\n", value=f"""**Nome no Discord:** {member.name}\n**Status:** {member.activity}\n**Está atualmente:** {member.status}\n**Conta criada: **{member.created_at.__format__("%d/%m/%Y as %H:%M")}""")
        embed.add_field(name="__**Informações do perfil no servidor:**__", value=f"""**Nick:** {member.nick}\n**Entrou no servidor:** {member.joined_at.__format__("%d/%m/%Y as %H:%M")}\n**Cargos:** {''.join([r.mention for r in member.roles[1:]])}""", inline=False)
        embed.set_footer(text=f"Horário: {time.strftime('%H:%M:%S')}", icon_url="https://cdn.discordapp.com/avatars/689012066266382351/c16512460537ad5174c5c16a319e1258.png")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Comandos(bot))