from rest_framework import serializers
from .models import Bench, Rating

class BenchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bench
        fields = ('id', 'img', 'long', 'lat')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating 
        fields = ('id', 'bench', 'view', 'squirrels', 'seclusion', 'accesability', 'time_spent', 'time_submitted')