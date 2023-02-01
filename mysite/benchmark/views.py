from django.shortcuts import render
from django.http import HttpResponse

def helloWorld(request):
    return HttpResponse("Hello World!")


# READ 

def getAllBenches(request):
    return HttpResponse("all the benches")



