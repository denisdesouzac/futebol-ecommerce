from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Client

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
    first_name = forms.CharField(
        label='Nome',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        required=True
    )
    last_name = forms.CharField(
        label='Sobrenome',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}),
        required=True
    )
    endereco = forms.CharField(
        label='Endereço',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço'}),
        required=True
    )
    telefone = forms.CharField(
        label='Telefone',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            Client.objects.create(user=user, endereco=self.cleaned_data['endereco'], telefone=self.cleaned_data['telefone'])
        
        return user
