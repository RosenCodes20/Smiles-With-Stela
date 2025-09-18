from django.shortcuts import render

from mother_gift.all_products.models import AllProducts
from mother_gift.common.forms import SearchForm


# Create your views here.

def index(request):

    player_search_form = SearchForm(request.GET)
    queryset = AllProducts.objects.all()

    if request.user.is_authenticated:
        queryset = AllProducts.objects.filter(user=request.user)

    else:
        queryset = []

    if request.user.is_authenticated:
        if "all_products" in request.GET:
            product = request.GET.get('product')
            queryset = queryset.filter(product_type__icontains=product)


    context = {
        'player_search_form': player_search_form,
        'queryset': queryset
    }

    return render(request, "index.html", context)