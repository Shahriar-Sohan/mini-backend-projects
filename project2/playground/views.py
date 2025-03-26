from django.shortcuts import render
from django.http import HttpResponse


def calc():
    x=1
    y=2
    return x
# A basic view that returns an HTTP response
def home(request):
    x = calc()
    return HttpResponse("Hello, welcome to the home page!")

# A view that renders a template
def about(request):
    return HttpResponse("Hello, welcome to the about page!")