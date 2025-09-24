from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from mother_gift.all_products.forms import AddProductForm


# Create your views here.

def all_products(request):

    return render(request, 'all-products.html')

def product_details(request, pk):

    return render(request, 'product-details.html')


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