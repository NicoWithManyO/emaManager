from django.db import models

# Create your models here.
class Referent(models.Model):
    discord_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, blank=True)
    discriminator = models.IntegerField(blank=True)
    member_avatar = models.URLField(blank=True, null=True)

    guild = models.CharField(max_length=32, blank=True, null=True)
    joined_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}#{self.discriminator}"
