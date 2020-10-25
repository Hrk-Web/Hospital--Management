from django.urls import path
from .views import Authentication

urlpatterns = [
    path('', Authentication.authenticate, name="authenticate"),
    path('login', Authentication.logIn, name="login"),
]
