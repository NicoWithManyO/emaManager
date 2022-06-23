from django.contrib import admin
from .models import PossibleRoster, PossiblePlacementConf, PossibleMatchFormat, Tournament, Match

# Register your models here.
@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ['organization_owner', 'is_active', 'name', 'current_season', 'current_round', 'code_name']
    list_display_links = ['name']

@admin.register(PossibleRoster)
class PossibleRosterAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(PossiblePlacementConf)
class PossiblePlacementConfAdmin(admin.ModelAdmin):
    pass

@admin.register(PossibleMatchFormat)
class PossibleMatchFormatAdmin(admin.ModelAdmin):
    pass

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    # actions = [check_scores, generate_placement]
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