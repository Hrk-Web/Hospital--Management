from django.urls import path
from .views import Authentication

urlpatterns = [
    path('', Authentication.authenticate, name="authenticate"),
    path('login', Authentication.log_in, name="login"),
    path('createuser', Authentication.create_user, name="createuser"),
    
]
