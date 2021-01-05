from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello word. This is a test view for the presentation app")
