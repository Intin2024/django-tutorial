from django.shortcuts import render
from .models import Gravadora

def home(request):
    return render(request, 'home.html')

def list_records(request):
    gravadoras = Gravadora.objects.all()
    return render(request, 'list_gravadoras.html', {"gravadoras": gravadoras})

def create_records(request):
    return render(request, 'form_gravadoras.html')