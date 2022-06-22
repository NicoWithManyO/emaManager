from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    code_name = models.CharField(max_length=4)

    discord_staff_members = models.ManyToManyField('Referent.Referent', blank=True)

    discord_server_id = models.IntegerField(default=0)
    discord_server_invit = models.URLField(blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
