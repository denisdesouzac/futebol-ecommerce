from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def principal(request):
    template = loader.get_template('principal.html')
    return HttpResponse(template.render())

def loja(request): 
    template = loader.get_template('loja.html')
    return HttpResponse(template.render())

def sobre(request):
    template = loader.get_template('sobre.html')
    return HttpResponse(template.render())