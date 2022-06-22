from django.contrib import admin
from .models import Team

from django.utils.html import format_html

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
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
