from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from .forms import CustomUserCreationForm  # Importar o formulário do arquivo forms.py
from django.http import HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from .models import Product, Order, OrderItem, Payment
from django.contrib.auth import logout
from .forms import PaymentForm  # Vamos criar este formulário a seguir

@login_required
def checkout(request):
    order = get_object_or_404(Order, client=request.user.client, status='pending')

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.order = order
            payment.save()

            # Atualiza o status do pedido para "shipped" ou conforme a lógica da sua aplicação
            order.status = 'shipped'
            order.save()

            return redirect('order_success')  # Redireciona para uma página de sucesso
        else:
            return HttpResponseBadRequest("Formulário de pagamento inválido.")
    else:
        form = PaymentForm()

    cart_items = order.order_items.all()
    cart_total = sum(item.total_price for item in cart_items)

    return render(request, 'checkout.html', {
        'form': form,
        'order': order,
        'cart_items': cart_items,
        'cart_total': cart_total,
    })

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

@login_required
def add_to_cart(request, product_id):
    # Obtém o produto e a quantidade do formulário
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 0))

    if quantity <= 0:
        return HttpResponseBadRequest("Quantidade inválida.")

    # Obtém ou cria o pedido do usuário
    order, created = Order.objects.get_or_create(client=request.user.client, status='pending')

    # Obtém ou cria o item do pedido
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if not created:
        # Se o item já existir no carrinho, apenas aumenta a quantidade
        order_item.quantity += quantity
    else:
        # Se o item for novo, define a quantidade inicial e os preços
        order_item.quantity = quantity
        order_item.unit_price = product.price

    # Atualiza o estoque do produto
    product.quantity_in_stock -= quantity

    # Calcula o preço total
    order_item.total_price = order_item.unit_price * order_item.quantity
    
    # Salva as alterações
    order_item.save()
    product.save()

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

# @login_required
# def perfil_view(request):
#     return render(request, 'perfil.html')
@login_required
def perfil_view(request):
    client = request.user.client  # Assumindo que o usuário está relacionado ao cliente
    orders = Order.objects.filter(client=client)

    return render(request, 'perfil.html', {
        'user': request.user,
        'orders': orders
    })

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
def cart_view(request):
    try:
        order = Order.objects.get(client=request.user.client, status='pending')
        cart_items = order.order_items.all()
        cart_total = sum(item.total_price for item in cart_items)
    except Order.DoesNotExist:
        cart_items = []
        cart_total = 0.00

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'cart_total': cart_total,
    })

def home_view(request):
    return render(request, 'home.html')

def order_detail(request, id):
    order = get_object_or_404(Order, id=id, client=request.user.client)

    return render(request, 'order_detail.html', {'order': order})

def order_summary(request):
    # Recupera o pedido mais recente do usuário logado
    if request.user.is_authenticated:
        order = Order.objects.filter(client__user=request.user).order_by('-order_date').first()
        if not order:
            return render(request, 'order_summary.html', {'message': 'No orders found.'})
        return render(request, 'order_summary.html', {'order': order})
    else:
        return render(request, 'order_summary.html', {'message': 'You need to log in to view this page.'})