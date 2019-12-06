from django.urls import path
from .views import (
    DocumentoList,
    DocumentoNovo,
    DocumentoEdit,
    DocumentoDelete
)

urlpatterns = [
    path('', DocumentoList.as_view(), name='list_documentos'),
    path('novo/', DocumentoNovo.as_view(), name='create_documento'),
    path('editar/<int:pk>', DocumentoEdit.as_view(), name='update_documento'),
    path('delete/<int:pk>', DocumentoDelete.as_view(), name='delete_documento'),    
]