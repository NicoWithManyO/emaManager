from django.conf import settings
import coc
from coc import utils

coc_client = settings.COC_CLIENT

async def get_clan_info(tag):
    if not utils.is_valid_tag(tag):
        return None
    try:
        clan = await coc_client.get_clan(tag)
    except coc.NotFound:
        return None
    return clan
