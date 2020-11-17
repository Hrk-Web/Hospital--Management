from django.shortcuts import render, HttpResponse, redirect, Http404
from django.contrib.auth.models import auth, User
from django.views.decorators.csrf import csrf_exempt
from .models import UserMobData 
from inventory.models import MedicineData

# Create your views here.
class Authentication:

    # login page for staff
    @csrf_exempt
    def staff_here(self, request):
        return render(request, "login1.html")

    # login page for owner
    @csrf_exempt
    def owner_here(self, request):
        return render(request, "login.html")

    @csrf_exempt
    def users_list(self, request):
        users = User.objects.all()
        mobs = UserMobData.objects.all()
        context = {
            "users": users,
            "mobs": mobs,
        }
        return render(request, "create.html", context)

    @csrf_exempt
    def home_view(self, request):
        return render(request, "home.htm")

    # login credential for staff
    @csrf_exempt
    def staff_login(self, request):
        if request.method == 'POST':
            try:
                username = request.POST['username']
                password = request.POST['password']
            except Exception as e:
                return HttpResponse(e)

            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)

                context = {

                    "status": 'staff',
                    "status1": 'staff1'
                }
                return render(request, 'medi.html', context)
            return HttpResponse("login failed")

    # login credential for owner
    @csrf_exempt 
    def owner_login(self, request):
        
        if request.method == 'POST':
            try:
                username = request.POST['username']
                password = request.POST['password']
            except Exception as e:
                return HttpResponse(e)

            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)

                if request.user.username == 'admin':

                    obj = MedicineData.objects.all().order_by('no_of_pieces')
                    medicines = MedicineData.objects.all().order_by('medicine_name')
                    short = 0
                    exp = 0
                    for i in obj:
                        if i.no_of_pieces <= 50:
                            short += 1
                        left = i.no_of_days_left 
                        for j in left:
                            if j == ' ':
                                p = left[0: left.index(j)]
                                if int(p) <= 50:
                                    exp += 1
                    
                    context = {
                        "meds": obj,
                        "total_medicine": len(medicines),
                        "status": 'super',
                        "status1": 'super1',
                        "shortage_med": short,
                        "expiring": exp/2,
                    }
                    return render(request, 'inv.html', context)
                else: 
                    return HttpResponse("Unauthorised")
            return HttpResponse("login failed")

    @csrf_exempt
    def create_user(self, request):
        if request.method == 'POST':
            try:
                username = request.POST['username']
                name = request.POST['name']
                number = request.POST['number']
                password = request.POST['password']
            except: 
                username = "not found"
                name = "not found"
                number = "not found"
                password = "not found"

            user = None
            mob = None
            try:
                user = User.objects.create_user(username=username, first_name=name, password=password)
                user.save()
            except Exception as e:
                return HttpResponse(e)

            try:
                mob = UserMobData(user=user, mob_no=number, username=username)
                mob.save()
            except Exception as e:
                return HttpResponse(e)

            if user is not None:
                if mob is not None:
                    obj = User.objects.all()
                    obj1 = UserMobData.objects.all()
                    context = {
                        "users": obj,
                        "mobs": obj1,
                    }
                    return render(request, 'create.html', context)
                else: return HttpResponse("Mobile data not saved")            
            return HttpResponse("user creation failed")

    @csrf_exempt
    def delete_user(self, request):
        if request.user.is_staff:
            return render(request, "delete.htm")
        obj = User.objects.all()
        obj1 = UserMobData.objects.all()
        context = {
            "users": obj,
            "mobs": obj1,
        }
        return render(request, 'create.html', context)
    
    @csrf_exempt
    def deleting_user(self, request):
        if request.user.is_staff:
            if request.method == 'POST':
                try:
                    username = request.POST.get('username')
                except:
                    obj = User.objects.all()
                    obj1 = UserMobData.objects.all()
                    context = {
                        "users": obj,
                        "mobs": obj1,
                    }
                    return render(request, 'create.html', context)
                try:
                    user = User.objects.get(username=username)
                    user.delete()
                    obj = User.objects.all()
                    obj1 = UserMobData.objects.all()
                    context = {
                        "users": obj,
                        "mobs": obj1,
                    }
                    return render(request, 'create.html', context)

                except:
                    obj = User.objects.all()
                    obj1 = UserMobData.objects.all()
                    context = {
                        "users": obj,
                        "mobs": obj1,
                    }
                    return render(request, 'create.html', context)





        