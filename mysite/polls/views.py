from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(request):
    myName = "andre"
    questions = Question.objects.all()
    context = {"name":myName, 'questions' : questions}
    return render(request, "polls/index.html", context)

def index1(request):
    return HttpResponse("<h1>poll page 1</h1>")