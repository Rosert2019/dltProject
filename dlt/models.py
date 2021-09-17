from django.db import models
from django.utils.timezone import now

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=60, unique=True)
    update_date = models.DateTimeField(default=now)
    bodytext = models.TextField('Page Content', blank=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=60)
    git_link = models.CharField(max_length=60, unique=True)
    productionn_link = models.CharField(max_length=60, unique=True)
    created_at = models.DateTimeField(default=now)
    description = models.TextField('Page Content', blank=True)

    def __str__(self):
        return self.name       