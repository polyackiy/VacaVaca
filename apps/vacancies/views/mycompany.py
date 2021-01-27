from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView

from apps.vacancies.forms import CompanyForm
from apps.vacancies.models import Company


class MyCompanyLetsStart(TemplateView):
    template_name = 'company-lets-start.html'


class MyCompanyBaseEditView(SuccessMessageMixin):
    model = Company
    template_name = 'company-edit.html'
    form_class = CompanyForm
    success_url = reverse_lazy('vacancies:company')


class MyCompanyCreateView(MyCompanyBaseEditView, CreateView):
    success_message = 'Компания создана успешно'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MyCompanyEditView(MyCompanyBaseEditView, UpdateView):
    success_message = 'Информация о компании обновлена успешно'

    def get_object(self, queryset=None):
        return self.request.user.company

