from django.shortcuts import render

from mother_gift.all_products.models import AllProducts


# Create your views here.

def soaps(request):

    soaps_queryset = AllProducts.objects.filter(product_type='Сапуни')

    context = {
        'soaps_queryset': soaps_queryset
    }

    return render(request, 'soaps.html', context)