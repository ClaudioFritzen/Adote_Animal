from django.db import models

from django.contrib.auth.models import User

from .choices import ESTADOS_BRASIL
from django.forms import forms
# Create your models here.
class Raca(models.Model):
    raca = models.CharField(max_length=50)

    def __str__(self):
        return self.raca


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag
    
class Pet(models.Model):

    choices_status = (('P', 'Para Adoção'),
                        ('A', 'Adotado'))

    usuario = models.ForeignKey(User, on_delete= models.CASCADE)
    foto = models.ImageField(upload_to='fotos_pets')
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)
    tags = models.ManyToManyField(Tag)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=choices_status)


    def __str__(self):
        return self.nome
class Estados(models.Model):

    ESTADOS_BRASIL = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AM', 'Amazonas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins')
)
    estados = models.CharField(max_length=2, choices=ESTADOS_BRASIL)

    def __str__(self):
        return self.estados
    

""" class Estado(models.Model):
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=255) """

