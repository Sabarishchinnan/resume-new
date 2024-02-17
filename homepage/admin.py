from django.contrib import admin
from django.utils.html import format_html

from .models import Homepage, Titleinformation
# Register your models here.

admin.site.register(Homepage)
admin.site.register(Titleinformation)