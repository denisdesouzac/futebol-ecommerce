# views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo à Página Inicial!</h1><p>Esta é uma página inicial temporária.</p>")
