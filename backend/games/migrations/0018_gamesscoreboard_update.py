# Generated by Django 3.2.12 on 2024-07-29 17:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0017_gamesscoreboard_played_games'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamesscoreboard',
            name='update',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]