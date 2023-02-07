from django.db import models
from django.db.models import Avg


class Bench (models.Model):
    img = models.ImageField(default=None, null=True, blank=True)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

    # def average_rating(self) -> float:
    #     return Rating.objects.filter(bench = self).aggregate(average_rating = Avg('Rating'))


    def __str__(self):
        return f"bench # {self.id}: its a gud bench"

class Rating (models.Model):
    bench = models.ForeignKey(Bench, on_delete=models.CASCADE)
    view = models.IntegerField()
    seclusion = models.IntegerField()
    accesibility = models.IntegerField()
    squirrels = models.IntegerField() 
    time_submitted = models.TimeField(default=None)
    time_spent = models.IntegerField(default=None)
    rating = models.IntegerField()

    def __str__ (self):
        return f"{self.bench.id}: {self.rating}"



