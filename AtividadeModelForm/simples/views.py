from django.shortcuts import render, redirect
from simples.models import Product
from simples.forms import ProductForm

def list_products(request):
    products = Product.objects.all()
    context = {'products':products}
    html = 'list.html'
    return render(request, html, context)



def add_product(request): 
    html = 'add.html'
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.save()
            return redirect('/list_products/')
    else:
        form = ProductForm()
        context = {'form': form}
        return render(request, html, context)