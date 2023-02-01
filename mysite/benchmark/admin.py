from django.contrib import admin

# Register your models here.
from .models import Bench, Rating

admin.site.register(Bench)
admin.site.register(Rating)