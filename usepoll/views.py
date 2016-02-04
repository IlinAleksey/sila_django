from django.shortcuts import render

from django.http import HttpResponse
from .models import Coach
from .models import CoachSerializer
from .models import Exercise
from .models import ExerciseSerializer
from django.core import serializers
import json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def coaches(request):
    if request.method == 'GET':
        coaches_json = serializers.serialize("json", Coach.objects.all(), fields=('name', 'experience', 'price'))
        coaches_list = list(Coach.objects.all())
        coaches_serialized = [CoachSerializer(coach).data for coach in coaches_list]
        print(coaches_serialized)
        #coaches_dict = coaches.__
        return HttpResponse(coaches_serialized)

    if request.method == 'POST':
        return HttpResponse("POST")
    return HttpResponse("Nwither post nor get")


def events_request(request):
    if request.method == 'GET':
        #events = Exercise.objects.all()
        #print(events)
        events_json = serializers.serialize("json", Exercise.objects.all(), fields=('name', 'event_date'))
        #print(events_json)

        exercizes_list = list(Exercise.objects.all())
        exercizes_serialized = [ExerciseSerializer(coach).data for coach in exercizes_list]
        return HttpResponse(exercizes_serialized)

    if request.method == 'POST':
        return HttpResponse("POST")
    return HttpResponse("Nwither post nor get")

# Create your views here.
