from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

def principal(request):
    template = loader.get_template('principal.html')
    return HttpResponse(template.render())

def loja(request):
    template = loader.get_template('loja.html')
    return HttpResponse(template.render())

def sobre(request):
    template = loader.get_template('sobre.html')
    return HttpResponse(template.render())

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('perfil')  # Redireciona para a página perfil após o login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Nome de usuário',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuário'}),
        error_messages={
            'required': 'O nome de usuário é obrigatório.',
            'max_length': 'O nome de usuário deve ter no máximo 150 caracteres.',
        }
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu e-mail'}),
        error_messages={
            'required': 'O e-mail é obrigatório.',
            'invalid': 'Digite um e-mail válido.',
        }
    )
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}),
        error_messages={
            'required': 'A senha é obrigatória.',
        }
    )
    password2 = forms.CharField(
        label='Confirme sua senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'}),
        error_messages={
            'required': 'A confirmação de senha é obrigatória.',
            'password_mismatch': 'As senhas não coincidem.',
        }
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm  # Certifique-se de ajustar o caminho do import conforme necessário

def editar_conta_view(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = UserChangeForm(instance=request.user)

    
    return render(request, 'editar_conta.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automático após o cadastro
            return redirect('perfil')  # Redireciona para a página perfil após o cadastro
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def carrinho_view(request):
    # Lógica para recuperar itens do carrinho
    return render(request, 'carrinho.html')

def home_view(request):
    return render(request, 'home.html')

@login_required
def perfil_view(request):
    return render(request, 'perfil.html')
