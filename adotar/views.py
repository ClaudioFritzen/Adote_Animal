from django.shortcuts import render, redirect, HttpResponse
from divulgar.models import Pet, Raca
from .models import PedidoAdocao
from datetime import datetime

from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
def listar_pets(request):
    if request.method == "GET":
        pets = Pet.objects.filter(status='P')
        racas = Raca.objects.all()

        cidade = request.GET.get('cidade')
        raca_filter = request.GET.get('raca')

        # validação de pesquisar a cidade por letraas parecidas
        if cidade:
            pets = pets.filter(cidade__icontains=cidade)

        # busca no banco pelas raças
        if raca_filter:
            pets = pets.filter(raca__id=raca_filter)
            raca_filter = Raca.objects.get(id=raca_filter)
        return render(request, 'listar_pets.html', {'pets':pets, 'racas': racas, 'cidade':cidade, 'raca_filter': raca_filter})


def pedido_adocao(request, id_pet):
    pet = Pet.objects.filter(id=id_pet).filter(status="P")

    # VALIDAÇÕES
    if not pet.exists():
        messages.add_message(request, constants.ERROR, 'Esse pet já foi adotado :)')
        return redirect('/adotar')

    pedido = PedidoAdocao(pet=pet.first(),
                          usuario=request.user,
                          data=datetime.now())

    pedido.save()

    messages.add_message(request, constants.SUCCESS, 'Pedido de adoção realizado, você receberá um e-mail caso ele seja aprovado.')
    return redirect('/adotar')


def processa_pedido_adocao(request, id_pedido):
    status = request.GET.get('status')
    return  HttpResponse(f' Estado do pedido {status}')