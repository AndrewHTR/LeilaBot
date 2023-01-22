import discord
from discord import app_commands
from discord.ext import commands
import time
import random

class Minigames(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command()
    async def jokenpo(self, inter: discord.Interaction):
        resposta_bot = random.choice(['Pedra', 'Papel', 'Tesoura'])
        await inter.response.send_message('Vamos brincar de Jokenpo!')
        time.sleep(1)
        await inter.response.send_message('Escolha Pedra, Papel ou Tesoura e vamos ver quem ganha! :smirk_cat:')
        resposta = await self.bot.wait_for('message', check=lambda message: message.author == inter.user)
        resposta_user = resposta.content.lower()
        await inter.response.send_message(f"Eu escolho {resposta_bot}")
        if resposta_user == 'pedra':
            if resposta_bot == "Papel":
                await inter.response.send_message('Eu ganhei :sunglasses:')

            elif resposta_bot == 'Pedra':
                await inter.response.send_message('Empate :cry:')

            elif resposta_bot == 'Tesoura':
                await inter.response.send_message('Você ganhou :unamused:')
        
        elif resposta_user == 'papel':
            if resposta_bot == "Papel":
                await inter.response.send_message('Empate :cry:')

            elif resposta_bot == 'Pedra':
                await inter.response.send_message('Você ganhou :unamused:')

            elif resposta_bot == 'Tesoura':
                await inter.response.send_message('Eu ganhei :sunglasses:')

        elif resposta_user == 'Tesoura':
            if resposta_bot == "Papel":
                await inter.response.send_message('Você ganhou :unamused:')

            elif resposta_bot == 'Pedra':
                await inter.response.send_message('Eu ganhei :sunglasses:')

            elif resposta_bot == 'Tesoura':
                await inter.response.send_message('Empate :cry:')
