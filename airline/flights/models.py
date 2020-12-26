from django.db import models
from django.db.models.deletion import CASCADE

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return f" {self.city} ({self.code}) "
    
class Flights(models.Model):
    
    origin = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departures")
    destination = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arrivals")
    duration = models.IntegerField()
    
    def __str__(self):
    	return f"{self.origin} to {self.destination} in {self.duration} minutes"
    
class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    flight = models.ManyToManyField(Flights,blank=True,related_name="passengers")
    
    def __str__(self):
    	return f"{self.first_name} {self.last_name} "