# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 14:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body_markdown', models.TextField()),
                ('body_html', models.TextField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('website_position_id', models.CharField(db_index=True, max_length=100, null=True, unique=True)),
                ('website_page', models.CharField(choices=[('home', 'Home')], max_length=100)),
            ],
            options={
                'permissions': (('view_section', 'Can see available sections'), ('edit_section', 'Can edit available sections')),
            },
        ),
    ]
