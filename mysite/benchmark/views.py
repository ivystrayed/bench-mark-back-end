from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import BenchSerializer, RatingSerializer
from .models import Bench, Rating





# READ 

class BenchViewSet(viewsets.ModelViewSet):
    queryset = Bench.objects.all().order_by('id')
    serializer_class = BenchSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all().order_by('id')
    serializer_class = RatingSerializer




