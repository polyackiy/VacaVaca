import logging

from django.http import HttpResponseNotFound, HttpResponse, HttpResponseForbidden
from django.db.models import Count, Prefetch
from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView

from apps.vacancies.forms import ApplicationForm
from apps.vacancies.models import Specialty, Company, Vacancy

TITLE_ALL_VACANCIES = "Все вакансии"


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialities_with_number'] = Specialty.objects.annotate(vacancy_number=Count('vacancies'))
        context['companies_with_number'] = Company.objects.annotate(vacancy_number=Count('vacancies'))
        return context


class VacanciesView(TemplateView):
    template_name = "vacancies.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = TITLE_ALL_VACANCIES
        context['vacancies'] = Vacancy.objects.all()
        return context


class VacanciesBySpecialtyView(DetailView):
    template_name = "vacancies.html"
    model = Specialty
    slug_field = 'code'
    slug_url_kwarg = 'specialty'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['vacancies'] = Vacancy.objects.filter(specialty=self.object)
        return context


class CompanyView(DetailView):
    template_name = 'company.html'
    context_object_name = 'company'
    queryset = Company.objects.prefetch_related(
        Prefetch('vacancies', queryset=Vacancy.objects.select_related('company', 'specialty'))
    )


class VacancyView(DetailView):
    template_name = 'vacancy.html'
    model = Vacancy
    context_object_name = 'vacancy'
    form_class = ApplicationForm
    queryset = Vacancy.objects.select_related('company')
    object = None

    def get_context_data(self, form=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = form or self.form_class()
        return context

    def post(self, request, pk):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        form = self.form_class(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.vacancy_id = pk
            application.save()
            return redirect('/vacancies/appsuccess')
        self.object = self.get_object()
        return self.render_to_response(self.get_context_data(form=form))


class ApplicationSuccessView(TemplateView):
    template_name = 'app-success.html'


def custom_handler404(request, exception):
    logging.warning(f'Non-existent tour was requested {exception}')
    return HttpResponseNotFound('Кажется такая страница не существует :(')


def custom_handler500(request):
    return HttpResponse('Что-то не так. \nСпециально обученный человек отправлен разобраться.', status=500)
