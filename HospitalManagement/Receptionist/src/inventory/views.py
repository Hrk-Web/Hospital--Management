from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class Inventory:

    @csrf_exempt
    def dashboard(self, request):
        return render(request, 'medi.html', {})

    @csrf_exempt
    def stocks(self, request):
        return render(request, 'add.html', {})