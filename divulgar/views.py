from django.shortcuts import render
from django.http import HttpResponse


def novo_pet(request):
    return HttpResponse("estamos pra criar um novo pet")
    
