
import discord
from discord.ext import commands
from discord.commands import slash_command
from discord import option
import coc

import django
from django.utils.text import slugify
import datetime
import sys
import psutil
from django.utils import version

from Team.models import Team
from Tournament.models import Tournament, PossibleRoster
from .team_utils.team import add_team_clan, add_team_referent
from helpers.discord_utils.publication_template import std_team_embed, std_tournament_embed

from helpers.discord_utils.discord_view import Confirm

TOURNAMENT_CHOICES = []
for _ in Tournament.objects.all():
    TOURNAMENT_CHOICES.append(str(_))

ROSTER_CHOICES = []
for _ in PossibleRoster.objects.all():
    ROSTER_CHOICES.append(str(_))

class PublicCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="competition", description="(ref) Affiche les informations d'une compétition", guild_ids=[778509735397031936, 269040955380858880])
    @option(name="tournament", description="Compétition pour l'inscription", choices=TOURNAMENT_CHOICES)
    async def tournament(self, ctx, tournament):
        tournament = Tournament.objects.filter(name=tournament)[0]
        await ctx.respond(embed=await std_tournament_embed(tournament))

    @slash_command(name="inscription", description="(ref) Inscrire une équipe", guild_ids=[778509735397031936, 269040955380858880])
    @option(name="tournament", description="Compétition pour l'inscription", choices=TOURNAMENT_CHOICES)
    @option(name="roster", description="Roster d'inscription", choices=ROSTER_CHOICES)
    @option(name="clan_tag", descirption="Tag du clan utilisé pour vos matchs")
    @option(name="second_referent", description="Second référent (vivement conseillé)")
    @option(name="blason", seconde="Entrez ici, si possible, l'url du blason de votre équipe")
    async def register(self, ctx, tournament: str, name: str, roster: str, clan_tag: str, second_referent: discord.Member = None, blason = None):
        tournament = Tournament.objects.filter(name=tournament)[0]
        slug = slugify(f"{tournament.code_name}_{name}_{roster}")
        if Team.objects.filter(slug=slug).exists():
            await ctx.respond(f"> 🚫 Une équipe `{name}` existe déjà en `{tournament} {roster}`")
            return
        new_clan = await add_team_clan(clan_tag)
        if new_clan == None:
            await ctx.respond(f"> 🚫 `{clan_tag}` n'est pas un tag valide !")
            return
        else:
            new_owner = await add_team_referent(ctx.user)
            if second_referent:
                second_referent = await add_team_referent(second_referent)
            else:
                second_referent = None
        new_team = Team(name=name, slug=slug, roster=roster, tournament=tournament, registered_for_round=tournament.current_round, referent_owner=new_owner, second_referent=second_referent, active_clan=new_clan)
        if blason:
            new_team.blaosn = blason
        view = Confirm(ctx.user)
        confirmator = await ctx.send(f"> {new_team}", view=view)
        await view.wait()
        if view.value is None:
            print("Timed out...")
        elif view.value:
            new_team.save()
            new_team = Team.objects.filter(slug=slugify(f"{tournament.code_name}_{name}_{roster}"))[0]
            await ctx.send(embed=await std_team_embed(new_team.tournament, new_team))
            await ctx.respond(f"> ✅ Inscription validée")
            print("Confirmed...")
        else:
            await ctx.respond(f"> 🚫 {confirmator.content}")
            print("Cancelled...")
        await confirmator.delete()

    @slash_command(name="invite", description="Renvoi l'invitation du serveur", guild_ids=[778509735397031936, 269040955380858880])
    async def invit(self, ctx):
        e = discord.Embed(title = "Partagez ce lien pour inviter vos amis sur E-magine Gaming", description = f"> ** https://discord.gg/4yAZ2wV **\n\n[Twitter Ema](https://twitter.com/emagine_gaming?lang=fr)")
        await ctx.respond(embed=e)
            
    @slash_command(name="bot", description="(admin) Info système", guild_ids=[778509735397031936, 269040955380858880])
    async def info_sys(self, ctx):
        e = discord.Embed(description=f"**```Bot info```**")
        e.add_field(
            name=f"{datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}",
            value=f"bot_server boot since",
            inline=False,
        )
        e.add_field(
            name=f"{sys.version}",
            value=f"python version",
            inline=False,
        )
        e.add_field(
            name=f"{django.get_version()}",
            value=f"django version",
            inline=False
        )
        e.add_field(
            name=f"{discord.__version__}",
            value="pycord version",
            inline=True,
        )
        e.add_field(
            name=f"{coc.__version__}",
            value=f"coc lib version",
            inline=True,
        )
        e.add_field(
            name=f"current guild\n{ctx.guild.name}",
            value=f"{ctx.guild.id}",
            inline=False,
        )
        e.add_field(
            name=f"{len(ctx.guild.members)} membres",
            value="users_count",
            inline=True,
        )
        e.add_field(
            name=f"{len(ctx.guild.channels)} rooms",
            value="channels_count",
            inline=True,
        )
        e.set_thumbnail(url=f"{self.bot.user.display_avatar}")
        await ctx.respond(embed=e)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self} ready")

def setup(bot):
    bot.add_cog(PublicCommand(bot))