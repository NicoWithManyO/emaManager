from django.db import models
from django.utils.text import slugify


# Create your models here.
class Team(models.Model):
    ROSTERS_CHOICES = [
        (None, None),
        ('Mixt', 'Mixt'),
        ('Full', 'Full'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True, blank=True)
    roster = models.CharField(max_length=6, choices=ROSTERS_CHOICES, default=None)
    tournament = models.ForeignKey('Tournament.Tournament', on_delete=models.SET_NULL, null=True, blank=True)
    
    active_clan = models.ForeignKey('Ingame.CocClan', on_delete=models.SET_NULL, null=True, blank=True)

    registered_for_round = models.IntegerField(default=0, null=True, blank=True)

    referent_owner = models.ForeignKey('Referent.Referent', on_delete=models.SET_NULL, null=True, blank=True)
    second_referent = models.ForeignKey('Referent.Referent', related_name="second_referent", on_delete=models.SET_NULL, null=True, blank=True)

    is_staff_validated = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)
    blason_url = models.URLField(null=True, blank=True)

    played_matchs = models.CharField(max_length=36, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.id}. {self.name} {self.roster}"

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.tournament.code_name}_{self.name}_{self.roster}")
        super().save(*args, **kwargs)
