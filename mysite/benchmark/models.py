from django.db import models
from django.db.models import Avg


class Bench (models.Model):
    img = models.ImageField()
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

    def average_rating(self) -> float:
        return Rating.objects.filter(bench = self).aggregate(average_rating = Avg('rating'))


    def __str__(self):
        return f"bench # {self.id}: {self.average_rating()}"

class Rating (models.Model):
    bench = models.ForeignKey(Bench, on_delete=models.CASCADE)
    view = models.IntegerField()
    seclusion = models.IntegerField()
    accesibility = models.IntegerField()
    squirrels = models.IntegerField()
    time_spent = models.TimeField()

    def calculateRating(self):
        rating = 0
        rating = self.squirrel + self.seclusion + self.view 
        rating /= 3
        return rating 


    def __str__ (self):
        return f"{self.bench.id}: {self.rating()}"



