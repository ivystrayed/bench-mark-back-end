from django.shortcuts import render
from django.http import HttpResponse


# READ 

def getAllBenches(request):
    return HttpResponse("all the benches")



