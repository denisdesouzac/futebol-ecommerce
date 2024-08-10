from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from .forms import CustomUserCreationForm  # Importar o formulário do arquivo forms.py
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth import logout

# def custom_logout(request):
#     logout(request)
#     return redirect('home')

def custom_logout(request):
    logout(request)
    return render(request, 'logout.html')

def loja(request):
    products = Product.objects.all()  # Recupera todos os produtos do banco de dados
    print("Produtos carregados:", products)  # Adicione esta linha para debug
    return render(request, 'loja.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Lógica para adicionar o produto ao carrinho
    # Por exemplo, você pode adicionar o produto a um objeto de Carrinho na sessão

    return redirect('carrinho')

def principal(request):
    return render(request, 'principal.html')

def sobre(request):
    return render(request, 'sobre.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('perfil')  # Redireciona para o perfil após o login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Faz login automático após o cadastro
            return redirect('perfil')  # Redireciona para o perfil após o cadastro
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'cadastro.html', {'form': form})

@login_required
def perfil_view(request):
    return render(request, 'perfil.html')

@login_required
def editar_conta_view(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'editar_conta.html', {'form': form})

@login_required
def carrinho_view(request):
    # Lógica para recuperar itens do carrinho
    return render(request, 'cart.html')

def home_view(request):
    return render(request, 'home.html')
