# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialaggregator', '0002_auto_20160319_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aggregator',
            name='social_plugin',
            field=models.CharField(max_length=250, verbose_name='social plugin', choices=[(b'edsa_facebook_fanpage', b'Facebook Fanpage'), (b'edsa_instagram', b'Instagram'), (b'edsa_twitter', b'Twitter')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ressource',
            name='creation_date',
            field=models.DateTimeField(auto_now=True, verbose_name='creation date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ressource',
            name='social_type',
            field=models.CharField(default=b'edsa_article', max_length=250, verbose_name='social plugin', choices=[(b'edsa_article', b'Article'), (b'edsa_facebook_fanpage', b'Facebook Fanpage'), (b'edsa_instagram', b'Instagram'), (b'edsa_twitter', b'Twitter')]),
            preserve_default=True,
        ),
    ]
