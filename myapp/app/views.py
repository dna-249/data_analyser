from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json
from .updater import updater

@csrf_exempt
def index(request):
    if request.method == "GET":
        return HttpResponse("Server is running.")
  
    if request.method != 'POST':
        return JsonResponse({'error': f'Method {request.method} not allowed'}, status=405)
    
    # 1. Get the file safely
    uploaded_file = request.POST.get('file')
    if not uploaded_file:
        return JsonResponse({'error': 'No file found. Make sure you use name="file" and multipart/form-data encoding.'}, status=400)

    try:
        # 2. Process file through updater
        df_data = updater(uploaded_file)
        
        # Convert DataFrame to Python List (records orient)
        json_string = df_data.to_json(orient='records') 
        dynamic_payload = json.loads(json_string) 
        
        # 3. Save to Database (Hardcoded user_id=1 as per your request)
        user_instance, created = User.objects.get_or_create(
            user_id= uploaded_file,
            defaults={'dynamic_data': dynamic_payload} 
        )
        
        if not created:
            # IMPORTANT: Since dynamic_payload is a LIST, we replace or extend. 
            # Dictionaries use .update(), Lists use assignment or .extend()
            user_instance.dynamic_data = dynamic_payload 
            user_instance.save()
        
        return JsonResponse({
            'message': 'User record created' if created else 'User record updated',
            'user_id': 1,
            'status': 'Created' if created else 'Updated',
            'rows_processed': len(dynamic_payload)
        }, status=201 if created else 200)

    except Exception as e:
        return JsonResponse({'error': f'Processing error: {str(e)}'}, status=500)