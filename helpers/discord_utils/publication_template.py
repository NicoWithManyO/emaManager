
import discord, random

def random_color():
    return random.randint(0, 16777215)

def set_tournament_color(tournament):
    if tournament.name == "Ranking":
        return discord.Color.dark_green()
    if tournament.name == "E-cup":
        return discord.Color.blue()

def roster_traitement(roster):
    if roster.startswith("M"):
        return f"🇲ixt"
    if roster.startswith("F"):
        return f"🇫ull"

async def std_team_embed(tournament, data):
    roster = roster_traitement(data.roster)
    e = discord.Embed(color=random_color(), title=f"{data.id}. {data.name}", description=f"Roster **{roster}**\n<:clan:850857450731077652> **{data.active_clan.tag}** [{data.active_clan.name}]({data.active_clan.clan_iglink}) (lvl{data.active_clan.clan_level})")
    e.set_author(name=f"{tournament} 🇸{tournament.current_season}", icon_url=tournament.logo_url)
    e.set_footer(text=tournament.organization_owner, icon_url=tournament.organization_owner.logo_url)
    e.add_field(name=f"Référent", value=f"<:discord:848504368226369536> {data.referent_owner}")
    if data.second_referent:
        e.add_field(name=f"Second référent", value=f"<:discord:848504368226369536> {data.second_referent}")
    if data.blason_url:
        e.set_thumbnail(url=data.blason_url)
    else:
        e.set_thumbnail(url=tournament.logo_url)
        e.add_field(name="ℹ️ attention", value="Vous n'avez pas fournit de blason", inline=False)
    return e

async def std_tournament_embed(tournament):
    e = discord.Embed(color=set_tournament_color(tournament))
    e.set_author(name=f"{tournament} 🇸{tournament.current_season}", icon_url=tournament.logo_url)
    e.set_footer(text=tournament.organization_owner, icon_url=tournament.organization_owner.logo_url)
    e.set_thumbnail(url=tournament.logo_url)
    if tournament.is_active:
        e.add_field(name="✅ Actif", value=f"current round : `{tournament.current_round}`")
    else:
        e.add_field(name="🚫 Inactif", value="Restez branché pour d'éventuelles nouvelles saisons")
    return e