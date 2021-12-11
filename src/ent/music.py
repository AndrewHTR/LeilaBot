import pytube
import discord
import os
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='join', help='Manda o commands entrar em um canal de voz')
    async def join(self, ctx):
        if not ctx.message.author.voice:
            await ctx.send(f'{ctx.message.author.name} não está conectado.')
        else:
            channel = ctx.message.author.voice.channel
        await channel.connect()
    @commands.command(name='leave', help='Manda o commands sair do canal de voz.')
    async def leave(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await ctx.send('O commands não está conectado ao canal de voz.')

    @commands.command()
    async def play(self,ctx, *, url):
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
        server = ctx.message.guild
        voice = server.voice_client
        
        yt = pytube.YouTube(url)
        print(f'O video: {yt.title}')
        myitag = 251
        if 'https' not in url:
            video = pytube.Search(yt)
        
        video = yt.streams.get_by_itag(myitag)
        video.download(filename='music')
        voice.play(discord.FFmpegPCMAudio(executable='ffmpeg.exe', source= 'music'))
        voice.is_playing()
        
    @commands.command()
    async def pause(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client
        """voice_channel = ctx.message.guild.voice_client"""
        if voice_channel.is_playing():
            voice_channel.pause()
        else:
            await ctx.send("O bot não está tocando nada no momento")

    @commands.command()
    async def resume(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if ctx.message.guild.voice_client.is_paused():
            ctx.message.guild.voice_client.resume()
        else:
            await ctx.send("O bot não está tocando nada. Use o comando !play (musica) para tocar algo.")

    @commands.command()
    async def stop(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if ctx.message.guild.voice_client.is_playing():
            ctx.message.guild.voice_client.stop()
        else:
            await ctx.send(" O bot não está tocando nada no momento.")

def setup(bot):
    bot.add_cog(Music(bot))