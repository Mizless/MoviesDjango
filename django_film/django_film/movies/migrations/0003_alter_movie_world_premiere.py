# Generated by Django 4.2.7 on 2023-12-01 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_world_premiere'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='world_premiere',
            field=models.DateField(default=datetime.date(2023, 12, 1), verbose_name='Премьера в мире'),
        ),
    ]
