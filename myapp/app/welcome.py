from django.shortcuts import render
from django.core.management import call_command
from django.db import connection
from .models import User

def index(request):
    # Check if our table exists in the current session
    all_tables = connection.introspection.table_names()
    
    # If the table isn't there, run migrate programmatically
    if "app_user" not in all_tables:
        call_command('migrate', interactive=False)
    
    # Now it's safe to query
    ids = User.objects.all()
    
    return render(request, 'welcome.html', {"user": ids})