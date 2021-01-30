from django.views.generic import CreateView, UpdateView, ListView

from apps.vacancies.models import Vacancy


class MyVacancies(ListView):
    template_name = 'vacancy-list.html'
    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.filter(company=self.request.user.company)
        return context


class MyVacancyCreate(CreateView):
    pass


class MyVacancyEdit(UpdateView):
    pass
