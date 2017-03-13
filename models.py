from django.conf import settings
from django.db import models
from geonode.base.models import ResourceBase


class News(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="news_updates")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    publisher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='news')

    class Meta:
        db_table = 'cartoview_news'
