from django.urls import path, include
from .views import Authentication
import inventory

allauth = Authentication()
urlpatterns = [
    path('', allauth.owner_here, name="owner_here"),
    path('staff-here', allauth.staff_here, name="staff_here"),
    path('login', allauth.owner_login, name="login"),
    path('staff-login', allauth.staff_login, name="staff_login"),
    path('createuser', allauth.create_user, name="createuser"),
    path('inventory/', include("inventory.urls")),
    path('users-list', allauth.users_list, name="users"),
]

# this is for fun 