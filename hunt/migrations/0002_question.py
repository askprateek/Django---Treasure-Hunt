# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField()),
                ('text', models.TextField()),
                ('answer', models.CharField(max_length=50)),
            ],
        ),
    ]
