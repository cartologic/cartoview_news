# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_auto_20170228_0547'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=b'news_updates', blank=True)),
                ('publish_date', models.DateTimeField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('publisher', models.ForeignKey(related_name='news', to=settings.AUTH_USER_MODEL)),
                ('resource', models.ForeignKey(to='base.ResourceBase')),
            ],
            options={
                'db_table': 'cartoview_news',
            },
        ),
    ]
