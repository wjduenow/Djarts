# Generated by Django 2.1.1 on 2018-09-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_gametype_rules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='last_game_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
