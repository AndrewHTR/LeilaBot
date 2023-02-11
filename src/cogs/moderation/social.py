import discord
from discord import app_commands
from discord.ext import commands
import random
import datetime
from discord.ui import Button, View
from cogs.moderation.mongodb import *


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
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        myquery = {"_id": message.author.id}
        user = collection.find(myquery)
        for result in user:
            score = result["score"]
        score += 1
        collection.update_one({"_id": message.author.id}, {"$set": {"score": score}})
        await message.channel.send(f"Pontos atuais: {score}")
    
    @app_commands.command(description='Mostra perfil dos usuarios')
    async def perfil(self, inter: discord.Interaction, member: discord.Member = None): 
        #region embeds
        myquery = {"_id": inter.user.id}
        if (collection.count_documents(myquery) == 0):
            post = {"_id": inter.user.id, "score": 1}
            collection.insert_one(post)
        if not member: member = inter.user
        if not member.bot:
            time   = datetime.datetime.now() 
            avatar = member.avatar
            
            embed  = discord.Embed(color = 0xad75ad, title = f"Perfil do Usuário {member.name}")
            embed.set_thumbnail(url = avatar)
            
            embed.add_field(name = "__**Informações da conta:**__\n", value = f"""**Nome no Discord:** {member.name}\n**Status:** {member.activity}\n**Está atualmente:** {member.status}\n**Conta criada: **{member.created_at.__format__("%d/%m/%Y as %H:%M")}""")
            embed.add_field(name = "__**Informações do perfil no servidor:**__", value = f"""**Nick:** {member.nick}\n**Entrou no servidor:** {member.joined_at.__format__("%d/%m/%Y as %H:%M")}\n**Cargos:** {' '.join([r.mention for r in member.roles[1:]])}""", inline=False)
            embed.set_footer(text = f"Horário: {time.strftime('%H:%M:%S')}", icon_url = "https://media.discordapp.net/attachments/661371734531768363/961359898233430016/unknown.png")
            #endregion       
            
            view = View(timeout=5.0)

            await inter.response.send_message(embed=embed, view=view)
   
    @app_commands.command(description='Mostra o avatar do usuario')
    async def avatar(self, inter: discord.Interaction, member: discord.Member = None):
        try:
            pass
        except:
            await inter.response.send_message("não foi", ephemeral=True, delete_after=20)
        if member == None: member = inter.user
        avatar = member.avatar.url[:90]
        time   = datetime.datetime.now() 
        embed = discord.Embed(title=f'__**Avatar requisitado por:**__ **{inter.user.name}**', color = 0xad75ad, description='Aperte no botão **"DOWNLOAD"** abaixo\npara fazer download da imagem.')
        a = embed.set_image(url=avatar)
        a.image.width = 800
        a.image.height = 800
        embed.set_footer(text = f"Horário: {time.strftime('%H:%M:%S')}", icon_url = "https://media.discordapp.net/attachments/661371734531768363/961359898233430016/unknown.png")

        download_button = Button(label='Download', url=avatar)
        view = View(timeout=None)
        view.add_item(download_button)

        await inter.response.send_message(embed=embed, view=view)

    @app_commands.command(description='Mostra o icone do server')
    async def icon(self, inter: discord.Interaction):
        icon = inter.guild.icon.url[:88]
        print(icon)
        time   = datetime.datetime.now() 
        embed = discord.Embed(title=f'__**Icone requisitado por:**__ **{inter.user.name}**', color = 0xad75ad, description='Aperte no botão **"DOWNLOAD"** abaixo\npara fazer download da imagem.')
        embed.set_image(url=icon)
        embed.set_footer(text = f"Horário: {time.strftime('%H:%M:%S')}", icon_url = "https://media.discordapp.net/attachments/661371734531768363/961359898233430016/unknown.png")

        download_button = Button(label='Download', url=icon)
        view = View(timeout=None)
        view.add_item(download_button)
        
        await inter.response.send_message(embed=embed, view=view)

    
    @app_commands.command()
    async def server(self, inter: discord.Interaction):
        time   = datetime.datetime.now()

        rolelist = [r.name for r in inter.guild.roles if r != inter.guild.default_role]
        roles = ", ".join(rolelist)
        
        embed = discord.Embed(title=f'**Informações do servidor: {inter.guild.name}**', color=0xad75ad,
        description=f'💠 **Dono do server:** {inter.guild.owner}\n💠 **Data de crianção:** {inter.guild.created_at.__format__("%d/%m/%Y as %H:%M")}\n💠 **Usuarios:** {inter.guild.member_count.real}\n💠 Canais de texto: {len(inter.guild.text_channels)}\n💠 Canais de voz: {len(inter.guild.voice_channels)}\n💠 Prefixo atual: /')
        embed.set_author(name='Informações de servidor', icon_url=inter.guild.icon.url[:88])
        embed.add_field(name='**Cargos do servidor:**', value=f'{roles}\n\nServer ID: {inter.guild.id}')
        embed.set_footer(text = f"Horário: {time.strftime('%H:%M:%S')}", icon_url = "https://media.discordapp.net/attachments/661371734531768363/961359898233430016/unknown.png")
        
        await inter.response.send_message(embed=embed)

