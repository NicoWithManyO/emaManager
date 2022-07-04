from django.contrib import admin
from .models import PossibleMatchFormat, PossiblePlacementConf, PossibleRoster

# Register your models here.
@admin.register(PossibleRoster)
class PossibleRosterAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(PossiblePlacementConf)
class PossiblePlacementConfAdmin(admin.ModelAdmin):
    pass

@admin.register(PossibleMatchFormat)
class PossibleMatchFormatAdmin(admin.ModelAdmin):
    pass