from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
import datetime
from .models import MedicineData, BillHistory

# Create your views here.
class Inventory:

    @csrf_exempt
    def dashboard(self, request):
        return render(request, 'medi.html', {})

    @csrf_exempt
    def stocks(self, request):
        return render(request, 'add.html', {})

    @csrf_exempt
    def update_stocks(self, request):
        if request.method == "POST":
            med_name = request.POST.get('medicine') 
            batch_no = request.POST.get('batch')
            mf_date = request.POST.get('mfdate')
            no_of_boxes = request.POST.get('boxes')
            exp_date = request.POST.get('exdate')
            invoice_no = request.POST.get('invoice')
            no_of_pieces = request.POST.get('pieces')
            purchase_date = request.POST.get('purchase')
  
        try:
            # saving data here
            med = MedicineData(username=request.user.username, medicine_name=med_name,
                                batch_id=batch_no, mfd=mf_date, 
                                number_of_boxes=no_of_boxes,exd=exp_date, 
                                invoice_no=invoice_no, no_of_pieces=no_of_pieces,
                                date_of_purchase=purchase_date, date_of_added=datetime.datetime.now(),
                            )
            med.save()

            if med is not None:
                # med.no_of_days_left = str(med.exd - datetime.datetime.now().date())
                # med.save()
                return render(request, 'medi.html')
        except: pass
        return HttpResponse("failed")

    @csrf_exempt
    def show_medicines(self, request):
        obj = MedicineData.objects.all().order_by('medicine_name')

        status = "staff"
        status1 = "staff1"
        if request.user.is_staff:
            status = "super"
            status1 = "super1"
        context = {
            "meds": obj,
            "status": status,
            "status1": status1,
        }
        return render(request, 'inv.html', context)

    @csrf_exempt
    def expiring_list(self, request):
        obj = MedicineData.objects.all().order_by('exd')
        for data in obj:
            data.no_of_days_left = str(data.exd - datetime.datetime.now().date())
            data.save()

        medicines = set()
        for i in obj:
            left = i.no_of_days_left 
            for j in left:
                if j == ' ':
                    p = left[0: left.index(j)]
                    if int(p) <= 50:
                        medicines.add(i)
        
        medi = list(medicines)
                

        context = {
            "meds": medi,
        }
        return render(request, 'exp.html', context)

    @csrf_exempt
    def shortage_list(self, request):
        obj = MedicineData.objects.all().order_by('no_of_pieces')

        status = "staff"
        status1 = "staff1"
        if request.user.is_staff:
            status = "super"
            status1 = "super1"
        context = {
            "meds": obj,
            "status": status,
            "status1": status1,
        }
        return render(request, 'short.html', context)
        
    @csrf_exempt
    def billing_history(self, request):
        obj = BillHistory.objects.all()
        sum = 0.0
        for i in obj:
            sum = sum + i.price

        status = "staff"
        status1 = "staff1"
        
        if request.user.is_staff:
            status = "super"
            status1 = "super1"
            
        context = {
            "bills": obj,
            "total": sum,
            "status": status,
            "status1": status1,
        }
        return render(request, 'bill_history.html', context)

    @csrf_exempt
    def billing(self, request):
        return render(request, 'bill.html')

    @csrf_exempt
    def save_bill(self, request):
        if request.method == 'POST':
            nameu = request.POST.get('names')
            mob = request.POST.get('mob')
            
            # repeated slots
            medi = request.POST.get('med')
            units = request.POST.get('unit')
            price = request.POST.get('price')

            print(nameu)
            print(mob)
            print(medi)
            print(price)
            print(units)
            print(price)



        return HttpResponse("hi")