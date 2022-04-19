import discord
from discord.commands.core import slash_command
from discord.ext import commands, bridge
from discord.ext.bridge import BridgeContext, BridgeExtContext, BridgeApplicationContext
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
    @bridge.bridge_command(help='Mostra perfil dos usuarios')
    async def perfil(self, ctx: BridgeContext, member: discord.Member = None):
        """Mostra informações do usuario """    
            #region embeds
        #await ctx.defer()
        if not member: member = ctx.author
        if not member.bot:
            time   = datetime.datetime.now() 
            avatar = member.avatar
            
            embed  = discord.Embed(color = 0xad75ad, title = f"Perfil do Usuário {member.name}")
            embed.set_thumbnail(url = avatar)
            #embed.set_author(name = f"Bot criado por: Andrew Kauã",
            #url      = "https://github.com/AndrewHTR",
            #icon_url = "https://media.discordapp.net/attachments/673668744471379971/960000584948269076/IMG_20220402_231811.jpg")

            embed.add_field(name = "__**Informações da conta:**__\n", value = f"""**Nome no Discord:** {member.name}\n**Status:** {member.activity}\n**Está atualmente:** {member.status}\n**Conta criada: **{member.created_at.__format__("%d/%m/%Y as %H:%M")}""")
            embed.add_field(name = "__**Informações do perfil no servidor:**__", value = f"""**Nick:** {member.nick}\n**Entrou no servidor:** {member.joined_at.__format__("%d/%m/%Y as %H:%M")}\n**Cargos:** {' '.join([r.mention for r in member.roles[1:]])}""", inline=False)
            embed.set_footer(text = f"Horário: {time.strftime('%H:%M:%S')}", icon_url = "https://media.discordapp.net/attachments/661371734531768363/961359898233430016/unknown.png")
            #endregion       
            button = Button(label='Aperte', style=discord.ButtonStyle.gray, emoji='➡️')
            button2 = Button(label='Fechar')
            async def button_callback(interaction: discord.Interaction):
                embed.add_field(name='__**teste:**__', value='testando')
                await interaction.response.edit_message(embed=embed)
                #await interaction.response.send_message("Apertou foi :3")
            async def button2_callback(interaction: discord.Interaction):
                await interaction.response.edit_message(delete_after=0.1)
            button.callback = button_callback
            button2.callback = button2_callback
            
            view = View(timeout=5.0)
            view.add_item(button)
            view.add_item(button2)

            #await ctx.send(embed=embed, view=view)
                                 
             
            if isinstance(ctx, BridgeExtContext):
                await ctx.send(embed=embed, view=view)
            else: 
                await ctx.respond(embed=embed, view=view)
   
    #@slash_command(guild_ids=[int(get_guildid())], description = "Mostra informações do usuário" )
    @bridge.bridge_command(help='Mostra o avatar do usuario')
    async def avatar(self, ctx: BridgeContext, member: discord.Member = None):
        if not member: member = ctx.author
        avatar = member.avatar.url[:90]
        time   = datetime.datetime.now() 
        
        embed = discord.Embed(title=f'__**Avatar requisitado por:**__ **{ctx.author.name}**', color = 0xad75ad, description='Aperte no botão **"DOWNLOAD"** abaixo\npara fazer download da imagem.')
        embed.set_image(url=avatar)
        embed.set_footer(text = f"Horário: {time.strftime('%H:%M:%S')}", icon_url = "https://media.discordapp.net/attachments/661371734531768363/961359898233430016/unknown.png")

        download_button = Button(label='Download', url=avatar)
        view = View(timeout=None)
        view.add_item(download_button)

        if isinstance(ctx, BridgeExtContext):
            await ctx.send(embed=embed, view=view)
        else:
            await ctx.respond(embed=embed, view=view)

    @bridge.bridge_command(help='Mostra o icone do server')
    async def icon(self, ctx: BridgeContext):
        icon = ctx.guild.icon.url[:88]
        print(icon)
        time   = datetime.datetime.now() 
        embed = discord.Embed(title=f'__**Icone requisitado por:**__ **{ctx.author.name}**', color = 0xad75ad, description='Aperte no botão **"DOWNLOAD"** abaixo\npara fazer download da imagem.')
        embed.set_image(url=icon)
        embed.set_footer(text = f"Horário: {time.strftime('%H:%M:%S')}", icon_url = "https://media.discordapp.net/attachments/661371734531768363/961359898233430016/unknown.png")

        download_button = Button(label='Download', url=icon)
        view = View(timeout=None)
        view.add_item(download_button)
        
        
        if isinstance(ctx, BridgeExtContext):
            await ctx.send(embed=embed, view=view)
        else:
            await ctx.respond(embed=embed, view=view)
    
    @bridge.bridge_command()
    async def server(self, ctx: BridgeContext):
        time   = datetime.datetime.now()

        rolelist = [r.name for r in ctx.guild.roles if r != ctx.guild.default_role]
        roles = ", ".join(rolelist)
        
        embed = discord.Embed(title=f'**Informações do servidor: {ctx.guild.name}**', color=0xad75ad,
        description=f'💠 **Dono do server:** {ctx.guild.owner}\n💠 **Data de crianção:** {ctx.guild.created_at.__format__("%d/%m/%Y as %H:%M")}\n💠 **Usuarios:** {ctx.guild.member_count.real}\n💠 Canais de texto: {len(ctx.guild.text_channels)}\n💠 Canais de voz: {len(ctx.guild.voice_channels)}\n💠 Prefixo atual: {ctx.prefix}')
        embed.set_author(name='Informações de servidor', icon_url=ctx.guild.icon.url[:88])
        embed.add_field(name='**Cargos do servidor:**', value=f'{roles}\n\nServer ID: {ctx.guild.id}')
        embed.set_footer(text = f"Horário: {time.strftime('%H:%M:%S')}", icon_url = "https://media.discordapp.net/attachments/661371734531768363/961359898233430016/unknown.png")

        if isinstance(ctx, BridgeExtContext):
            await ctx.send(embed=embed)
        else:
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Social(bot)) 