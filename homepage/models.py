from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Homepage(models.Model):

    description = RichTextField()
    updated_date = models.DateTimeField(default=datetime.now, blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.description


class Titleinformation(models.Model):

    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    org = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/homepage/%Y/%m/")
    updated_date = models.DateTimeField(default=datetime.now, blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name