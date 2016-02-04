from django.db import models
from rest_framework import serializers

class Event(models.Model):
    name = models.CharField(max_length=200)
    event_date = models.DateTimeField('date of the event')

    def __str__(self):
        return self.name + self.event_date.__str__()

class Exercise(models.Model):
    name = models.CharField(max_length=200)
    event_date = models.DateTimeField('date')

    def __str__(self):
        return '{0} {1}'.format(self.name, str(self.event_date))

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('name', 'event_date')


class Customer(models.Model):
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    pullups_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name + str(self.pullups_count)


class Coach(models.Model):
    name = models.CharField(max_length=200)
    experience = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    image_url = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ('name', 'experience', 'price', 'image_url')


# Create your models here.
