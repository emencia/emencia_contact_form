# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 09:22
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('civility', models.CharField(blank=True, choices=[(b'mrs', 'Mrs'), (b'mr', 'Mr')], max_length=10, verbose_name='Civility')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Last Name')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='phone')),
                ('company', models.CharField(blank=True, max_length=255, verbose_name='company')),
                ('city', models.CharField(blank=True, max_length=255, verbose_name='city')),
                ('state', models.CharField(blank=True, max_length=255, verbose_name='state/province')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='Country')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(blank=True, verbose_name='Message')),
                ('optin_newsletter', models.BooleanField(default=False, verbose_name='Do you wish to receive the newsletter?')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
