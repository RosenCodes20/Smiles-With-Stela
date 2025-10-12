from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from mother_gift.all_products.models import AllProducts


# Create your views here.

def soaps(request):

    soaps_queryset = AllProducts.objects.filter(product_type='Сапуни')

    products_per_page = 8

    paginator = Paginator(soaps_queryset, products_per_page)

    page = request.GET.get('page')

    try:
        soaps_queryset = paginator.page(page)

    except PageNotAnInteger:
        soaps_queryset = paginator.page(1)

    except EmptyPage:
        soaps_queryset = paginator.page(paginator.num_pages)

    context = {
        'soaps_queryset': soaps_queryset
    }

    return render(request, 'soaps.html', context)