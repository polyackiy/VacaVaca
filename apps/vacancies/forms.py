from string import Template

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import ModelForm, Textarea
from django.utils.safestring import mark_safe

from apps.vacancies.models import Application, Company, Vacancy
from vacavaca.settings import MEDIA_URL


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']
        widgets = {
            'written_cover_letter': Textarea(attrs={'rows': 8, }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Записаться на собеседование'))


class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        html = Template("""<img style="max-width: 120px;height: auto;" src="$media$link"/>""")
        return mark_safe(html.substitute(media=MEDIA_URL, link=value))


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'employee_count', 'logo', 'location', 'description']
        widgets = {
            'description': Textarea(attrs={'rows': 8, }),
            'logo': PictureWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить', css_class='btn-info'))


class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'specialty', 'skills', 'description', 'salary_min', 'salary_max']
        widgets = {
            'description': Textarea(attrs={'rows': 16, }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить', css_class='btn-info'))
