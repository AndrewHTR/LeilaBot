import discord, aiohttp, random, datetime
from discord.commands import command
from discord.commands.core import slash_command
from discord.ext import commands
from modules.utils import get_guildid
from urllib.request import urlopen
from bs4 import BeautifulSoup

role_ids = [...]

class AddButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label = "nomes fodas",
            style = discord.enums.ButtonStyle.primary,
        )

class Comandos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[int(get_guildid())], description = "Faz com que o bot mande mensagem")
    async def falar(self, ctx, *, arg):
        await ctx.respond(''.join(arg))

    @commands.command()
    async def webhookzada(self, ctx):
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
            linhas = bs.find_all('div', {'class':'css-hkjq8i'})
            test, a, b, c = [], [], [], []
            for i in bs.find('div', {'class':'css-hkjq8i'}):
                print(i)
            await webhook.send(f"{linhas}", username='Alfredo')
    
    #@slash_command(guild_ids=[int(get_guildid())])
    @commands.command()
    async def debug(self, ctx):
        """Teste com botões"""

        # timeout is None because we want this view to be persistent.
        view = discord.ui.View(timeout=None)

        # Loop through the list of roles and add a new button to the view for each role.
        for role_id in role_ids:
            # Get the role from the guild by ID.
            role = ctx.guild.get_role(role_id)
            view.add_item(AddButton())
        embed = discord.Embed(title='Testezada')
        await ctx.send(embed=embed, view=view)
        
def setup(bot):
    bot.add_cog(Comandos(bot))