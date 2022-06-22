# Generated by Django 4.0.5 on 2022-06-08 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Referent', '0001_initial'),
        ('Organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='discord_staff_members',
            field=models.ManyToManyField(blank=True, to='Referent.referent'),
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
            ],
        ),
    ]