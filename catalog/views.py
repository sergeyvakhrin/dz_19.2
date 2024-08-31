from django.shortcuts import render

from catalog.models import Contact, Product


def product_list(request):
    product = Product.objects.all()
    context = {'products': product}
    return render(request, 'product_list.html', context)


def contact_list(request):
    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\nТелефон: {contact}\nСообщение: {message}\n')
        Contact.objects.create(name=name, phone=contact, message=message)
    return render(request, 'contact_list.html')


