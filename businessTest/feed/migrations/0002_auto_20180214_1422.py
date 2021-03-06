# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-14 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='network',
            old_name='likes',
            new_name='likes2',
        ),
        migrations.AddField(
            model_name='likes',
            name='mynetwork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.Network'),
        ),
    ]
