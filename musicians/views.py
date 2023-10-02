# musicians/views.py
from django.shortcuts import render
from .models import Musician

def home(request):
    return render(request, 'musicians/home.html')

def musician_list(request):
    musicians = Musician.objects.all()
    return render(request, 'musicians/musician_list.html', {'musicians': musicians})

def musician_detail(request, musician_id):
    musician = Musician.objects.get(id=musician_id)
    return render(request, 'musicians/musician_detail.html', {'musician': musician})
