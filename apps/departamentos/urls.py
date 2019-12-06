from django.urls import path
from .views import (
    DepartamentoList,
    DepartamentoNovo,
    DepartamentoEdit,
    DepartamentoDelete
)

urlpatterns = [
    path('', DepartamentoList.as_view(), name='list_departamentos'),
    path('novo/', DepartamentoNovo.as_view(), name='create_departamento'),
    path('editar/<int:pk>', DepartamentoEdit.as_view(), name='update_departamento'),
    path('delete/<int:pk>', DepartamentoDelete.as_view(), name='delete_departamento'),    
]