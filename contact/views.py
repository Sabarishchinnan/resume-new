from django.shortcuts import render
from .models import Contactinformation

# Create your views here.
def contact(request):
    name = Contactinformation.objects.values_list('name', flat=True)
    phone = Contactinformation.objects.values_list('phone', flat=True)
    email = Contactinformation.objects.values_list('email', flat=True)
    field1 = Contactinformation.objects.values_list('field1', flat=True)
    field2 = Contactinformation.objects.values_list('field2', flat=True)
    field3 = Contactinformation.objects.values_list('field3', flat=True)

    data =  {
        'name' : name[0],
        'phone' : phone[0],
        'email' : email[0],
        'field1' : field1[0],
        'field2' : field2[0],
        'field3' : field3[0]
    }

    return render(request,'webpages/contact.html', data)
