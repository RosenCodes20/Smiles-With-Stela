from django.shortcuts import render

from mother_gift.all_products.models import AllProducts
from mother_gift.common.forms import SearchForm


# Create your views here.

def index(request):

    player_search_form = SearchForm(request.GET)
    queryset = AllProducts.objects.all()

    if request.user.is_authenticated:
        queryset = AllProducts.objects.filter()

    return render(request, "index.html",)