from django.shortcuts import render

from catalog.models import Product


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.POST:
        contact = request.POST
        print(contact)
    return render(request, 'contacts.html')