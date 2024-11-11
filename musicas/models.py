from django.db import models

class Gravadora(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.TextField()

class Musica(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    is_single = models.BooleanField()
    gravadora = models.ForeignKey(Gravadora, on_delete=models.CASCADE, blank=True, null=True)

