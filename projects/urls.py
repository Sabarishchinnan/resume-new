from django.urls import path

from . import views

urlpatterns = [
    path('/', views.projects, name="projects"),
    path('/personal', views.personal, name='personal'),
    path('/professional', views.professional, name='professional'),
    path('/achievements', views.achievements, name='achievements'),
]