from django.shortcuts import render
from django.http import Http404,HttpResponse
from .models import product_model
from django.views.generic import TemplateView
from datetime import datetime
from products.form import add_product_form,import_export_form
# Create your views here.


def products_home(request):
    all_products = product_model.objects.all()
    return render(request, 'products.html', {
        'data': "Hello Django ",
        'all_products': all_products,
    })


def product_detail(request,product_id):
    try:
        product = product_model.objects.get(id = product_id)
    except product_model.DoesNotExist:

        raise Http404("product does not exist")

    return render(request, 'product_detail.html', { 'product':product})


# def get_product(request):


def add_product(request):
    if request.method == "POST":
        form = add_product_form(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.name = form.cleaned_data['name']
            product.size = form.cleaned_data['size']
            product.style = form.cleaned_data['style']
            product.color = form.cleaned_data['color']
            product.number_in_stock = form.cleaned_data['number_in_stock']
            product.save()

            return render(request, 'update.html', {'form': form})
    else:
        form = add_product_form()
    return render(request, 'update.html', {'form': form})


def import_export(request):
    if request.method == "POST":
        form = import_export_form(request.POST)
        if form.is_valid():
            history = form.save(commit=False)
            history.product = form.cleaned_data['product']
            product = history.product
            history.number = form.cleaned_data['number']
            product.number_in_stock += history.number
            history.time = datetime.now()
            current_number_in_stock = product.number_in_stock
            history.current_number_in_stock = current_number_in_stock
            history.save()
            product.save()

            return render(request, 'home.html')
    else:
        form = import_export_form()
    return render(request, 'import_export.html', {'form': form})