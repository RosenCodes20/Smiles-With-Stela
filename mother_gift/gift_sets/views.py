from django.shortcuts import render

from mother_gift.all_products.function_helper import paginator_function_helper
from mother_gift.all_products.models import AllProducts


# Create your views here.

def gift_sets(request):

    gift_sets_queryset = AllProducts.objects.filter(product_type='Подаръчни комплекти')

    gift_sets_queryset = paginator_function_helper(request, gift_sets_queryset)

    context = {
        'gift_sets_queryset': gift_sets_queryset
    }

    return render(request, 'gift_sets.html', context)