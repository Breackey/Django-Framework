from django.shortcuts import render

def home(request):
    return render(request, "home.html",{})

def about(request):
    from pages.namer import bree
    return render(request, "about.html",{"me":bree})

def contact(request):
    return render(request, "contact.html",{})