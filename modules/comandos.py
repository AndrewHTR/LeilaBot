import discord
from discord import client
from discord.flags import Intents
from tokenzada import Tokenzada as tk
from discord.ext import commands, tasks
import os
import youtube_dl
import random
import time
import asyncio
import requests
intentin = discord.Intents().all()
client = discord.Client(Intents=intentin)
bot = commands.Bot(command_prefix='!', description='a')

@bot.command()
async def falar(ctx, *, arg):
    await ctx.message.delete()
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

@bot.command(name='join', help='Manda o bot entrar em um canal de voz')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send(f'{ctx.message.author.name} não está conectado.')
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()
@bot.command(name='leave', help='Manda o bot sair do canal de voz.')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send('O bot não está conectado ao canal de voz.')

@bot.command()
async def play(ctx,url):
    try:
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send(f'**Tocando:** {filename}')
    except:
        await ctx.send('O bot não está conectado a um canal de voz. ')

@bot.command()
async def pause(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    """voice_channel = ctx.message.guild.voice_client"""
    if voice_channel.is_playing():
         voice_channel.pause()
    else:
        await ctx.send("O bot não está tocando nada no momento")

@bot.command()
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if ctx.message.guild.voice_client.is_paused():
         ctx.message.guild.voice_client.resume()
    else:
        await ctx.send("O bot não está tocando nada. Use o comando !play (musica) para tocar algo.")

@bot.command()
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if ctx.message.guild.voice_client.is_playing():
         ctx.message.guild.voice_client.stop()
    else:
         ctx.send(" O bot não está tocando nada no momento.")
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restricfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'options': '-vn'
}
 
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self,source,*,data,volume=0.5):
        super().__init__(source,volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""
    @classmethod
    async def from_url(cls,url,*,loop=None,stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename
@bot.command()
async def converter(ctx,a,b):

    convertter = requests.get('https://www.bcb.gov.br/conversao')
    print(convertter)

bot.run(tk.token)