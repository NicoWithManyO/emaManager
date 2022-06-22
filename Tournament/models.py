from django.db import models
from django.utils.text import slugify

# Create your models here.
class PossibleRoster(models.Model):
    name = models.CharField(max_length=16, primary_key=True)
    description = models.CharField(max_length=132, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class PossiblePlacementConf(models.Model):
    name = models.CharField(max_length=16, primary_key=True)
    description = models.CharField(max_length=132, blank=True)

    direct_elimination = models.BooleanField(default=False)
    by_group = models.BooleanField(default=False)
    play_off = models.BooleanField(default=False)
    
    pts_for_win = models.IntegerField(default=0)
    pts_for_tie = models.IntegerField(default=0)
    pts_for_played = models.IntegerField(default=0)

    first_critere = models.CharField(max_length=22, blank=True, null=True)
    second_critere = models.CharField(max_length=22, blank=True, null=True)
    three_critere = models.CharField(max_length=22, blank=True, null=True)
    four_citere = models.CharField(max_length=22, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class PossibleMatchFormat(models.Model):
    ATTACKS_CHOICES = [
        (None, None),
        (1, '1 attaque'),
        (2, '2 attaques'),
    ]
    TEAM_SIZES_CHOICES = [
        (None, None),
        (5, '5vs5'),
        (10, '10vs10'),
        (15, '15vs15'),
        (20, '20vs20'),
        (25, '25vs25'),
        (30, '30vs30'),
        (35, '35vs35'),
        (40, '40vs40'),
        (45, '45vs45'),
        (50, '50vs50'),
    ]

    name = models.CharField(max_length=16, primary_key=True)
    code_name = models.CharField(max_length=164, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    team_size = models.IntegerField(blank=True, null=True, choices=TEAM_SIZES_CHOICES)
    prep_duration = models.DurationField(blank=True, null=True)
    war_duration = models.DurationField(blank=True, null=True)
    attack_per_member = models.IntegerField(choices=ATTACKS_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.code_name}"
        
    def save(self, *args, **kwargs):
        self.code_name = f"{self.team_size}/{self.prep_duration}/{self.war_duration}/{self.attack_per_member}"
        self.slug = slugify(f"{self.name}_{self.team_size}_{self.prep_duration}_{self.war_duration}_{self.attack_per_member}")
        super().save(*args, **kwargs)


class Tournament(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    code_name = models.CharField(max_length=4)
    organization_owner = models.ForeignKey('Organization.Organization', on_delete=models.SET_NULL, null=True, blank=True)

    is_active = models.BooleanField(default=False)
    
    on_registration = models.BooleanField(default=True)
    
    std_roster = models.ManyToManyField('PossibleRoster', blank=True)
    std_match_format = models.ForeignKey('PossibleMatchFormat', on_delete=models.SET_NULL, null=True, blank=True)
    placement_conf = models.ForeignKey('PossiblePlacementConf', on_delete=models.SET_NULL, null=True, blank=True)

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

