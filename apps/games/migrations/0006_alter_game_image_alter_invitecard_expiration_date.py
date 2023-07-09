# Generated by Django 4.2.3 on 2023-07-09 04:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_game_image_alter_invitecard_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.URLField(max_length=1000, verbose_name='сылка'),
        ),
        migrations.AlterField(
            model_name='invitecard',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 8, 10, 58, 8, 966068), verbose_name='дата истечения'),
        ),
    ]
