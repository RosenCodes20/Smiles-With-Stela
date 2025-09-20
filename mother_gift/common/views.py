from django.core.mail import send_mail
from django.shortcuts import render

from mother_gift.all_products.models import AllProducts
from mother_gift.common.forms import SearchForm, SendInfoForm


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

    if request.method == "GET":
        message_form = SendInfoForm()

    else:
        message_form = SendInfoForm(request.POST)

        if message_form.is_valid():

            send_mail(
                f'Съобщение до мен от: {message_form.cleaned_data["name"]}',
                message_form.cleaned_data['message'],
                "rrirrirri08@gmail.com",
                [message_form.cleaned_data['email']],
                fail_silently=False
            )

    context = {
        'player_search_form': player_search_form,
        'queryset': queryset,
        'message_form': message_form
    }

    return render(request, "index.html", context)