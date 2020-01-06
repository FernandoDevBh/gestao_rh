from django.db import models


class Teste(models.Model):
    descricao = models.TextField()

class RegistroUsuarios(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=16,decimal_places=6)

    class Meta:
        db_table = 'registro_usuarios'