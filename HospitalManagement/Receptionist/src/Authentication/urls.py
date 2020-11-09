from django.urls import path, include
from .views import Authentication
import inventory

allauth = Authentication()

urlpatterns = [
    path('', allauth.authenticate, name="authenticate"),
    path('login', allauth.log_in, name="login"),
    path('createuser', allauth.create_user, name="createuser"),
    path('inventory/', include("inventory.urls")),
]

# this is for fun 