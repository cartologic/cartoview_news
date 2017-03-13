# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartoview_news', '0002_remove_news_resource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='publish_date',
        ),
    ]
