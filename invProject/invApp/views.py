from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# CRUD = Create, Read, Update, Delete
# Home View
def home_view(request):
    return render(request, 'invApp/home.html')

# Create View
def product_create_view(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form':form})

# Read View
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'invApp/product_list.html', {'products':products})
