# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('socialaggregator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ressource',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 19, 7, 16, 46, 945009), verbose_name='creation date', editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ressource',
            name='image',
            field=filer.fields.image.FilerImageField(default=None, to='filer.Image', max_length=255, blank=True, null=True, verbose_name='image'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ressource',
            name='thumbnail',
            field=filer.fields.image.FilerImageField(related_name='+', default=None, to='filer.Image', max_length=255, blank=True, null=True, verbose_name='thumbnail'),
            preserve_default=True,
        ),
    ]
