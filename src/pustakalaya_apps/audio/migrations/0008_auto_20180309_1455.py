# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-09 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0007_auto_20180307_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofileupload',
            name='file_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='File name'),
        ),
    ]
