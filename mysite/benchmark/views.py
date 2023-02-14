from django.db.models import Avg
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import BenchSerializer, RatingSerializer, avgRatingSerializer
from .models import Bench, Rating
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response 





# READ 

class BenchViewSet(viewsets.ModelViewSet):
    queryset = Bench.objects.all().order_by('id')
    serializer_class = BenchSerializer

    @action(detail=True)
    def benchstats(self, request, pk=None):
        bench = self.get_object()
        queryset = Rating.objects.filter(bench = bench.id).aggregate(Avg('seclusion'), Avg('view'),Avg('accesibility'), Avg('squirrels'),)
        serializer = avgRatingSerializer(queryset)
        return Response(serializer.data, 200)





class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all().order_by('id')
    serializer_class = RatingSerializer








