from django.shortcuts import render



def home(request):
    return render(request, 'index.html')

def sobre_mim(request):
    return render(request, 'sobre_mim.html')

def contato(request):
    return render(request, 'contato.html')

def projetos(request):
    return render(request, 'projetos.html')