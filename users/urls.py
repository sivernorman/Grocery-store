from django.urls import path
from django.views import View
from .views import RegisterView, home, RegisterForm
urlpatterns=[
    path('users/', home, name='users-home'),
    path('register/',RegisterView.as_view(), name='users-register'),

]