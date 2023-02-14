from django.db import models
from django.db.models import Avg


class Bench (models.Model):
    img = models.ImageField(default='../asets/default-bench.png')
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"bench # {self.id}: its a gud bench"

class Rating (models.Model):
    bench = models.ForeignKey(Bench, on_delete=models.CASCADE)
    view = models.IntegerField()
    seclusion = models.IntegerField()
    squirrels = models.IntegerField()
    accesibility = models.IntegerField()

    def __str__ (self):
        return f"{self.bench.id}"



