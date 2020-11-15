from django.urls import path, include
from .views import Authentication
import inventory

allauth = Authentication()

urlpatterns = [
    path('', allauth.authenticate, name="authenticate"),
    path('staff-here', allauth.staff_here, name="staff_here"),
    path('login', allauth.log_in, name="login"),
    path('staff-login', allauth.staff_login, name="staff_login"),
    path('createuser', allauth.create_user, name="createuser"),
    path('inventory/', include("inventory.urls")),
]

# this is for fun 