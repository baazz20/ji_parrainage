from django.shortcuts import render

def index(request):
    return render(request, "sponsorship/index.html")

def resultat(request):
    return render(request, "sponsorship/resultat.html")