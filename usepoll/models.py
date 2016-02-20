from django.db import models
from rest_framework import serializers


class Coach(models.Model):
    name = models.CharField(max_length=200)
    experience = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    image_url = models.CharField(max_length=200, default='', blank=True)
    bio = models.TextField(max_length=10000, default='', blank=True)

    def __str__(self):
        return self.name

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ('id', 'name', 'experience', 'price', 'image_url')


class CoachSerializerComplete(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ('id', 'name', 'experience', 'price', 'image_url', 'bio')


class Gym(models.Model):
    name = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=200, default='', blank=True )
    address = models.CharField(max_length=200, default='', blank=True )
    image_url = models.CharField(max_length=200, default='', blank=True)



class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ('id', 'name', 'address', 'phone', 'city', 'image_url')


class Exercise(models.Model):
    name = models.CharField(max_length=200)
    event_date = models.DateTimeField('date')
    coach = models.ForeignKey(Coach, related_name='exercises', default=None, null=True, blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.name, str(self.event_date))

class ExerciseSerializer(serializers.ModelSerializer):
    coach = CoachSerializer()
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'event_date', 'coach')





# Create your models here.
