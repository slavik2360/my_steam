# Generated by Django 4.2.3 on 2023-07-09 04:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_alter_invitecard_expiration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.URLField(default=1, verbose_name='сылка'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invitecard',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 8, 10, 29, 7, 619888), verbose_name='дата истечения'),
        ),
    ]
