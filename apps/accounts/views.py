from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

from apps.accounts.forms import MySignupForm, MyLoginForm


class MyLoginView(LoginView):
    form_class = MyLoginForm
    redirect_authenticated_user = True
    template_name = 'login.html'


class MySignupView(CreateView):
    form_class = MySignupForm
    success_url = 'login'
    template_name = 'signup.html'

    def form_valid(self, form):
        form_to_return = super().form_valid(form)
        # autologin after signup
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return form_to_return
