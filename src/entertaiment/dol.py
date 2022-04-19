import discord
from async_timeout import timeout
from discord.ext import commands, bridge
from discord.ext.bridge import BridgeContext, BridgeExtContext, BridgeApplicationContext
import requests
class Dol(commands.Cog):
    def __init__(self, bot: bridge.Bot):
        self.bot = bot

    @commands.command()
    async def dolar(self, ctx: BridgeContext):
        thumb = 'https://cdn.discordapp.com/attachments/857302713233833987/965966562282573864/kisspng-powell-law-group-p-c-brazilian-real-moeda-de-um-moedas-5b344c7a44d4a0.7824366215301541062819.png'
        embed = discord.Embed(title='BRL para USD:', color=0xad75ad, description=f"O valor do Real para o Dólar atualmente está em R${round(float(dolar_value), 2)}")
        embed.set_thumbnail(thumb)
        url = 'https://economia.awesomeapi.com.br/all/USD-BRL'

        response = requests.get(url)

        if response.status_code == 200:
            dolar_value = response.json()['USD']['low']
            await ctx.send(embed=embed)
        else:
            await ctx.send('Erro ao buscar valor do Dólar')


def setup(bot):
    bot.add_cog(Dol(bot))