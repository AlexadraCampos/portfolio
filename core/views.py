from django.shortcuts import render



def home(request):
    return render(request, 'core/home.html')

def sobre_mim(request):
    return render(request, 'core/sobre_mim.html')

def contato(request):
    return render(request, 'core/contato.html')

def projetos(request):
    return render(request, 'core/projetos.html')

