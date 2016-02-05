from django.shortcuts import render

from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.renderers import JSONRenderer
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
        testlogin = request.GET.get('testlogin', '')
        if testlogin == 'no':
            return HttpResponseForbidden("testlogin = no")
        coach_name = request.GET.get('name', '')
        object_id = request.GET.get('id', '')
        print(coach_name, object_id)
        if coach_name:
            try:
                coaches_list = Coach.objects.get(name=coach_name)
            except ObjectDoesNotExist:
                return HttpResponseBadRequest('Bad Request')
            coaches_serialized = CoachSerializer(coaches_list)
            print(coaches_serialized.data)
            json_res = coaches_serialized.data
            print(json_res)
            return HttpResponse(str(json_res))
        if object_id:
            try:
                coaches_list = Coach.objects.get(pk=object_id)
            except ObjectDoesNotExist:
                return HttpResponseBadRequest('Bad Request')
            coaches_serialized = CoachSerializer(coaches_list)
            print(coaches_serialized.data)
            json_res = coaches_serialized.data
            print(json_res)
            return HttpResponse(str(json_res))
        else:
            coaches_list = list(Coach.objects.all())
            coaches_serialized = [CoachSerializer(coach).data for coach in coaches_list]
            return HttpResponse(json.dumps(coaches_serialized))

    return HttpResponseBadRequest('Bad Request')


def events_request(request):
    if request.method == 'GET':
        testlogin = request.GET.get('testlogin','')
        if testlogin == 'no':
            return HttpResponseForbidden("testlogin = no")
        object_id = request.GET.get('id', '')
        if object_id:
            try:
                exercizes_list = Exercise.objects.get(pk=object_id)
            except ObjectDoesNotExist:
                return HttpResponseBadRequest('Bad Request')
            exercizes_serialized = ExerciseSerializer(exercizes_list)
            print(exercizes_serialized.data)
            json_res = exercizes_serialized.data
            print(json_res)
            return HttpResponse(str(json_res))
        else:
            exercizes_list = list(Exercise.objects.all())
            exercizes_serialized = [ExerciseSerializer(coach).data for coach in exercizes_list]
            return HttpResponse(json.dumps(exercizes_serialized))

    return HttpResponseBadRequest('Bad Request')


def signup(request):
    if request.method == 'POST':
        testlogin = request.POST.get('testlogin','')
        if testlogin == 'no':
            return HttpResponseForbidden("testlogin = no")
        exercizes_list = list(Exercise.objects.all())
    return HttpResponseBadRequest('Bad Request')


# Create your views here.
