# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-03 21:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_auto_20170903_2103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infographic',
            options={'ordering': ('infographic__pub_date', 'infographic__title')},
        ),
        migrations.AlterModelOptions(
            name='metainfographic',
            options={'ordering': ('pub_date', 'title')},
        ),
        migrations.RemoveField(
            model_name='infographic',
            name='active',
        ),
        migrations.RemoveField(
            model_name='infographic',
            name='ad',
        ),
        migrations.RemoveField(
            model_name='infographic',
            name='description',
        ),
        migrations.RemoveField(
            model_name='infographic',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='infographic',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='infographic',
            name='sponsored',
        ),
        migrations.RemoveField(
            model_name='infographic',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='infographic',
            name='title',
        ),
        migrations.RemoveField(
            model_name='metainfographic',
            name='high_def_url',
        ),
        migrations.RemoveField(
            model_name='metainfographic',
            name='infographic',
        ),
        migrations.RemoveField(
            model_name='metainfographic',
            name='lang',
        ),
        migrations.RemoveField(
            model_name='metainfographic',
            name='medium_img',
        ),
        migrations.RemoveField(
            model_name='metainfographic',
            name='thumbnail_img',
        ),
        migrations.AddField(
            model_name='infographic',
            name='high_def_url',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='URL to high definition infographic'),
        ),
        migrations.AddField(
            model_name='infographic',
            name='lang',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Language code'),
        ),
        migrations.AddField(
            model_name='infographic',
            name='medium_img',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='', verbose_name='Medium image'),
        ),
        migrations.AddField(
            model_name='infographic',
            name='meta_infographic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='public.MetaInfographic'),
        ),
        migrations.AddField(
            model_name='infographic',
            name='thumbnail_img',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='', verbose_name='Thumbnail'),
        ),
        migrations.AddField(
            model_name='metainfographic',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='metainfographic',
            name='ad',
            field=models.BooleanField(default=False, verbose_name='Ad'),
        ),
        migrations.AddField(
            model_name='metainfographic',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='metainfographic',
            name='pub_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Publication date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metainfographic',
            name='slug',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='metainfographic',
            name='sponsored',
            field=models.BooleanField(default=False, verbose_name='Sponsored'),
        ),
        migrations.AddField(
            model_name='metainfographic',
            name='tags',
            field=models.ManyToManyField(to='public.Tag'),
        ),
        migrations.AddField(
            model_name='metainfographic',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Title'),
        ),
    ]