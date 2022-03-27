import discord
from discord.ext import commands
import asyncio
import youtube_dl
import pytube
queue = []      
options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}
ffmpeg_options = {'options': '-vn'}
ytdl = youtube_dl.YoutubeDL(options)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')
    @classmethod
    async def from_url(cls, url, *, loop = None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download = not stream))

        if 'entries' in data:
            data = data['entries'][0]
        elif 'formats' in data:
            data = data["formats"][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

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
    
        #server = ctx.message.guild
        #voice = server.voice_client
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        myitag = 251
        arquivo = url
        self.queue = queue
        

        if url in queue:
            await ctx.send('Esta musica já está na queue')
        else:
            queue.append(url)

        for url in queue:
            yt = pytube.YouTube(url)
            video = yt.streams.get_by_itag(myitag)
            video.download(filename='music')

        a = yt.title
        i = 0 
        while i < len(self.queue):
            try:
                voice.play(discord.FFmpegPCMAudio(executable='ffmpeg.exe', source='music'))
                await ctx.send(f'Tocando agora: {yt.title}')
            except:
                pass
            i += 1

        print(f'O video: {yt.title}')
           

           

    @commands.command()
    async def pause(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client
        
        if voice_channel.is_playing():
            voice_channel.pause()
        else:
            await ctx.send("O bot não está tocando nada no momento. Use o comando !play (musica) para tocar algo.")

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
            await ctx.send(" O bot não está tocando nada no momento. Use o comando !play (musica) para tocar algo.")
        queue.clear()
    @commands.command()
    async def queue(self, ctx):
        print(queue)
    

def setup(bot):
    bot.add_cog(Music(bot))