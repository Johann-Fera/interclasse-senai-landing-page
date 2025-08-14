from django.db import models

class inscrito(models.Model):
    nome = models.CharField(max_length=50)
    curso_turma = models.CharField(max_length=100, default=" ")
    email = models.EmailField(default=" ")
    telefone = models.PositiveIntegerField(default=0)
    volei = models.BooleanField(default=False)
    futebol = models.BooleanField(default=False)
    tenis = models.BooleanField(default=False)
    time = models.BooleanField(default=False)
    nome_time = models.CharField(max_length=50, default=" ")
    quant_time = models.PositiveIntegerField(default=0)
    aapm = models.BooleanField(default=False)
    comentarios = models.TextField(default=" ")

    def __str__(self):
        return self.nome
    
