from datetime import date

from django.contrib.auth.models import User
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from vacavaca.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALTY_IMAGE_DIR, DEFAULT_COMPANY_IMAGE, \
    DEFAULT_SPECIALTY_IMAGE


class Company(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название компаниии')
    location = models.CharField(max_length=48, verbose_name='География')
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR, default=DEFAULT_COMPANY_IMAGE, verbose_name='Логотип')
    description = models.TextField(verbose_name='Информация о компании')
    employee_count = models.IntegerField(verbose_name='Количество человек в компании')
    owner = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='company', null=True, blank=True)


class Specialty(models.Model):
    code = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    picture = models.ImageField(upload_to=MEDIA_SPECIALTY_IMAGE_DIR, default=DEFAULT_SPECIALTY_IMAGE)

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название вакансии')
    specialty = models.ForeignKey(
        Specialty, on_delete=models.PROTECT, related_name='vacancies', verbose_name='Специализация'
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=256, verbose_name='Требуемые навыки')
    description = models.TextField(verbose_name='Описание вакансии')
    salary_min = models.IntegerField(verbose_name='Зарплата от')
    salary_max = models.IntegerField(verbose_name='Зарплата до')
    published_at = models.DateField(null=True, default=date.today)


class Application(models.Model):
    written_username = models.CharField(max_length=128, verbose_name='Ваше имя')
    written_phone = PhoneNumberField(null=False, blank=False, unique=False, verbose_name='Ваш телефон')
    written_cover_letter = models.TextField(verbose_name='Сопроводительное письмо')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
