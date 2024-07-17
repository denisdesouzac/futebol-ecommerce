# Projeto prático Programação Web

# Futebol Store

Futebol Store é uma aplicação Django para gerenciar uma loja online de artigos esportivos, com foco em produtos de futebol. O projeto inclui funcionalidades para cadastro de clientes, gerenciamento de pedidos, itens de pedidos e pagamentos.

## Funcionalidades

- Cadastro e autenticação de usuários
- Gerenciamento de clientes e administradores
- Criação e acompanhamento de pedidos
- Adição de itens aos pedidos
- Gerenciamento de pagamentos

## Instalação

### Pré-requisitos

- Python 3.x
- Django 3.x ou superior
- Banco de dados (SQLite por padrão, mas pode ser configurado para usar outros)

### Passos de Instalação

1. Clone o repositório:
   
   ```git clone https://github.com/seu-usuario/futebol_store.git
      cd futebol_store

2. Crie e ative um ambiente virtual:


```python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows

3. Instale as dependências:


```pip install -r requirements.txt

4. Aplique as migrações do banco de dados:

```python manage.py migrate

5. Crie um superusuário para acessar o admin do Django:

```python manage.py createsuperuser

6. Inicie o servidor de desenvolvimento:

```python manage.py runserver

7. Acesse a aplicação em http://127.0.0.1:8000/.
