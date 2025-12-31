from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from django.shortcuts import render
from .models import User
from .updater import updater
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

@csrf_exempt
def Home(request):
    if request.method == "POST":
        head   = request.POST.get("head")
        tail   = request.POST.get("tail")
        iloc   = request.POST.get("iloc")
        loc   = request.POST.get("loc")
        col   = request.POST.get("col")
        fil   = request.POST.get("fil")
        fil2   = request.POST.get("fil2")
        discribe   = request.POST.get("discribe")
        
        if discribe == "0":
            discribe = True
        else:
            discribe = False
        
       
    
       
        item = User.objects.all()
        df = pd.DataFrame(item[0].dynamic_data)
        cols = df.columns
        if head:  
            head = int(head)
            
            if discribe == True:
                df = df.head(head).describe()
            else:
                df = df.head(head)
                
                
           
        if tail:
           tail = int(tail)
           if discribe == True:
                df = df.tail(tail).describe()
           else:
                df = df.tail(tail)
            
        if col:
            col  = int(col)
            if discribe == True:
               df = df.take([col], axis=0).describe()
            else:
                df = df.take([col], axis=0)
            
        
            
        if iloc:
            iloc  = int(iloc)
            if discribe == True:
               df = df.iloc[iloc].describe()
               
            else:
               df = df.iloc[iloc]
               
        if loc:
            if discribe == True:
                df = df[[loc]].describe()
            else:
                df = df[[loc]] 
                
        if fil & fil2:
            if discribe == True:
                df = filter_data(df,fil,fil2)
                df = df.describe()
            else:
                df = filter_data(df,fil,fil2)
                
               
            
           
            print(df)
            
        return render(request,"home.html" ,{"user":df.to_dict(),"col":cols})
   
    return render(request, 'home.html', {'message': 'Form submitted!'})





def filter_data(df,cols_str, values_str):
    # .split() without arguments handles multiple spaces automatically
    cols = cols_str.split()
    values = values_str.split()
    
    # Check if lists match to avoid errors
    if len(cols) != len(values):
        raise ValueError("The number of columns must match the number of values.")

    # Initialize mask with all True
    mask = pd.Series([True] * len(df))
    
    # zip() is cleaner for looping through two lists simultaneously
    for col, val in zip(cols, values):
        if col in df.columns:
            # Update mask: cumulative AND logic
            current_filter = df[col].astype(str).str.strip() == str(val).strip()
            mask &= current_filter
            
    return df[mask]