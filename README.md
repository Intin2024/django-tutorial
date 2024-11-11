# Django

## Criar projeto
- Criar pasta vazia
- Criar ambiente virtual
```
python3 -m venv venv
```
- Ativar ambiente virtual
```
source venv/bin/activate
```

- Atualizar o pip
```
pip install --upgrade pip
```
- Instale a dependência do Django
```
pip install Django
```
- Inicializar aplicação
```
django-admin startproject meusite .
```
- Executar o servidor
```
python3 manage.py runserver
```
- Aplicar migrations
```
python3 manage.py migrate
```
- Criar super-usuário
```
python3 manage.py createsuperuser
```

## Criar app
- Criar um novo app
```
python3 manage.py startapp musicas
```
- Modificar `INSTALLED_APPS` no arquivo `settings.py` para ter o aplicativo instalado ao fim da lista.
- Modificar o arquivo `models.py` para incluir os objetos da aplicação
- Criar a migration desta primeira modificação
```
python3 manage.py makemigrations
```
- Aplicar a migration desta primeira modificação
```
python3 manage.py migrate
```
- Registrar no site do admin, no arquivo `admin.py`
```python3
admin.site.register(Modelo)
```

## Criar páginas
- Criar pasta `templates` dentro do app
- Adicionar página html à pasta
- Criar função de view no arquivo `views.py`
```python3
def home(request):
    return render(request, 'home.html')
```
- Criar arquivo `urls.py` no app
```python3
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')
]
```
- Modificar a lista urlpatterns do arquivo `urls.py` do site
```python3
from django.contrib import admin
from django.urls import path, include # adiciona include à importação

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('musicas.urls')) # importa urls do app
]
```