from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Create your views here.

@login_required
def cart(request):

    return render(request, 'cart.html')


def add_to_cart(request, pk):
    pass