from django.shortcuts import render, redirect
from complexa.forms import AuthorForm, PublishingCompanyForm, BookForm
from complexa.models import Author, PublishingCompany, Book



def add_author(request): 
    html = 'add.html'
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.save()
            return redirect('/')
    else:
        form = AuthorForm()
        context = {'form': form}
        return render(request, html, context)

def add_pub_company(request): 
    html = 'add.html'
    if request.method == 'POST':
        form = PublishingCompanyForm(request.POST)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.save()
            return redirect('/')
    else:
        form = PublishingCompanyForm()
        context = {'form': form}
        return render(request, html, context)

def add_book(request): 
    html = 'add.html'
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.save()
            return redirect('/')
    else:
        form = BookForm()
        context = {'form': form}
        return render(request, html, context)

def list_books(request):
    books = Book.objects.all()
    context = {'books':books}
    html = 'list_books.html'
    return render(request, html, context)

def list_pub_companys(request):
    pub_companys = PublishingCompany.objects.all()
    context = {'pub_companys':pub_companys}
    html = 'list_pubs.html'
    return render(request, html, context)

def list_authors(request):
    authors = Author.objects.all()
    context = {'authors':authors}
    html = 'list_authors.html'
    return render(request, html, context)