from django.contrib import admin
from .models import MedicineData, BillHistory

# Register your models here.
admin.site.register(MedicineData)
admin.site.register(BillHistory)