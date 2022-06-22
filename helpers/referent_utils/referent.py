
from Referent.models import Referent

async def add_team_referent(member):
    print(member.joined_at)
    new_referent = Referent(discord_id=member.id, name=member.display_name, discriminator=member.discriminator, joined_date=member.joined_at)
    new_referent.save()
    new_referent = Referent.objects.filter(pk=member.id)[0]
    return new_referent
    