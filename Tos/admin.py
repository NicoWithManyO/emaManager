from django.contrib import admin, messages
from .models import CurrentTos

from Tournament.models import Match
from TournamentPossibleConf.models import PossibleRoster

# Register your models here.
@admin.action(description="*!* Valider le Tos")
def valid_tos(self, request, queryset):
    for _ in queryset:
        roster = PossibleRoster.objects.filter(name=_.roster)[0]
        print(roster)
        new_match = Match(tournament=_.tournament, roster=roster, for_round=_.for_round, home=_.home, opponent=_.opponent)
        new_match.save()
        self.message_user(request, f"{new_match} add", messages.INFO)
        _.delete()

@admin.register(CurrentTos)
class CurrentTosAdmin(admin.ModelAdmin):
    actions = [valid_tos, ]