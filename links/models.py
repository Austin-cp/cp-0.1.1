#from django.conf import settings
from django.db import models


class Link(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)





