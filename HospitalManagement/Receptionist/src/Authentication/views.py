from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import auth, User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class Authentication:

    @csrf_exempt
    @staticmethod
    def authenticate(request):
        return render(request, "login.html")

    @csrf_exempt 
    @staticmethod
    def log_in(request):
        
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return render(request, 'create.html')
            return HttpResponse("login failed")

    @csrf_exempt
    @staticmethod
    def create_user(request):
        if request.method == 'POST':
            username = request.POST['username']
            name = request.POST['name']
            number = request.POST['number']
            password = request.POST['password']

            user = User.objects.create_user(username=username, first_name=name, password=password)
            user.save()

            if user is not None:
                return HttpResponse("user created")
            
            return HttpResponse("user creation failed")


    
