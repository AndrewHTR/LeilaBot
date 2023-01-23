import discord
from discord import app_commands
from discord.app_commands import checks
from discord.ext import commands
from modules.utils import get_guildid

class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="reload")
    async def _reload(self, inter: discord.Interaction, module: str):
        
        try:
            await self.bot.load_extension(f"cogs.{module}")
        except commands.ExtensionAlreadyLoaded:
            await inter.response.send_message("Cog is loaded")
        except commands.ExtensionNotFound:
            await inter.response.send_message("Cog not found")
        else:
            await inter.response.send_message("Cog is unloaded")
            await self.bot.unload_extension(f"cogs.{module}")

