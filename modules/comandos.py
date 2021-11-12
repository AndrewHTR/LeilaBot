import discord
from modules import tokenzada as tk
from discord.ext import commands
import decimal
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


"""@bot.comand()"""


bot.run(tk.Tokenzada.token)