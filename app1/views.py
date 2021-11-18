from django.shortcuts import render
from django.http import HttpResponse

def abdulrahim(request):
    return HttpResponse('<marquee><h1 style="color:skyblue;",>ABDUL RAHIM IS MY BROTHER</h1></marquee>')

