## Nomes: 
- Denis de Souza
- Luis Felipe Costa Teixeira
- Ronald Galdino

# **Futebol Store**

Futebol Store é uma aplicação em Django para gerenciar uma loja online de artigos esportivos, focada em produtos de futebol. O projeto inclui funcionalidades para cadastro de clientes, gerenciamento de pedidos, itens de pedidos e pagamentos. Nesta etapa, priorizamos o desenvolvimento dos Models, mas estamos avançando para adicionar mais detalhes, como a implementação da parte Front-end.

## Funcionalidades

- Cadastro e autenticação de usuários
- Gerenciamento de clientes e administradores
- Criação e acompanhamento de pedidos
- Adição de itens aos pedidos
- Gerenciamento de pagamentos

## Instalação

- Para saber mais sobre Django:

   [Link do projeto](https://github.com/ufla-prog-web/aula-django-03)

### Pré-requisitos

- Python 3
- Django 3 ou superior

### Passos de Instalação

1. Clone o repositório:
   
   
     ```
   git clone https://github.com/seu-usuario/futebol_store.git
   cd futebol_store


3. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows

4. Instale o django dentro do ambiente virtual criado (testado na versão 5.0.3):

    ```bash
    pip3 install django
    python -m pip install Django
   
5. teste as versões

    ```bash
   django-admin --version
   python3 -m django --version

5. Instale as dependências:
   
   ```bash
   pip install -r requirements.txt

6. Executando o Projeto:

   ```bash
   python manage.py migrate

7. Crie um superusuário para acessar o admin do Django:
   
   ```bash
   python3 manage.py collectstatic

9. Inicie o servidor de desenvolvimento:
    
   ```bash
   python manage.py runserver

9. Acesse a aplicação em http://127.0.0.1:8000/.
