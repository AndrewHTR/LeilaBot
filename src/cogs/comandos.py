import discord, aiohttp, random, datetime
from discord.commands import slash_command, command
from discord.ext import commands
from modules.utils import get_guildid
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Comandos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[int(get_guildid())], help="Faz com que o bot mande mensagem")
    async def falar(self, ctx, *, arg):
        await ctx.respond(''.join(arg))

    @commands.command()
    async def teste(self, ctx):
        html = urlopen("https://store.epicgames.com/pt-BR/")
        bs = BeautifulSoup(html, 'html.parser')

        async with aiohttp.ClientSession() as session:
            time = datetime.datetime.now()
            webhook = discord.Webhook.from_url('https://discord.com/api/webhooks/959082526616465480/Ztrt68L7WuDp29DU21S-hPcDMMVycy5-CkFaIaSCw9rSPB5ryQ85nfRFj_myMag5UIxN', session=session)
            embed = discord.Embed(title="Informações: ", color = random.randint(0, 0xffffff))
            embed.set_author(name=f"Bot criado por: Andrew Kauã",
            url = "https://github.com/AndrewHTR",
            icon_url="https://cdn.discordapp.com/avatars/500456611073228821/481f96ffc73c973188e9595317256e94.png")
            embed.set_footer(text=f"Horário: {time.strftime('%H:%M:%S')}", icon_url="https://cdn.discordapp.com/avatars/689012066266382351/c16512460537ad5174c5c16a319e1258.png")
            linhas = bs.find('div', {'class':'css-voksei'})
            test, a, b, c = [], [], [], []
            for i in linhas:
                filhas = i.findChildren('div')
                test.append(filhas[0].text)
                a.append(filhas[1].text)
                b.append(filhas[2].text)
                c.append(filhas[3])
            await webhook.send(f"{linhas}", username='Alfredo')
        
def setup(bot):
    bot.add_cog(Comandos(bot))