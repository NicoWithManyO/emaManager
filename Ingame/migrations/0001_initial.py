# Generated by Django 4.0.5 on 2022-06-08 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CocClan',
            fields=[
                ('tag', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=22, null=True)),
                ('public_warlog', models.BooleanField(default=False)),
                ('clan_level', models.IntegerField(default=0)),
                ('clan_iglink', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('discord_add', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
