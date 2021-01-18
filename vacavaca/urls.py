"""vacavaca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from vacancies.views import IndexView, VacanciesView, VacanciesBySpecialtyView, \
    CompanyView, VacancyView, custom_handler404, custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='main'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    re_path(r'^vacancies/cat/(?P<specialty>\w+)?/$',
            VacanciesBySpecialtyView.as_view(),
            name='vacancies_by_specialty'
            ),
    re_path(r'^companies/(?P<pk>\d+)?/$', CompanyView.as_view(), name='company'),
    re_path(r'^vacancies/(?P<pk>\d+)?/$', VacancyView.as_view(), name='vacancy'),
]

handler404 = custom_handler404
handler500 = custom_handler500
