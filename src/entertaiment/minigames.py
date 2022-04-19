from discord.commands import slash_command
from discord.ext import commands
import time
import random

class Minigames(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command()
    async def jokenpo(self, ctx: commands.Context):
        resposta_bot = random.choice(['Pedra', 'Papel', 'Tesoura'])
        await ctx.send('Vamos brincar de Jokenpo!')
        time.sleep(1)
        await ctx.send('Escolha Pedra, Papel ou Tesoura e vamos ver quem ganha! :smirk_cat:')
        resposta = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
        resposta_user = resposta.content.lower()
        await ctx.send(f"Eu escolho {resposta_bot}")
        if resposta_user == 'pedra':
            if resposta_bot == "Papel":
                await ctx.send('Eu ganhei :sunglasses:')

            elif resposta_bot == 'Pedra':
                await ctx.send('Empate :cry:')

            elif resposta_bot == 'Tesoura':
                await ctx.send('Você ganhou :unamused:')
        
        elif resposta_user == 'papel':
            if resposta_bot == "Papel":
                await ctx.send('Empate :cry:')

            elif resposta_bot == 'Pedra':
                await ctx.send('Você ganhou :unamused:')

            elif resposta_bot == 'Tesoura':
                await ctx.send('Eu ganhei :sunglasses:')

        elif resposta_user == 'Tesoura':
            if resposta_bot == "Papel":
                await ctx.send('Você ganhou :unamused:')

            elif resposta_bot == 'Pedra':
                await ctx.send('Eu ganhei :sunglasses:')

            elif resposta_bot == 'Tesoura':
                await ctx.send('Empate :cry:')
                    
def setup(bot):
    bot.add_cog(Minigames(bot))