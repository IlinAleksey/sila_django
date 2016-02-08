from django.contrib import admin

from django.contrib import admin

from .models import Event
from .models import Exercise, Customer, Coach, Gym

admin.site.register(Exercise)

admin.site.register(Customer)

admin.site.register(Coach)

admin.site.register(Gym)
# Register your models here.
