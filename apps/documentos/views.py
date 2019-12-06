from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import Documento
from django.urls import reverse_lazy

class DocumentoView():
    model = Documento
    fields = ('descricao','pertence',)

class DocumentoList(DocumentoView, ListView):
    pass

class DocumentoNovo(DocumentoView, CreateView):
    pass

class DocumentoEdit(DocumentoView, UpdateView):
    pass

class DocumentoDelete(DocumentoView, DeleteView):
    pass