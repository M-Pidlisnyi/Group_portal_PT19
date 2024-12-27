from django.shortcuts import render
from .models import Announcment

def Announcment_list(request):
    anns = Announcment.objects.all().order_by('-created_at')
    latest_anns = anns.first() if anns.exists() else None
    return render(request, 'Announcment_app/Announcment_list.html', {'anns': anns, 'latest_anns': latest_anns})
