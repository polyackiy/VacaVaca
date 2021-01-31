# Generated by Django 3.1.5 on 2021-01-30 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies', '0007_auto_20210130_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(verbose_name='Описание вакансии'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_max',
            field=models.IntegerField(verbose_name='Зарплата до'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_min',
            field=models.IntegerField(verbose_name='Зарплата от'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='skills',
            field=models.CharField(max_length=256, verbose_name='Требуемые навыки'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vacancies', to='vacancies.specialty', verbose_name='Специализация'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Название вакансии'),
        ),
    ]