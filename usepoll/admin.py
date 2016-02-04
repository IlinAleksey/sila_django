from django.contrib import admin

from django.contrib import admin

from .models import Event
from .models import Exercise
from .models import Customer
from .models import Coach

admin.site.register(Event)

admin.site.register(Exercise)

admin.site.register(Customer)

admin.site.register(Coach)
# Register your models here.
