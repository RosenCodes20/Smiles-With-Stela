from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from mother_gift.all_products.function_helper import paginator_function_helper
from mother_gift.all_products.models import AllProducts


# Create your views here.

def soaps(request):

    soaps_queryset = AllProducts.objects.filter(product_type='Сапуни')

    if request.user.is_authenticated:
        if 'product' in request.GET:
            product = request.GET.get('product')
            soaps_queryset = soaps_queryset.filter(product_description__icontains=product)
            print(soaps_queryset)

    soaps_queryset = paginator_function_helper(request, soaps_queryset)


    context = {
        'soaps_queryset': soaps_queryset
    }

    return render(request, 'product/soaps.html', context)