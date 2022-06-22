
import discord
from discord.ext import commands
from discord.commands import slash_command
from discord import option

from helpers.discord_utils.publication_template import std_team_embed

from Team.models import Team


class ReferentCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="team", description="(ref) Affiche les équipes dont vous êtes référent, ou celle demandées", guild_ids=[778509735397031936, 269040955380858880])
    @option(name="search", descritption="Motif à rechercher (ID, nom d'équipe ou référent")
    async def team(self, ctx, search: str=None):
        all_teams = []
        if not search:
            all_teams = Team.objects.filter(referent_owner=ctx.user.id)
        
        try:
            all_teams = Team.objects.filter(id=int(search))
        except:
            for _ in Team.objects.all():
                if search.lower() in _.name.lower() or _.name.lower() in search.lower():
                    all_teams.append(_)
                if search.lower() in _.referent_owner.name.lower():
                    all_teams.append(_)
                if _.second_referent:
                    if search.lower() in _.second_referent.name.lower():
                        all_teams.append(_)
        set_all_teams = set(all_teams)
        if not all_teams:
            await ctx.respond(f"> 🚫 pas de résultat")
            return
        for _ in set_all_teams:
            await ctx.respond(embed=await std_team_embed(_.tournament, _))

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self} ready")

def setup(bot):
    bot.add_cog(ReferentCommand(bot))