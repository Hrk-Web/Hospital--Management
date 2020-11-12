from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import auth, User
from django.views.decorators.csrf import csrf_exempt
from .models import UserMobData 

# Create your views here.
class Authentication:

    @csrf_exempt
    def authenticate(self, request):
        return render(request, "login.html")

    @csrf_exempt 
    def log_in(self, request):
        
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)

                obj = User.objects.all()
                obj1 = UserMobData.objects.all()
                context = {
                    "users": obj,
                    "mobs": obj1,
                }
                return render(request, 'create.html', context)
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

            user = User.objects.create_user(username=username, first_name=name, password=password)
            user.save()

            mob = UserMobData(user=user, mob_no=number, username=username)
            mob.save()

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

