# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-03 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infographic',
            name='visible',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='infographics',
        ),
        migrations.AddField(
            model_name='infographic',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='infographic',
            name='tags',
            field=models.ManyToManyField(to='public.Tag'),
        ),
    ]