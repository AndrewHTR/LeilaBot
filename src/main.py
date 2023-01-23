import asyncio
import discord
from modules.utils import get_token, get_prefix
from modules.bot import Bot

intents = discord.Intents().all()

bot = Bot(command_prefix=get_prefix(), intents=intents)

async def main():
    async with bot:
        await bot.start(get_token())

asyncio.run(main()) 