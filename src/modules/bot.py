import discord
from discord.ext import commands
import random

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
            self.paginator.add_line(f"`{joined}`")

    def get_opening_note(self):
        command_name = self.invoked_with
        return (
            f"Você pode utilizar `{self.context.clean_prefix}{command_name} [comando]` para mais informações sobre o comando.\n"
            f"Você também pode usar `{self.context.clean_prefix}{command_name} [categoria]` para mais informações sobre a categoria."
        )

    async def send_pages(self):
        destination = self.get_destination()
        self.paginator.add_line("\nPara mais informações aperte no botão **Wiki** abaixo. :D")
        emby = discord.Embed(color = random.randint(0, 0xffffff), title='Ajuda', description='')

        for page in self.paginator.pages:
            emby.description += page   
        view = discord.ui.View(timeout=None)

        view.add_item(AddButton(texto='Wiki', url='https://github.com/AndrewHTR/AlfredoBot/wiki'))
        await destination.send(embed=emby, view=view)