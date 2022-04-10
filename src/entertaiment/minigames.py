from discord.commands import slash_command
from discord.ext import commands
import time
import random

class Minigames(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def jokenpo(self, ctx,opcao):
        a = opcao.upper()
        respostabot = random.randint(1,3)
        joken = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
        if opcao == "PEDRA":
            if a == 1:
                await ctx.send(f'Eu escolhi {joken.get(respostabot)}...')
                time.sleep(1)
                await ctx.send('Empate!! :face_exhaling:')
            elif a == 2:
                await ctx.send(f'Eu escolhi {joken.get(respostabot)}...')
                time.sleep(1)
                await ctx.send(f'Ganhei! :sunglasses:')
            else:
                await ctx.send(f'Eu escolhi {joken.get(respostabot)}...')
                time.sleep(1)
                await ctx.send(f'Você ganhou :neutral_face:')
        if a == 'PAPEL':
                if respostabot == 1:
                    await ctx.send(f'Eu escolhi {joken.get(respostabot)}...')
                    time.sleep(1)
                    await ctx.send('Você ganhou... :neutral_face:')
                elif respostabot == 2:
                    await ctx.send(f'Eu escolhi {joken.get(respostabot)}...')
                    time.sleep(1)
                    await ctx.send('Empate!! :face_exhaling:')
                else: 
                    await ctx.send(f'Eu escolhi {joken.get(respostabot)}...')
                    time.sleep(1)
                    await ctx.send('Ganhei! :sunglasses:')
        if a == 'TESOURA':
                if respostabot == 1:
                    await ctx.send(f'Eu escolhi {joken.get(respostabot)}...')
                    time.sleep(1)
                    await ctx.send('Ganhei! :sunglasses:')
                elif respostabot == 2:
                    await ctx.send(f'Eu escolhi {joken.get(respostabot)}...')
                    time.sleep(1)
                    await ctx.send('Você ganhou... :neutral_face:')
                else: 
                    await ctx.send(f'Eu escolhi {joken.get(respostabot)}...')
                    time.sleep(1)
                    await ctx.send('Empate!! :face_exhaling:')
                    
def setup(bot):
    bot.add_cog(Minigames(bot))