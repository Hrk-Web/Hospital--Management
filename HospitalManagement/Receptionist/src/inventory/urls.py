from django.urls import path, include
from .views import Inventory

inventory = Inventory()


urlpatterns = [
    path('dashboard', inventory.dashboard, name="show"),
    path('stocks', inventory.stocks, name="stocks"),
]
