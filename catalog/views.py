from django.shortcuts import render

from catalog.models import Contact


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\nТелефон: {contact}\nСообщение: {message}\n')
        Contact.objects.create(name=name, phone=contact, message=message)
    return render(request, 'contacts.html')
