# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20160614_0435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='journal',
            new_name='published_in',
        ),
        migrations.AddField(
            model_name='publication',
            name='entry_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
