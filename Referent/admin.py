from django.contrib import admin
from .models import Referent

# Register your models here.
@admin.register(Referent)
class ReferentAdmin(admin.ModelAdmin):
    list_display = ['name', 'discriminator', 'discord_id', 'updated_at']
