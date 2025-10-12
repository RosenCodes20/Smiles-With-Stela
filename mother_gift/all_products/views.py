from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from mother_gift.all_products.forms import AddProductForm
from mother_gift.all_products.function_helper import paginator_function_helper
from mother_gift.all_products.models import AllProducts
from mother_gift.common.forms import SearchForm


# Create your views here.

def all_products(request):

    all_products_queryset = AllProducts.objects.all()

    if request.user.is_authenticated:
        if 'product' in request.GET:
            product = request.GET.get('product')
            all_products_queryset = all_products_queryset.filter(product_description__icontains=product)

    all_products_queryset = paginator_function_helper(request, all_products_queryset)

    context = {
        'all_products_queryset': all_products_queryset,
    }

    return render(request, 'all-products.html', context)

def product_details(request, pk):

    product = AllProducts.objects.get(id=pk)

    split_text = product.applicable_for.split(": ")

    context = {
        'product': product,
        'split_text': split_text
    }

    return render(request, 'product-details.html', context)


@login_required
def create_products(request): # THIS PAGE WILL BE ONLY VISIBLE BY ME!!!
    form = AddProductForm(request.POST or None, request.FILES or None)

    if request.user.is_superuser:
        if form.is_valid():
            product = form.save(commit=False)

            product.user = request.user

            product.save()

            return redirect('all-products')

        context = {
            'form': form
        }

        return render(request, 'add_product.html', context)

    else:
        raise PermissionError("Sorry you can't go there! Go back as fast as you can!")

