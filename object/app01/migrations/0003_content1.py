# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-18 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='content1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]