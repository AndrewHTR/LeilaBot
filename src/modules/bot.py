import datetime
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from modules.utils import get_guildid

class AddButton(discord.ui.Button):
    def __init__(self, texto, url):
        super().__init__(
            label = texto,
            style = discord.enums.ButtonStyle.primary,
            url = url
        )

class NewHelpName(commands.MinimalHelpCommand):
    def add_bot_commands_formatting(self, commands, heading):
        """Adds the minified bot heading with commands to the output.

        The formatting should be added to the :attr:`paginator`.

        The default implementation is a bold underline heading followed
        by commands separated by an EN SPACE (U+2002) in the next line.

        Parameters
        -----------
        commands: Sequence[:class:`Command`]
            A list of commands that belong to the heading.
        heading: :class:`str`
            The heading to add to the line.
        """

        if commands:
            # U+2002 Middle Dot
            joined = ",\u2002".join(c.name for c in commands)
            self.paginator.add_line(f"__**{heading}:**__")
            self.paginator.add_line(f"```{joined}```")
        
    def add_subcommand_formatting(self, command):
        fmt = "{0}`{1}` \N{EN DASH} {2}" if command.short_doc else "{0}`{1}`"
        self.paginator.add_line(fmt.format(self.context.clean_prefix, command.qualified_name, command.short_doc))

    def get_opening_note(self):
        command_name = self.invoked_with
        return (
            f"Você pode utilizar `{self.context.clean_prefix}{command_name} [comando]` para mais informações sobre o comando.\n"
            f"Você também pode usar `{self.context.clean_prefix}{command_name} [categoria]` para mais informações sobre a categoria."
        )

    def add_command_formatting(self, command):
        if command.description:
            self.paginator.add_line(command.description, empty=True)

        signature = self.get_command_signature(command)
        if command.aliases:
            self.paginator.add_line(signature)
            self.add_aliases_formatting(command.aliases)
        else:
            self.paginator.add_line(signature, empty=True)

        if command.help:
            try:
                self.paginator.add_line(command.help, empty=True)
            except RuntimeError:
                for line in command.help.splitlines():
                    self.paginator.add_line(line)
                self.paginator.add_line()

    async def send_pages(self):
        destination = self.get_destination()
        self.paginator.add_line("\nPara mais informações aperte no botão **Wiki** abaixo. :D")
        time = datetime.datetime.now() 
        emby = discord.Embed(color = 0xad75ad, title='**Comandos do bot:**', description='')
        emby.set_footer(text = f"Horário: {time.strftime('%H:%M:%S')}", icon_url = "https://media.discordapp.net/attachments/661371734531768363/961359898233430016/unknown.png")
        for page in self.paginator.pages:
            emby.description += page   
        view = discord.ui.View(timeout=None)

        view.add_item(AddButton(texto='Wiki', url='https://github.com/AndrewHTR/AlfredoBot/wiki'))
        await destination.send(embed=emby, view=view)

guild = discord.Object(id=int(get_guildid()))

class Bot(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    async def setup_hook(self):
        await self.load_extension("cogs")
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

    