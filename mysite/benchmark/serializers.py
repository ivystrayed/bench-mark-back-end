from rest_framework import serializers
from .models import Bench, Rating

class BenchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bench
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating 
        fields = '__all__'

class avgRatingSerializer(serializers.Serializer):
    seclusion__avg = serializers.DecimalField(max_digits =3, decimal_places=2)
    view__avg = serializers.DecimalField(max_digits =3, decimal_places=2)
    accesibility__avg = serializers.DecimalField(max_digits =3, decimal_places=2)
    squirrels__avg = serializers.DecimalField(max_digits =3, decimal_places=2)
