# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-24 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_documentationlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentationlink',
            name='displayed',
            field=models.BooleanField(default=True),
        ),
    ]
