
import discord
from discord.ext import commands

import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_EmaManager.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


extensions_list = ['helpers.cogs_PublicCommand', 'helpers.cogs_ReferentCommand' ]
all_guilds = [ 269040955380858880 ]


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=["&", ], case_insensitive=True, intents=discord.Intents.all())
        for extension in extensions_list:
            try:
                self.load_extension(extension)
            except Exception as extension:
                print(f"[ewb.EXTENSION ERROR]")

    async def on_ready(self):
        print(f"{self.user} ({self.user.id}) ready !")


if __name__ == "__main__":
    ewb = Bot()
    ewb.run(os.environ.get("DISCORD_BOT_TOKEN"))