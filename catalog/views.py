from django.shortcuts import render, get_object_or_404

from catalog.models import Contact, Product


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)


def contact_list(request):
    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\nТелефон: {contact}\nСообщение: {message}\n')
        Contact.objects.create(name=name, phone=contact, message=message)
    return render(request, 'contact_list.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)
