from django.shortcuts import render
from .models import User

def index(request):
    
    ids = User.objects.all()
    
    return render(request, 'welcome.html', {"user":ids})