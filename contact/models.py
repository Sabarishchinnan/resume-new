from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Contactinformation(models.Model):

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    field1 = models.CharField(max_length=255, blank=True)
    field2 = models.CharField(max_length=255, blank=True)
    field3 = models.CharField(max_length=255, blank=True)
    field4 = models.CharField(max_length=255, blank=True)
    field5 = models.CharField(max_length=255, blank=True)
    field6 = models.CharField(max_length=255, blank=True)
    field7 = models.CharField(max_length=255, blank=True)
    field8 = models.CharField(max_length=255, blank=True)
    updated_date = models.DateTimeField(default=datetime.now, blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name