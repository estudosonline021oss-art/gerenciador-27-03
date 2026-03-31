from django.db import models

class Tarefa (models.Model):
    tarefa = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    descricao = models.CharField(
        max_length=500,
        null=False,
        blank=False
    )
    data = models.DateField(
        
    )
    status = models.BooleanField(
        
    )