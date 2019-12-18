from django.urls import path
from .views import (
    RegistroHoraExtraList,
    RegistroHoraExtraNovo,
    RegistroHoraExtraEdit,
    RegistroHoraExtraEditFuncionario,
    RegistroHoraExtraDelete
)

urlpatterns = [
    path(
        '',
        RegistroHoraExtraList.as_view(),
        name='list_registros_hora_extra'
    ),
    path(
        'novo/',
        RegistroHoraExtraNovo.as_view(),
        name='create_registros_hora_extra'
    ),
    path(
        'editar/<int:pk>', 
        RegistroHoraExtraEdit.as_view(), 
        name='update_registros_hora_extra'
    ),
    path(
        'editar-funcionario/<int:pk>', 
        RegistroHoraExtraEditFuncionario.as_view(), 
        name='update_registros_hora_extra_funcionario'
    ),
    path(
        'delete/<int:pk>', 
        RegistroHoraExtraDelete.as_view(),
        name='delete_registros_hora_extra'
    ),
]