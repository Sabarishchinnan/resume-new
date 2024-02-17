from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Achievements(models.Model):
    description = RichTextField()
    updated_date = models.DateTimeField(default=datetime.now, blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.description


class Projects(models.Model):

    project_choices = (
        ('Personal', 'Personal'),
        ('Professional', 'Professional')
    )

    date = models.CharField(max_length=10)
    project_type = models.CharField(choices=project_choices,max_length=20)
    project_name = RichTextField()
    description = RichTextField()
    tech_stack = RichTextField()
    updated_date = models.DateTimeField(default=datetime.now, blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.project_type

