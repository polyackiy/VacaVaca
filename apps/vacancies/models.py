from django.contrib.auth.models import User
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from vacavaca.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALTY_IMAGE_DIR, DEFAULT_COMPANY_IMAGE, \
    DEFAULT_SPECIALTY_IMAGE


class Company(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=48)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR, default=DEFAULT_COMPANY_IMAGE)
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='companies')


class Specialty(models.Model):
    code = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    picture = models.ImageField(upload_to=MEDIA_SPECIALTY_IMAGE_DIR, default=DEFAULT_SPECIALTY_IMAGE)


class Vacancy(models.Model):
    title = models.CharField(max_length=128)
    specialty = models.ForeignKey(Specialty, on_delete=models.PROTECT, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=256)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField(null=True)


class Application(models.Model):
    written_username = models.CharField(max_length=128, verbose_name='Ваше имя')
    written_phone = PhoneNumberField(null=False, blank=False, unique=True, verbose_name='Ваш телефон')
    written_cover_letter = models.TextField(verbose_name='Сопроводительное письмо')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
