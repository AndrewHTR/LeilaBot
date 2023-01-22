from discord.ext import commands

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Parece que você não tem permissão para isso bobinho :shushing_face:")
            print(error)
        if isinstance(error, commands.MissingAnyRole):
            await ctx.send("Você não tem um cargo para isso.")
            print(error)
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Esse comando não existe.")
            print(error)
            
    @commands.Cog.listener()
    async def on_application_command_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Parece que você não tem permissão para isso bobinho :shushing_face:")
            print(error)
        if isinstance(error, commands.MissingAnyRole):
            await ctx.send("Você não tem um cargo para isso.")
            print(error)
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Esse comando não existe.")
            print(error)
            
