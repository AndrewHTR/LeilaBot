from .moderation.moderation import Moderation
from .moderation.social import Social
from .events.ErrorHandler import ErrorHandler
from .events.NotifyHandler import NotifyHandler
from .events.on_ready import OnReady
from .entertaiment.dol import Dol
from .entertaiment.minigames import Minigames


extensions = (
    Moderation,
    Social,
    ErrorHandler,
    NotifyHandler,
    OnReady,
    Dol,
    Minigames,
)

async def setup(bot):
    for extension in extensions:
        await bot.add_cog(extension(bot))