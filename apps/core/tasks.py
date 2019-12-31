# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.core.mail import send_mail
from apps.funcionarios.models import Funcionario
from django.conf import settings


@shared_task
def add(x, y):
    return x + y

@shared_task
def send_relatorio():
    total = Funcionario.objects.all().count()
    send_mail(
        'Relatório Celery',
        'Relatorio geral de funcionarios %f.' %total,
        settings.EMAIL_HOST_USER,
        ['fsffernando@hotmail.com'],
        fail_silently=False,
    )
    return True

@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)