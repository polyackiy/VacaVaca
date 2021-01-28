from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login', views.MyLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', views.MySignupView.as_view(), name='signup'),
]