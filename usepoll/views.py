from django.shortcuts import render

from django.http import HttpResponse
from .models import Coach
from .models import Exercise
from django.core import serializers
import json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def coaches(request):
    if request.method == 'GET':
        coaches_json = serializers.serialize("json", Coach.objects.all())
        return HttpResponse(coaches_json)

    if request.method == 'POST':
        return HttpResponse("POST")
    return HttpResponse("Nwither post nor get")


def events_request(request):
    if request.method == 'GET':
        events = Exercise.objects.all()
        print(events)
        events_json = serializers.serialize("json", Exercise.objects.all())
        print(events_json)
        return HttpResponse(events_json)

    if request.method == 'POST':
        return HttpResponse("POST")
    return HttpResponse("Nwither post nor get")

# Create your views here.
