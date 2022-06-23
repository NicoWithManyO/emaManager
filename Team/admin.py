from django.contrib import admin, messages
from .models import Team

from Tos.models import CurrentTos
from helpers.tournament_utils.tournament import simple_tos, save_tos

from django.utils.html import format_html

# Register your models here.
@admin.action(description="🧤 Tirage au sort avec la sélection")
def tos(self, request, queryset):
    roster = ""
    for _ in queryset:
        roster = _.roster
        if not _.is_staff_validated:
            self.message_user(request, f"{_} n'est pas validée !", messages.ERROR)
            return
    for _ in CurrentTos.objects.all():
        if _.roster == roster:
            self.message_user(request, f"Un Tos pour {roster} est déjà présent", messages.ERROR)
            return
    self.message_user(request, f"{len(queryset)} équipes sélectionées pour le tirage", messages.INFO)
    all_matchs = simple_tos(queryset)

    if not all_matchs:
        self.message_user(request, f"error", messages.ERROR)
        return
    
    temp = []
    print(all_matchs)

    for _ in all_matchs:
        if len(_) > 1:
            temp.append(f"{_[0].name} vs {_[1].name}")
        else:
            temp.append(f"{_[0].name} exempt")
    o = ' | '.join(temp)
    self.message_user(request, f"{len(all_matchs)} matchs\n{o}", messages.INFO)
    save_tos(all_matchs)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    actions = [tos, ]
    list_display = [
        'tournament',
        'registered_for_round',
        'roster',
        'id',
        'is_staff_validated',
        'name',
        'clan',
        'referent_owner',
        'second_referent',
    ]
    list_display_links = ['name']
    
    def clan(self, obj):
        if obj.active_clan:
            return format_html(f"<a href='{obj.active_clan.clan_iglink}'>{obj.active_clan.tag}</a> ({obj.active_clan.name})")
