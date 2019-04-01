from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, World.  This is going to be a decent application for handling advising!")