from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UpdateExcelForm
from .models import ArquivoExcel, CampanhaDoacao
from .utils import read_excel

class UploadExcelView(CreateView):
    template_name = "core/upload_excel.html"
    form_class = UpdateExcelForm
    model = ArquivoExcel

    def upload_file(request):
        if request.method == 'POST':
            form = UpdateExcelForm(request.POST, request.FILES)
            if form.is_valid():
                read_excel(request.FILES['file'])
                return HttpResponseRedirect('/success/url/')
        else:
            form = UpdateExcelForm()
        return render(request, 'upload_excel.html', {'form': form})

    def form_valid(self, form):
        pass

    def form_invalid(self, form):
        pass

    # def post(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     import ipdb; ipdb.set_trace()
    #     files = request.FILES.getlist('file')
    #     if form.is_valid():
    #
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

class CreateCampanhaView(CreateView):
    template_name = "core/create_campanha.html"
    model = CampanhaDoacao
    fields = ['data_inicio', 'data_fim']
