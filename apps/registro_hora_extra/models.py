from django.db import models
from apps.funcionarios.models import Funcionario
from django.urls import reverse


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('list_registros_hora_extra')

    def __str__(self):
        return self.motivo
