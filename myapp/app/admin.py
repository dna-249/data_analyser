from django.contrib import admin

# Register your models here.
# app/admin.py

from django.contrib import admin
from .models import User # <-- Import your custom model(s)

# Option 1: Using the decorator (Modern Django)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # This list controls which fields show up in the main list view
    list_display = ('user_id', 'dynamic_data') 
    
    # Optional: If you want to search the dynamic data based on user_id
    search_fields = ('user_id',) 


# Option 2 (Alternative if you prefer not using decorators):
# admin.site.register(User, UserAdmin)