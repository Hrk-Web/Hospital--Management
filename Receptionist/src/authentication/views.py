from django.shortcuts import render, HttpResponse, redirect, Http404
from django.contrib.auth.models import auth, User
from django.views.decorators.csrf import csrf_exempt
from .models import UserMobData 

# Create your views here.
class Authentication:

    @csrf_exempt
    def staff_here(self, request):
        return render(request, "login1.html")

    @csrf_exempt
    def home_view(self, request):
        return render(request, "home.htm")

    @csrf_exempt
    def authenticate(self, request):
        return render(request, "login.html")

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

                obj = User.objects.all()
                obj1 = UserMobData.objects.all()
                context = {
                    "users": obj,
                    "mobs": obj1,
                }
                return render(request, 'medi1.html', context)

            return HttpResponse("login failed")

    @csrf_exempt 
    def log_in(self, request):
        
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
                    print('hritik')
                    obj = User.objects.all()
                    obj1 = UserMobData.objects.all()
                    context = {
                        "users": obj,
                        "mobs": obj1,
                    }
                    return render(request, 'create.html', context)
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

