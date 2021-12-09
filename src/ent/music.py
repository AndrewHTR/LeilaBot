from discord.ext import commands
import youtube_dl
import discord
import asyncio

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self,source,*,data,volume=0.5):
        super().__init__(source,volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""
    @classmethod
    async def from_url(cls,url,*,loop=None,stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: Music.ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            data = data['entries'][0]
        filename = data['title'] if stream else Music.ytdl.prepare_filename(data)
        return filename
class Music(commands.Cog):
    def __init__(self, commands):
        self.commands = commands
    
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
    async def play(self, ctx,* ,url):
        try:
            server = ctx.message.guild
            voice_channel = server.voice_client

            async with ctx.typing():
                filename = await YTDLSource.from_url(url, loop=commands.loop)
                voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
            await ctx.send(f'**Tocando:** {filename}')
        except:
            await ctx.send('O commands não está conectado a um canal de voz. ')

    @commands.command()
    async def pause(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client
        """voice_channel = ctx.message.guild.voice_client"""
        if voice_channel.is_playing():
            voice_channel.pause()
        else:
            await ctx.send("O commands não está tocando nada no momento")

    @commands.command()
    async def resume(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if ctx.message.guild.voice_client.is_paused():
            ctx.message.guild.voice_client.resume()
        else:
            await ctx.send("O commands não está tocando nada. Use o comando !play (musica) para tocar algo.")

    @commands.command()
    async def stop(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if ctx.message.guild.voice_client.is_playing():
            ctx.message.guild.voice_client.stop()
        else:
            ctx.send(" O commands não está tocando nada no momento.")
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

def setup(bot):
    bot.add_cog(Music(bot))