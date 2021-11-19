import discord
from discord import activity
import modules.comandos as cm
import modules.tokenzada as tk
client = discord.Client()

@client.event
async def on_ready():
    print('Logado como: {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$Hello'):
        await message.channel.send('Hello')
client.run(tk.Tokenzada.token) 

