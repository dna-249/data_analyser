from django.shortcuts import render
from .models import User

def index(request):
    try:
        ids = User.objects.all()
    except:
        ids = [] # Fallback if table doesn't exist yet
    return render(request, 'welcome.html', {"user": ids})