import discord
from discord.commands.core import slash_command
from discord.ext import commands
import random
import datetime
from modules.utils import get_guildid

class AddButton(discord.ui.Button):
    def __init__(self, texto, url):
        super().__init__(
            label = texto,
            style = discord.enums.ButtonStyle.primary,
            url = url
        )


class Social(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_command(guild_ids=[int(get_guildid())], description = "Mostra informações do usuário" )
    #@commands.command()
    async def perfil(self, ctx, member: discord.Member):
        """Mostra informações do usuario """    
        #region embeds
        time = datetime.datetime.now() 
        avatar = member.avatar
        embed = discord.Embed(color = random.randint(0, 0xffffff),title=f"Perfil do Usuário {member.name}")
        embed.set_thumbnail(url = avatar)
        embed.set_author(name=f"Bot criado por: Andrew Kauã",
        url = "https://github.com/AndrewHTR",
        icon_url="https://media.discordapp.net/attachments/673668744471379971/960000584948269076/IMG_20220402_231811.jpg")

        embed.add_field(name="__**Informações da conta:**__\n", value=f"""**Nome no Discord:** {member.name}\n**Status:** {member.activity}\n**Está atualmente:** {member.status}\n**Conta criada: **{member.created_at.__format__("%d/%m/%Y as %H:%M")}""")
        embed.add_field(name="__**Informações do perfil no servidor:**__", value=f"""**Nick:** {member.nick}\n**Entrou no servidor:** {member.joined_at.__format__("%d/%m/%Y as %H:%M")}\n**Cargos:** {''.join([r.mention for r in member.roles[1:]])}""", inline=False)
        embed.set_footer(text=f"Horário: {time.strftime('%H:%M:%S')}", icon_url="https://media.discordapp.net/attachments/661371734531768363/961359898233430016/unknown.png")
        #endregion       
        
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Social(bot))