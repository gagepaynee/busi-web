# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-06 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('rank', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=b'', max_length=100)),
                ('link', models.URLField(blank=True, default=b'')),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('rank', models.IntegerField(default=0)),
                ('article', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='feed.Article')),
            ],
        ),
    ]
