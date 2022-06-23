from django.db import models

# Create your models here.
class CurrentTos(models.Model):
    tournament = models.ForeignKey('Tournament.Tournament', on_delete=models.SET_NULL, null=True)
    roster = models.CharField(max_length=8, null=True, blank=True)
    for_round = models.IntegerField(default=0)
    home = models.ForeignKey('Team.Team', on_delete=models.SET_NULL, null=True)
    opponent = models.ForeignKey('Team.Team', related_name="opponent", on_delete=models.SET_NULL, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.tournament.code_name}_{self.for_round}_{self.home}_{self.opponent}"
