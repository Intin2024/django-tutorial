from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from .models import Gravadora
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')


def create_user(request):
    if request.method=="POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('login')
    return render(request, 'registration/create.html')

def list_records(request):
    gravadoras = Gravadora.objects.all()
    return render(request, 'list_gravadoras.html', {"gravadoras": gravadoras})

def create_records(request):
    if not request.user.is_authenticated:
        # return HttpResponseNotFound("")
        return redirect('lista-gravadoras')
    if request.method=="POST":
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        gravadora = Gravadora()
        gravadora.nome = nome
        gravadora.endereco = endereco
        gravadora.save()
        return redirect('lista-gravadoras')
    return render(request, 'form_gravadoras.html')


def update_records(request, id):
    if not request.user.is_authenticated:
        # return HttpResponseNotFound("")
        return redirect('lista-gravadoras')
    gravadora = get_object_or_404(Gravadora, pk=id)
    if request.method=="POST":
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        gravadora.nome = nome
        gravadora.endereco = endereco
        gravadora.save()
        return redirect('lista-gravadoras')
    return render(request, 'form_gravadoras.html', {'gravadora': gravadora})


def remove_records(request, id):
    if not request.user.is_authenticated:
        # return HttpResponseNotFound("")
        return redirect('lista-gravadoras')
    gravadora = get_object_or_404(Gravadora, pk=id)
    gravadora.delete()
    return redirect('lista-gravadoras')