from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib import messages
from .forms import CustomUserCreationForm  # Importar o formulário do arquivo forms.py
from django.http import HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem, Payment, Client
from django.contrib.auth import logout
from .forms import PaymentForm  # Vamos criar este formulário a seguir
from django.utils import timezone
from .forms import EditAccountForm
from django.contrib.auth import update_session_auth_hash

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
    user = request.user
    orders = Order.objects.filter(client=user.client)  
    
    return render(request, 'perfil.html', {
        'user': user,
        'orders': orders
    })

@login_required
def editar_conta(request):
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            if form.cleaned_data['password1']:
                # Atualiza a sessão para que o usuário continue logado após a mudança da senha
                update_session_auth_hash(request, user)
            messages.success(request, 'Suas informações foram atualizadas com sucesso.')
            return redirect('editar_conta')  # Redireciona para a mesma página
    else:
        form = EditAccountForm(instance=request.user)

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

    # Renderiza a página de detalhes do pedido para todos os status
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
    
@login_required
def add_to_cart(request, product_id):
    # Obtém o produto com base no id fornecido
    product = get_object_or_404(Product, id=product_id)

    # Obtém a quantidade fornecida na requisição GET, padrão é 1 se não fornecido
    quantity = request.GET.get('quantity', 1)
    try:
        quantity = int(quantity)
        if quantity < 1:
            quantity = 1
    except (ValueError, TypeError):
        quantity = 1

    # Obtém ou cria um pedido para o cliente
    order_qs = Order.objects.filter(client=request.user.client, status='pending')
    if order_qs.exists():
        order = order_qs[0]
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(client=request.user.client, order_date=ordered_date, status='pending')

    # Obtém ou cria um item de pedido para o produto
    order_item, created = OrderItem.objects.get_or_create(
        product=product,
        order=order,
        defaults={'quantity': quantity}
    )

    # Atualiza a quantidade do item do pedido
    if not created:
        if order_item.quantity + quantity > product.quantity_in_stock:
            messages.warning(request, "Quantidade solicitada excede o estoque disponível.")
            return redirect("order-summary")

        order_item.quantity += quantity
        order_item.save()
        messages.info(request, "Quantidade do item foi atualizada.")
    else:
        if quantity > product.quantity_in_stock:
            messages.warning(request, "Quantidade solicitada excede o estoque disponível.")
            return redirect("order-summary")

        order_item.quantity = quantity
        order_item.save()
        messages.info(request, "Item adicionado ao carrinho.")

    # Atualiza o estoque do produto
    product.quantity_in_stock -= quantity
    product.save()

    # Adiciona o item ao pedido se ainda não estiver
    if not order.order_items.filter(product=product).exists():
        order.order_items.add(order_item)

    return redirect("carrinho")


@login_required
def remove_from_cart(request, product_id):
    # Recupera o produto com base no ID
    product = get_object_or_404(Product, id=product_id)
    
    # Obtém a ordem não finalizada do usuário
    order_qs = Order.objects.filter(client=request.user.client, status='pending')
    if order_qs.exists():
        order = order_qs[0]
        
        # Verifica se o item está no carrinho
        if order.order_items.filter(product=product).exists():
            order_item = OrderItem.objects.filter(
                product=product,
                order=order
            ).first()
            
            if order_item:
                order_item.delete()  # Remove o item do carrinho
                # Verifica se o pedido está vazio
                if not order.order_items.exists():
                    order.delete()  # Remove o pedido se estiver vazio
                messages.info(request, "Produto removido do carrinho.")
            else:
                messages.info(request, "Produto não encontrado no carrinho.")
        else:
            messages.info(request, "Produto não está no seu carrinho.")
    else:
        messages.info(request, "Você não tem um pedido ativo.")
    
    return redirect("carrinho")