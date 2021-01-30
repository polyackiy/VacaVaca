from django.urls import path, re_path

from apps.vacancies.views import public, mycompany, myvacancies

app_name = 'vacancies'

urlpatterns = [
    path('', public.IndexView.as_view(), name='index'),
    path('vacancies/', public.VacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<slug:specialty>',
         public.VacanciesBySpecialtyView.as_view(),
         name='vacancies_by_specialty'
         ),
    path('companies/<int:pk>', public.CompanyView.as_view(), name='company'),
    path('vacancies/<int:pk>', public.VacancyView.as_view(), name='vacancy'),
    path('vacancies/appsuccess', public.ApplicationSuccessView.as_view(), name='app_success'),

    path('mycompany/letsstart/', mycompany.MyCompanyLetsStart.as_view(), name='my_company_lets_start'),
    path('mycompany/create/', mycompany.MyCompanyCreateView.as_view(), name='my_company_create'),
    path('mycompany/', mycompany.MyCompanyEditView.as_view(), name='my_company'),

    path('mycompany/vacancies/', myvacancies.MyVacancies.as_view(), name='my_vacancies'),
    path('mycompany/vacancies/create/', myvacancies.MyVacancyCreate.as_view(), name='my_vacancy_create'),
    path('mycompany/vacancies/create/', myvacancies.MyVacancyEdit.as_view(), name='my_vacancy_edit'),
]
