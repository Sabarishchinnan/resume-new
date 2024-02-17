from django.contrib import admin
from django.utils.html import format_html
from .models import Achievements, Projects

# Register your models here.
class PrjAdmin(admin.ModelAdmin):

    list_display = ('date', 'project_name',)
    search_fields = ('project_type', 'project_name')
    list_filter = ('date', 'project_type')
    list_display_links =('date', 'project_name',)

admin.site.register(Achievements)
admin.site.register(Projects, PrjAdmin)