from django.shortcuts import render

from mother_gift.all_products.function_helper import paginator_function_helper
from mother_gift.all_products.models import AllProducts


# Create your views here.

def decorations(request):

    decorations_queryset = AllProducts.objects.filter(product_type='Украси')

    if request.user.is_authenticated:
        if 'product' in request.GET:
            product = request.GET.get('product')
            decorations_queryset = decorations_queryset.filter(product_description__icontains=product)
            print(decorations_queryset)

    decorations_queryset = paginator_function_helper(request, decorations_queryset)

    context = {
        'decorations_queryset': decorations_queryset
    }

    return render(request, 'product/decorations.html', context)