from django.shortcuts import render
from django.http import HttpResponse
 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Exitem campos vazios')
            return render(request, 'cadastro.html')
        
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senhas e confirmar senha não são iguais.')
            return render(request, 'cadastro.html')

        # fazer a validação de email
        # enviar email para validação de email
        # ver o tamanho da senha > 5

        try:
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            return render(request, 'cadastro.html')
        except:
            return render(request, 'cadastro.html')