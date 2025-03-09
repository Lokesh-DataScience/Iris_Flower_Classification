from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .ml_model import predict_iris
from django.shortcuts import render

@csrf_exempt
def classify_iris(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            features = data.get("features",[])
            if len(features) != 4:
                return JsonResponse({"error":"Invalid input"}, status=400)
            
            prediction = predict_iris(features)
            return JsonResponse({"prediction":prediction})
        except Exception as e:
            return JsonResponse({"error":str(e)}, status=500)
    return JsonResponse({"Message":"Send a POST request with features"}, status=200)

def iris_form(request):
    return render(request, "classifier/index.html")