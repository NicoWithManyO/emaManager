# Generated by Django 4.0.5 on 2022-06-08 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0003_possiblematchformat_tournament_std_match_format'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='organization_owner',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='std_match_format',
        ),
        migrations.DeleteModel(
            name='PossibleMatchFormat',
        ),
        migrations.DeleteModel(
            name='Tournament',
        ),
    ]
