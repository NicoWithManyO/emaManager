from django.db import models

from helpers.ingame_utils.ingame import get_clan_info
from django.conf import settings
coc_client = settings.COC_CLIENT


# Create your models here.
class CocClan(models.Model):
    tag = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=22, blank=True, null=True)
    public_warlog = models.BooleanField(default=False)
    clan_level = models.IntegerField(default=0)
    clan_iglink = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    discord_add = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.tag} lvl{self.clan_level}"
    
    def save(self, *args, **kwargs):
        self.tag = f"#{self.tag.replace('#','')}"
        if not self.discord_add:
            coc_clan = coc_client.loop.run_until_complete(get_clan_info(self.tag))
            self.name = coc_clan.name
            self.public_warlog = coc_clan.public_war_log
            self.clan_level = coc_clan.level
            self.clan_iglink = coc_clan.share_link
        super().save(*args, **kwargs)

class CocWar(models.Model):
    pass