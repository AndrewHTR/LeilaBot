import discord
from discord import client
import tokenzada as tk
from discord.ext import commands
import decimal
import random
import time

bot = commands.Bot(command_prefix='!', description='a')

@bot.command()
async def falar(ctx, *, arg):
    await ctx.send(''.join(arg))

@bot.command()
async def mat(ctx,a: int,b, c: int):
    match(b):
        case'+':
            await ctx.send(a + c)
        case '*':
            await ctx.send(a * c)
        case '/':
            
            await ctx.send(round(a / c, 2))
        case '**':
            await ctx.send(round(a ** c, 2))

@bot.command()
async def jokenpo(ctx,opcao):
    a = opcao.upper()
    respostabot = random.randint(1,3)
    joken = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
    match(a):
        case 'PEDRA':
            if respostabot == 1:
                await ctx.send(f'Eu escolhi {joken.get(respostabot)}...')
                time.sleep(1)
                await ctx.send('Empate!! :face_exhaling:')
            elif respostabot == 2:
                await ctx.send(f'Eu escolhi {joken.get(respostabot)}...')
                time.sleep(1)
                await ctx.send(f'Ganhei! :sunglasses:')
            else:
                await ctx.send(f'Eu escolhi {joken.get(respostabot)}...')
                time.sleep(1)
                await ctx.send(f'Você ganhou :neutral_face:')
        case 'PAPEL':
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
        case 'TESOURA':
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

"""@bot.command()
async def ajuda(ctx,pessoa):
    await discord.send_friend_request(pessoa)"""

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@bot.command()
async def leave(context):
    await context.voice_client.disconnect()



bot.run(tk.Tokenzada.token)