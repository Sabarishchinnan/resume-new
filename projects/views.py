from django.shortcuts import render
from .models import Achievements, Projects

# Create your views here.
def projects(request):
    personal_project_list = Projects.objects.filter(project_type='Personal').order_by('-date')
    data =  {
        'personal_project_list' : personal_project_list
    }
    return render(request,'webpages/projects.html',data)


def personal(request):
    personal_project_list = Projects.objects.filter(project_type='Personal').order_by('-date')
    data =  {
        'personal_project_list' : personal_project_list
    }
    return render(request,'webpages/personal.html',data)


def professional(request):
    professional_project_list = Projects.objects.filter(project_type='Professional').order_by('-date')
    data =  {
        'professional_project_list' : professional_project_list
    }
    return render(request,'webpages/professional.html',data)


def achievements(request):
    achievements_list = Achievements.objects.order_by('-created_date')
    data =  {
        'achievements_list' : achievements_list
    }
    return render(request,'webpages/achievements.html', data)