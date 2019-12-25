import csv
import xlwt

from django.views import View
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)
from .models import RegistroHoraExtra
from django.urls import reverse_lazy
from .forms import RegistroHoraExtraForm
from django.http import HttpResponse
import json


class RegistroHoraExtraList(ListView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa)

class RegistroHoraExtraNovo(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(RegistroHoraExtraNovo, self).get_form_kwargs()
        kwargs.update({ 'user': self.request.user })
        return kwargs

class RegistroHoraExtraEditBase(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(RegistroHoraExtraEditBase, self).get_form_kwargs()
        kwargs.update({ 'user': self.request.user })
        return kwargs

class RegistroHoraExtraEdit(RegistroHoraExtraEditBase):
    def get_success_url(self):
        return reverse_lazy('update_registros_hora_extra', args=[self.object.id])        

class CompensarHoraExtra(View):
    def compensarHoras(self, id, compensar):
        registro = RegistroHoraExtra.objects.get(id=id)
        registro.compensar = bool(int(compensar))
        registro.save()
        return float(registro.funcionario.total_horas_extra)

    def post(self, request, *args, **kwargs):
        response = json.dumps({ 
            'mensagem': 'Requisição Executada',
            'horas': self.compensarHoras(kwargs['pk'], request.POST.get('compensar'))
        })
        return HttpResponse(response, content_type='application/json')

class RegistroHoraExtraEditFuncionario(RegistroHoraExtraEditBase):
    pass

class RegistroHoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_registros_hora_extra')

class ExportarCsv(View):
    def get(self, request, *args, **kwargs):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        response.write(u'\ufeff'.encode('utf8'))
        empresa = self.request.user.funcionario.empresa
        registro_hora_extra = RegistroHoraExtra.objects.filter(funcionario__empresa=empresa)

        writer = csv.writer(response)
        writer.writerow(['Id', 'Motivo', 'Funcionário', 'Horas', 'Utilizado'])
        for r in registro_hora_extra:            
            writer.writerow([r.id, r.funcionario, r.horas, r.compensar])

        return response

class ExportarExcel(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="user.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users')

        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id', 'Motivo', 'Funcionário', 'Rest. Func', 'Horas']

        for col_pos in range(len(columns)):
            ws.write(row_num, col_pos, columns[col_pos], font_style)

        font_style = xlwt.XFStyle()
        empresa = self.request.user.funcionario.empresa

        registros = RegistroHoraExtra.objects.filter(
            compensar=False,
            funcionario__empresa=empresa
            )
        
        row_num = 1

        for r in registros:
            ws.write(row_num, 0, r.id, font_style)
            ws.write(row_num, 1, r.motivo, font_style)
            ws.write(row_num, 2, r.funcionario.nome, font_style)
            ws.write(row_num, 3, r.funcionario.total_horas_extra, font_style)
            ws.write(row_num, 4, r.horas, font_style)
            row_num += 1

        wb.save(response)

        return response