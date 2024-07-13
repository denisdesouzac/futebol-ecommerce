from django.shortcuts import render
from django.http import HttpResponse

def some_view(request):
    return HttpResponse("This is some view")
