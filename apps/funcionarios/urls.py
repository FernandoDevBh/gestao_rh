from django.urls import path
from .views import (
    Pdf,
    reportlab_view,
    FuncionariosList,
    FuncionarioEdit,
    FuncionarioDelete,
    FuncionarioNovo
)


urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('novo/', FuncionarioNovo.as_view(), name='create_funcionario'),
    path('editar/<int:pk>', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('delete/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionario'),    
    path('pdf-reportlab/', reportlab_view, name='pdf_reportlab'),
    path('pdf-xhtml2pdf/', Pdf.as_view(), name='xhtml2pdf')
]