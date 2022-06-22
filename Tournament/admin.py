from django.contrib import admin
from .models import PossibleRoster, PossiblePlacementConf, PossibleMatchFormat, Tournament

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