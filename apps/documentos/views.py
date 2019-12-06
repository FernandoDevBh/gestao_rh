from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import Documento
from django.urls import reverse_lazy


class DocumentoList(ListView):
    model = Documento

class DocumentoNovo(CreateView):
    model = Documento
    fields = ('descricao','pertence',)

class DocumentoEdit(UpdateView):
    model = Documento
    fields = ('descricao','pertence',)

class DocumentoDelete(DeleteView):
    model = Documento
    success_url = reverse_lazy('list_documentos')