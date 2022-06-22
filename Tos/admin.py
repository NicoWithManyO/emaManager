from django.contrib import admin
from .models import CurrentTos

# Register your models here.
@admin.register(CurrentTos)
class CurrentTosAdmin(admin.ModelAdmin):
    pass