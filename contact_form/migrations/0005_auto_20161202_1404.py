# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-02 14:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    db_alias = schema_editor.connection.alias

    Site = apps.get_model("sites", "Site")
    site = Site.objects.get(pk=settings.SITE_ID)

    ContactFormSettings = apps.get_model("contact_form", "ContactFormSettings")
    ContactFormSettings.objects.using(db_alias).get_or_create(site=site)


def reverse_func(apps, schema_editor):
    # forwards_func() creates PrisonerType & InstitutionType instances,
    # so reverse_func() should delete them.
    Site = apps.get_model("sites", "Site")
    site = Site.objects.get(pk=settings.SITE_ID)

    ContactFormSettings = apps.get_model("contact_form", "ContactFormSettings")
    db_alias = schema_editor.connection.alias
    ContactFormSettings.objects.using(db_alias).get(site=site).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0004_auto_20161202_1151'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
