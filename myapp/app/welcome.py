from django.shortcuts import render
from django.core.management import call_command
from .models import User 

def index(request):
    try:
        # 1. Try to fetch users
        ids = User.objects.all()
        # Trigger a query to see if the table exists
        list(ids[:1]) 
    except Exception:
        # 2. If the table is missing, run migrate automatically
        call_command('migrate', interactive=False)
        ids = User.objects.all()
        
    return render(request, 'welcome.html', {"user": ids})