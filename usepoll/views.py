from django.shortcuts import render

from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.renderers import JSONRenderer
from .models import *
from django.core import serializers
import json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def coaches_request(request):
    if request.method == 'GET':
        testlogin = request.GET.get('testlogin', '')
        coach_name = request.GET.get('name', '')
        object_id = request.GET.get('id', '')
        print(coach_name, object_id)
        # if coach_name:
        #     try:
        #         coaches_list = Coach.objects.get(name=coach_name)
        #     except ObjectDoesNotExist:
        #         return HttpResponseBadRequest('Bad Request')
        #     coaches_serialized = CoachSerializerComplete(coaches_list)
        #     print(coaches_serialized.data)
        #     json_res = coaches_serialized.data
        #     print(json_res)
        #     return JsonResponse(json_res, content_type='application/json; charset=utf-8')
        if object_id:
            try:
                coaches_list = Coach.objects.get(pk=object_id)
            except ObjectDoesNotExist:
                return HttpResponseBadRequest('Bad Request')
            coaches_serialized = CoachSerializerComplete(coaches_list)
            print(coaches_serialized.data)
            json_res = coaches_serialized.data
            print(json_res)
            return JsonResponse(json_res, content_type='application/json; charset=utf-8', json_dumps_params={'ensure_ascii': False})
        else:
            coaches_list = list(Coach.objects.all())
            coaches_serialized = [CoachSerializer(coach).data for coach in coaches_list]
            return JsonResponse(coaches_serialized, safe=False, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8')

    return HttpResponseBadRequest('Bad Request')


def events_request(request):
    if request.method == 'GET':
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
            return JsonResponse(json_res, content_type='application/json; charset=utf-8', json_dumps_params={'ensure_ascii': False})
        else:
            exercizes_list = list(Exercise.objects.all())
            exercizes_serialized = [ExerciseSerializer(coach).data for coach in exercizes_list]
            return JsonResponse(exercizes_serialized, content_type='application/json; charset=utf-8', json_dumps_params={'ensure_ascii': False}, safe=False)

    return HttpResponseBadRequest('Bad Request')


def gyms_request(request):
    if request.method == 'GET':
        object_id = request.GET.get('id', '')
        if object_id:
            try:
                exercizes_list = Gym.objects.get(pk=object_id)
            except ObjectDoesNotExist:
                return HttpResponseBadRequest('Bad Request')
            exercizes_serialized = GymSerializer(exercizes_list)
            print(exercizes_serialized.data)
            json_res = exercizes_serialized.data
            print(json_res)
            return JsonResponse(json_res, content_type='application/json; charset=utf-8', json_dumps_params={'ensure_ascii': False})
        else:
            exercizes_list = list(Gym.objects.all())
            exercizes_serialized = [GymSerializer(coach).data for coach in exercizes_list]
            return JsonResponse(exercizes_serialized, content_type='application/json; charset=utf-8', json_dumps_params={'ensure_ascii': False}, safe=False)

    return HttpResponseBadRequest('Bad Request')



# Create your views here.
