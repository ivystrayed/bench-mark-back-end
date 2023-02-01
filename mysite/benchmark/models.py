from django.db import models


class Bench (models.Model):
    img = models.ImageField()
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

class Rating (models.Model):
    bench = models.ForeignKey(Bench, on_delete=models.CASCADE)
    view = models.IntegerField()
    seclusion = models.IntegerField()
    accesibility = models.IntegerField()
    squirrels = models.IntegerField()
    time_spent = models.TimeField()
    


