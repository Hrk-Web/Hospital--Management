from django.urls import path, include
from .views import Inventory

inventory = Inventory()


urlpatterns = [
    path('dashboard', inventory.dashboard, name="show"),
    path('stocks', inventory.stocks, name="stocks"),
    path('add-medicine', inventory.update_stocks, name="update_stock"),
    path('medi-list', inventory.show_medicines, name="show_medicine"),
    path('expiring-soon', inventory.expiring_list, name="exp_list"),
    path('shortage-med', inventory.shortage_list, name="shortage"),
    path('billing', inventory.billing, name="billing"),
    path('bill-history', inventory.billing_history, name="billing_history"),
    path('save-bill', inventory.save_bill, name="saving_bill"),
]
