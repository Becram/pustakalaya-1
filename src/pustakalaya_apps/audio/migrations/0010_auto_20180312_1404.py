# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-12 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0009_audio_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='license_type',
            field=models.CharField(blank=True, max_length=255, verbose_name='License type'),
        ),
    ]
