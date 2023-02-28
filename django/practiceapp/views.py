from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import json
from forms import ParametersForm
from models import TrainedData

@csrf_exempt
def params(request):
    if request.body:
        data = json.loads(request.body.decode('utf-8'))
        if data:
            for d in data:
                form = ParametersForm(d)
                if form.is_valid():
                    form.save()
    return JsonResponse({})

def trained_data(request):
    data = TrainedData.objects.all()
    return JsonResponse(data, safe=False)