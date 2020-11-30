from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    
    dests = Destination.objects.all()
   
    return render(request, 'index.html', { 'dests' : dests})
    
def indexa(request):
    return render(request, 'index-1.html')

def indexb(request):
    return render(request, 'index-2.html')

def indexc(request):
    return render(request, 'index-3.html')

def indexd(request):
    return render(request, 'index-4.html')