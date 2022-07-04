from django.db import models
from django.utils.text import slugify

# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    code_name = models.CharField(max_length=4)
    organization_owner = models.ForeignKey('Organization.Organization', on_delete=models.SET_NULL, null=True, blank=True)

    is_active = models.BooleanField(default=False)
    
    on_registration = models.BooleanField(default=True)
    
    std_roster = models.ManyToManyField('TournamentPossibleConf.PossibleRoster', blank=True)
    std_match_format = models.ForeignKey('TournamentPossibleConf.PossibleMatchFormat', on_delete=models.SET_NULL, null=True, blank=True)
    placement_conf = models.ForeignKey('TournamentPossibleConf.PossiblePlacementConf', on_delete=models.SET_NULL, null=True, blank=True)

    current_season = models.IntegerField(default=0)
    current_round = models.IntegerField(default=0)

    banner_url = models.URLField(blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)
    associated_color = models.CharField(max_length=12, null=True, blank=True)
    
    tracking_file = models.URLField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class Match(models.Model):
    RESULT_CHOICES = [
        ('win', "Win"),
        ('lose', 'Lose'),
        ('tie', 'Tie'),
    ]
    tournament = models.ForeignKey('Tournament', on_delete=models.SET_NULL, null=True, blank=True)
    roster = models.ForeignKey('TournamentPossibleConf.PossibleRoster', on_delete=models.SET_NULL, null=True, blank=True)
    for_round = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)
    
    home = models.ForeignKey('Team.Team', on_delete=models.SET_NULL, null=True)
    opponent = models.ForeignKey('Team.Team', related_name="opp", on_delete=models.SET_NULL, null=True, blank=True)

    date = models.DateField(blank=True, null=True)
    negociated_date = models.DateField(blank=True, null=True)

    is_ended = models.BooleanField(default=False)
    score = models.CharField(max_length=122, null=True, blank=True)
    home_result = models.CharField(max_length=5, choices=RESULT_CHOICES, null=True, blank=True)
    opponent_result = models.CharField(max_length=5, choices=RESULT_CHOICES, null=True, blank=True)

    is_exempt = models.BooleanField(default=False)
    home_forfeit = models.BooleanField(default=False)
    opponent_forfeit = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def save(self, *args, **kwargs):
        if not self.opponent:
            self.is_exempt = True
            self.home_result = "win"
            self.is_ended = True
        self.slug = slugify(f"{self.tournament.code_name}_{self.roster}_{self.home}_{self.opponent}_{self.for_round}")
        super().save(*args, **kwargs)