from django.urls import path

from apps.accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login', views.MyLoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('signup', views.MySignupView.as_view()),
]