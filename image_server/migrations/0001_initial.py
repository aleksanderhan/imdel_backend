# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.FileField(upload_to='uploaded_images')),
                ('text', models.CharField(blank=True, max_length=200)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
    ]
