from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    pessoa_foto = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.nome + ' - ' + self.endereco
    
class Funcionario(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    funcao = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    