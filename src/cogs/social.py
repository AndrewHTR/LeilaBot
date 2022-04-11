import discord
from discord.commands.core import slash_command
from discord.ext import commands
import random
import datetime
from modules.utils import get_guildid
from discord.ui import Button, View
class AddButton(discord.ui.Button):
    def __init__(self, texto = None, url = None, custom_id = None, emoji = None):
        super().__init__(
            label = texto,
            style = discord.enums.ButtonStyle.gray,
            url = url,
            custom_id = custom_id,
            emoji = emoji
        )


class Social(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #@slash_command(guild_ids=[int(get_guildid())], description = "Mostra informações do usuário" )
    @commands.command()
    async def perfil(self, ctx, member: discord.Member = None):
        """Mostra informações do usuario """    
            #region embeds
        #await ctx.defer()
        if not member: member = ctx.author
        if not member.bot:
            try:
                time   = datetime.datetime.now() 
                avatar = member.avatar
                embed  = discord.Embed(color = 0xad75ad, title = f"Perfil do Usuário {member.name}")
                embed.set_thumbnail(url = avatar)
                embed.set_author(name = f"Bot criado por: Andrew Kauã",
                url      = "https://github.com/AndrewHTR",
                icon_url = "https://media.discordapp.net/attachments/673668744471379971/960000584948269076/IMG_20220402_231811.jpg")

                embed.add_field(name = "__**Informações da conta:**__\n", value = f"""**Nome no Discord:** {member.name}\n**Status:** {member.activity}\n**Está atualmente:** {member.status}\n**Conta criada: **{member.created_at.__format__("%d/%m/%Y as %H:%M")}""")
                embed.add_field(name = "__**Informações do perfil no servidor:**__", value = f"""**Nick:** {member.nick}\n**Entrou no servidor:** {member.joined_at.__format__("%d/%m/%Y as %H:%M")}\n**Cargos:** {''.join([r.mention for r in member.roles[1:]])}""", inline=False)
                embed.set_footer(text = f"Horário: {time.strftime('%H:%M:%S')}", icon_url = "https://media.discordapp.net/attachments/661371734531768363/961359898233430016/unknown.png")
                #endregion       
                button = Button(label='dsadsa', style=discord.ButtonStyle.gray)
                view = View(timeout=True)
                view.add_item(button)
                seta_esquerda = view.add_item(AddButton(texto='⬅️', custom_id='seta_esquerda'))
                seta_direita = view.add_item(AddButton(texto='➡️', custom_id='seta_direita'))  
                aperte = view.add_item(AddButton(texto='Clique aqui!'))
                async def button_callback(interaction):
                    print('foi')
                    await interaction.response.send_message(content='Pimpolho')
                    return
                button.callback = button_callback
                await ctx.send(embed=embed, view=view)
                
            
            except:
                await ctx.send('Erro. D:')

def setup(bot):
    bot.add_cog(Social(bot))