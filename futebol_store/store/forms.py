from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
