import discord
from discord import app_commands
from discord.ext import commands
import requests
import datetime

class Dol(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command()
    async def dolar(self, inter: discord.Interaction):
        time = datetime.datetime.utcnow()
        url = 'https://economia.awesomeapi.com.br/all/USD-BRL'
        response = requests.get(url)
        dolar_value = response.json()['USD']['low']

        embed = discord.Embed(title='__**BRL para USD:**__', color = 0xad75ad, description=f"O valor do **Real** para o **Dólar** atualmente está em __R${round(float(dolar_value), 2)}__")
        embed.set_footer(text = f"Horário: {time.strftime('%H:%M:%S')}", icon_url = "https://media.discordapp.net/attachments/661371734531768363/961359898233430016/unknown.png")
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/959082477555679232/966071295185915954/kiss.png')

        await inter.response.send_message(embed=embed)
    
    @app_commands.command()
    async def euro(self, inter: discord.Interaction):
        time = datetime.datetime.utcnow()
        url = 'https://economia.awesomeapi.com.br/all/'
        response = requests.get(url)
        euro_value = response.json()['EUR']['low']

        embed = discord.Embed(title='__**BRL para EUR:**__', color = 0xad75ad, description=f"O valor do **Real** para o **Euro** atualmente está em __R${round(float(euro_value), 2)}__")
        embed.set_footer(text = f"Horário: {time.strftime('%H:%M:%S')}", icon_url = "https://media.discordapp.net/attachments/661371734531768363/961359898233430016/unknown.png")
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/959082477555679232/966071295185915954/kiss.png')

        await inter.response.send_message(embed=embed)
       
