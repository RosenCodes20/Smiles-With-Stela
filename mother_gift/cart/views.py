from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from mother_gift.all_products.models import AllProducts
from mother_gift.cart.models import Cart


# Create your views here.

@login_required
def cart(request):

    return render(request, 'cart.html')

def add_to_cart(request, pk):
    product = AllProducts.objects.get(id=pk)

    Cart.objects.create(
        product_image_cart=product.product_image,
        product_description_cart=product.product_description,
        product_price_cart=product.product_price,
        user_cart=request.user,
    )

    return redirect(request.META['HTTP_REFERER'])