from django.shortcuts import render

from mother_gift.all_products.function_helper import paginator_function_helper
from mother_gift.all_products.models import AllProducts


# Create your views here.

def decorations(request):

    decorations_queryset = AllProducts.objects.filter(product_type='Украси')

    decorations_queryset = paginator_function_helper(request, decorations_queryset)

    context = {
        'decorations_queryset': decorations_queryset
    }

    return render(request, 'decorations.html', context)