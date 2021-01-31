from datetime import date

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView

from apps.vacancies.forms import VacancyForm
from apps.vacancies.models import Vacancy


class MyVacanciesView(ListView):
    template_name = 'vacancy-list.html'
    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.filter(company=self.request.user.company)
        return context


class MyVacancyBaseEditView(SuccessMessageMixin):
    model = Vacancy
    template_name = 'vacancy-edit.html'
    form_class = VacancyForm


class MyVacancyCreateView(MyVacancyBaseEditView, CreateView):
    success_message = 'Вакансия создана успешно'

    def get_success_url(self):
        return reverse_lazy('vacancies:my_vacancy_edit', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.company = self.request.user.company
        form.instance.published_at = date.today()
        return super().form_valid(form)


class MyVacancyEditView(MyVacancyBaseEditView, UpdateView):
    success_message = 'Вакансия обновлена успешно'

    def get_success_url(self):
        return reverse_lazy('vacancies:my_vacancy_edit', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        return get_object_or_404(Vacancy, pk=self.kwargs['pk'])
