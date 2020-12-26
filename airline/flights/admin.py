from django.contrib import admin


# Register your models here.
from .models import Flights,Airport, Passenger
class FlightsAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration","passengers")
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flight",)
    
admin.site.register(Flights,FlightsAdmin)
admin.site.register(Airport)
admin.site.register(Passenger,PassengerAdmin)


