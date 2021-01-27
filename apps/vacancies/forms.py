from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm, Textarea

from apps.vacancies.models import Application, Company


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


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'employee_count', 'logo', 'location', 'description']
        widgets = {
            'description': Textarea(attrs={'rows': 8, }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))
