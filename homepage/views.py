from django.shortcuts import render
from .models import Homepage, Titleinformation

# Create your views here.

def homepage(request):
    name = Titleinformation.objects.values_list('name', flat=True)
    title = Titleinformation.objects.values_list('title', flat=True)
    role = Titleinformation.objects.values_list('role', flat=True)
    org = Titleinformation.objects.values_list('org', flat=True)
    image = Titleinformation.objects.values_list('image', flat=True)

    career_description = Homepage.objects.order_by('-created_date')
    data =  {
        'name' : name[0],
        'title' : title[0],
        'role' : role[0],
        'org' : org[0],
        'image' : image[0],
        'career_description' : career_description
    }
    return render(request,'webpages/home.html', data)

