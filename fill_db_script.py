import os
import django
import sys
from datetime import date

sys.path.append("/")
os.environ["DJANGO_SETTINGS_MODULE"] = 'vacavaca.settings'
django.setup()

from apps.vacancies import Specialty, Company, Vacancy
from apps import vacancies as data


def fill_db():
    specialties = {}
    for specialty_data in data.specialties:
        specialties[specialty_data['code']] = Specialty.objects.create(
            code=specialty_data['code'],
            title=specialty_data['title'],
        )

    companies = {}
    for company_data in data.companies:
        companies[company_data['id']] = Company.objects.create(
            name=company_data['title'],
            location=company_data['location'],
            logo=company_data['logo'],
            description=company_data['description'],
            employee_count=company_data['employee_count'],
        )

    for vacancy_data in data.jobs:
        Vacancy.objects.create(
            title=vacancy_data['title'],
            specialty=specialties[vacancy_data['specialty']],
            company=companies[vacancy_data['company']],
            skills=vacancy_data['skills'],
            description=vacancy_data['description'],
            salary_min=vacancy_data['salary_from'],
            salary_max=vacancy_data['salary_to'],
            published_at=date.fromisoformat(vacancy_data['posted']),
        )


if __name__ == '__main__':
    Vacancy.objects.all().delete()
    Specialty.objects.all().delete()
    Company.objects.all().delete()
    fill_db()
