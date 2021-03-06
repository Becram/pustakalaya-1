# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-07 10:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0005_auto_20180306_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='education_levels',
            field=models.ManyToManyField(blank=True, null=True, to='core.EducationLevel', verbose_name='Education Levels'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='keywords',
            field=models.ManyToManyField(blank=True, null=True, to='core.Keyword', verbose_name='Select list of keywords'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Publisher', verbose_name='Audio publisher'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='sponsors',
            field=models.ManyToManyField(blank=True, null=True, to='core.Sponsor', verbose_name='Sponsor'),
        ),
    ]
