from django.contrib import admin, messages
from .models import Tournament, Match

from django.conf import settings
coc_client = settings.COC_CLIENT

from helpers.ingame_utils.ingame import get_warlog

# Register your models here.
@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ['organization_owner', 'is_active', 'name', 'current_season', 'current_round', 'code_name']
    list_display_links = ['name']

@admin.action(description="📥 Recherche les scores (warlog)")
def check_scores(self, request, queryset):
    for match in queryset:
        warlog = coc_client.loop.run_until_complete(get_warlog(match.home.active_clan.tag))
        for war in warlog:
            if war.opponent:
                print(war)
                if war.opponent.tag == match.opponent.active_clan.tag and war.end_time.raw_time[:8] == str(match.date).replace("-",""):
                    self.message_user(request, f"{match} : {war.clan.destruction} {war.clan.stars}/{war.opponent.stars} {war.opponent.destruction}", messages.INFO)
                    score = f"{war.clan.destruction} {war.clan.stars} / {war.opponent.stars} {war.opponent.destruction}"
                    match.score = score
                    match.is_ended = True
                    match.home_result = war.result
                    match.save()

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    actions = [check_scores, ]
    list_display = [
        'tournament',
        'date',
        'for_round',
        'home',
        'score',
        'opponent',
        'is_ended',
    ]
    list_filter = [
        'tournament',
        'roster',
        'for_round',
        'date',
        'is_ended',
    ]
    list_display_links = ['date', 'home', 'opponent']