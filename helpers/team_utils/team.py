
from operator import truediv
from ..ingame_utils.ingame import get_clan_info
from Ingame.models import CocClan
from Referent.models import Referent


async def add_team_clan(tag):
    data_clan = await get_clan_info(tag)
    if data_clan == None:
        return None
    new_clan = CocClan(discord_add=True, tag=data_clan.tag, name=data_clan.name, public_warlog=data_clan.public_war_log, clan_level=data_clan.level, clan_iglink=data_clan.share_link)
    new_clan.save()
    new_clan = CocClan.objects.filter(pk=data_clan.tag)[0]
    return new_clan

async def add_team_referent(member):
    new_referent = Referent(discord_id=member.id, name=member.display_name, discriminator=member.discriminator, member_avatar=member.display_avatar)
    new_referent.save()
    new_referent = Referent.objects.filter(pk=member.id)[0]
    return new_referent
    
async def check_if_is_orga_staff(tournament, referent):
    pass