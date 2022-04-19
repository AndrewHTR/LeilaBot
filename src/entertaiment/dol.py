import discord
from discord.ext import commands
import requests
import datetime

class Dol(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def dolar(self, ctx: commands.Context):
        time = datetime.datetime.utcnow()
        url = 'https://economia.awesomeapi.com.br/all/USD-BRL'
        response = requests.get(url)
        dolar_value = response.json()['USD']['low']

        embed = discord.Embed(title='__**BRL para USD:**__', color = 0xad75ad, description=f"O valor do **Real** para o **Dólar** atualmente está em __R${round(float(dolar_value), 2)}__")
        embed.set_footer(text = f"Horário: {time.strftime('%H:%M:%S')}", icon_url = "https://media.discordapp.net/attachments/661371734531768363/961359898233430016/unknown.png")
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/959082477555679232/966071295185915954/kiss.png')

        if response.status_code == 200:
            await ctx.send(embed=embed)
        else:
            await ctx.send('Erro ao buscar valor do Dólar')
    
    @commands.command()
    async def euro(self, ctx: commands.Context):
        time = datetime.datetime.utcnow()
        url = 'https://economia.awesomeapi.com.br/all/'
        response = requests.get(url)
        euro_value = response.json()['EUR']['low']

        embed = discord.Embed(title='__**BRL para EUR:**__', color = 0xad75ad, description=f"O valor do **Real** para o **Euro** atualmente está em __R${round(float(euro_value), 2)}__")
        embed.set_footer(text = f"Horário: {time.strftime('%H:%M:%S')}", icon_url = "https://media.discordapp.net/attachments/661371734531768363/961359898233430016/unknown.png")
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/959082477555679232/966071295185915954/kiss.png')

        if response.status_code == 200:
            await ctx.send(embed=embed)
        else:
            await ctx.send('Erro ao buscar valor do Dólar')


def setup(bot):
    bot.add_cog(Dol(bot))