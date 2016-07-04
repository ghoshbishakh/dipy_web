# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-24 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20160616_0757'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentationLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=20, unique=True)),
                ('url', models.URLField(max_length=100)),
            ],
        ),
    ]
