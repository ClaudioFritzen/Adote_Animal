from django.shortcuts import render
from divulgar.models import Pet

# Create your views here.
def listar_pets(request):
    if request.method == "GET":
        pets = Pet.objects.filter(status='P')
        return render(request, 'listar_pets.html', {'pets':pets})