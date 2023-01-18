from django.shortcuts import render, redirect
from django.http import HttpResponse
import re
from django.contrib.auth.models import User  
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout

def cadastro(request):

    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')

    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')


        # validaçao dos campos nao podem estar vazio
        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Exitem campos vazios')
            return render(request, 'cadastro.html')

        # filtrando no banco se ja existe esse email
        usuario = User.objects.filter(username = nome)

        # validação para ver se existe esse usuario no banco ja
        if usuario.exists():
            messages.add_message(request, constants.WARNING, 'Nome de usuario já existente')
            return render(request, 'cadastro.html', {'email': email, 'senha': senha, 'confirmar_senha': confirmar_senha}) 
         #return HttpResponse('Cliente já existe')

        # validação para ver se existe esse email no banco ja
        email = User.objects.filter(email = email)
        if email.exists():
            messages.add_message(request, constants.WARNING, 'Email já utilizado')
            return render(request, 'cadastro.html', {'nome': nome, 'senha': senha, 'confirmar_senha': confirmar_senha}) 
         #return HttpResponse('Cliente já existe')

        # validação de email com regex
        """ if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            messages.add_message(request, constants.WARNING, 'Digite um emai valido') """
            #return render(request, {'nome': nome, 'senha': senha, 'confirmar_senha': confirmar_senha})


                



        # senha tem que ter 5 ou mais caractes
        if len(senha.strip()) <= 5:
            messages.add_message(request, constants.ERROR, 'Senha deve ser maior 5 caracteres ou mais')
            return render(request,'cadastro.html', {'nome': nome, 'email': email})

        # senha e contra senha tem que ser iguais
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senhas e confirmar senha não são iguais.')
            return render(request, 'cadastro.html', {'nome': nome, 'email': email})

        # fazer a validação de email
        # enviar email para validação de email
        # ver o tamanho da senha > 5 feito 
  
        try:
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            messages.add_message(request, constants.SUCCESS, 'Criado com sucesso')
            return render(request, 'login.html')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema! tente mais tarde.')
            return render(request, 'cadastro.html')

def logar(request):
    
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')

    if request.method == "GET":
        return render(request, 'login.html')
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        # verificação 
        user = authenticate(username=nome,
                            password=senha)
        #print(user)  # none nao existe, se existir aparecerar o nome do usuario

        # validações
        if user is not None:
            login(request, user)
            return redirect(f'/divulgar/novo_pet')
        else:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha incorretos!!!')
            return render(request, 'login.html')

def sair(request):
    logout(request)
    return redirect('/auth/login')

