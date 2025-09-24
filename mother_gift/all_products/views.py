from django.shortcuts import render

# Create your views here.

def all_products(request):

    return render(request, 'all-products.html')

def product_details(request, pk):

    return render(request, 'product-details.html')


def create_products(request): # THIS PAGE WILL BE ONLY VISIBLE BY ME!!!
    pass