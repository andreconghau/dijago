from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Andre Polls pages")

def index1(request):
    return HttpResponse("<h1>poll page 1</h1>")