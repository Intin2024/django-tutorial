from django.shortcuts import render, redirect
from .models import Gravadora

def home(request):
    return render(request, 'home.html')

def list_records(request):
    gravadoras = Gravadora.objects.all()
    return render(request, 'list_gravadoras.html', {"gravadoras": gravadoras})

def create_records(request):
    if request.method=="POST":
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        gravadora = Gravadora()
        gravadora.nome = nome
        gravadora.endereco = endereco
        gravadora.save()
        return redirect('lista-gravadoras')
    return render(request, 'form_gravadoras.html')