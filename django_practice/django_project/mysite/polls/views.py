from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi there, I am a web page and I don't know why I exist")
# Create your views here.
