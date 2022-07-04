from django.contrib import admin
from .models import CocClan, CocWar

from django.utils.html import format_html

# Register your models here.
# @admin.action(description="Vérifier l'état du warlog du clan")
# def check_warlog(self, request, queryset):
#     for _ in queryset:
#         coc_clan = coc_client.loop.run_until_complete(clan_info(_.tag))
#         _.public_warlog = coc_clan.public_war_log
#         _.save()
#         if not coc_clan.public_war_log:
#             self.message_user(request, f"{_} NOK !", messages.ERROR)
#         else:
#             pass

@admin.register(CocWar)
class CocWarAdmin(admin.ModelAdmin):
    pass

@admin.register(CocClan)
class CocClanAdmin(admin.ModelAdmin):

    list_display = ['public_warlog', 'name', 'clan_tag', 'clan_level']
    list_display_links = ['name']
    # actions = [check_warlog, ]

    def clan_tag(self, obj):
        return format_html(f"<a href='{0}'>{obj.tag}</a>", obj.clan_iglink)