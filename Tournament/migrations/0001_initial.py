# Generated by Django 4.0.5 on 2022-06-08 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Organization', '0004_remove_tournament_organization_owner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PossibleMatchFormat',
            fields=[
                ('name', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('code_name', models.CharField(blank=True, max_length=164, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('team_size', models.IntegerField(blank=True, choices=[(None, None), (5, '5vs5'), (10, '10vs10'), (15, '15vs15'), (20, '20vs20'), (25, '25vs25'), (30, '30vs30'), (35, '35vs35'), (40, '40vs40'), (45, '45vs45'), (50, '50vs50')], null=True)),
                ('prep_duration', models.DurationField(blank=True, null=True)),
                ('war_duration', models.DurationField(blank=True, null=True)),
                ('attack_per_member', models.IntegerField(blank=True, choices=[(None, None), (1, '1 attaque'), (2, '2 attaques')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PossiblePlacementConf',
            fields=[
                ('name', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=132)),
                ('direct_elimination', models.BooleanField(default=False)),
                ('by_group', models.BooleanField(default=False)),
                ('play_off', models.BooleanField(default=False)),
                ('pts_for_win', models.IntegerField(default=0)),
                ('pts_for_tie', models.IntegerField(default=0)),
                ('pts_for_played', models.IntegerField(default=0)),
                ('first_critere', models.CharField(blank=True, max_length=22, null=True)),
                ('second_critere', models.CharField(blank=True, max_length=22, null=True)),
                ('three_critere', models.CharField(blank=True, max_length=22, null=True)),
                ('four_citere', models.CharField(blank=True, max_length=22, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PossibleRoster',
            fields=[
                ('name', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=132)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('code_name', models.CharField(max_length=4)),
                ('is_active', models.BooleanField(default=False)),
                ('current_season', models.IntegerField(default=0)),
                ('current_round', models.IntegerField(default=0)),
                ('banner_url', models.URLField(blank=True, null=True)),
                ('logo_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('organization_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Organization.organization')),
                ('placement_conf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tournament.possibleplacementconf')),
                ('std_match_format', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tournament.possiblematchformat')),
            ],
        ),
    ]
