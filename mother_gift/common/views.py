from django.core.mail import send_mail
from django.shortcuts import render, redirect

from mother_gift.all_products.models import AllProducts
from mother_gift.common.forms import SearchForm, SendInfoForm, SubscribeForNewsForm


# Create your views here.

def index(request):

    player_search_form = SearchForm(request.GET)
    queryset = AllProducts.objects.all()

    if request.user.is_authenticated:
        if "product" in request.GET:
            product = request.GET.get('product')
            queryset = queryset.filter(product_description__icontains=product)

    if request.method == "GET":
        message_form = SendInfoForm()

    else:
        message_form = SendInfoForm(request.POST)

        if message_form.is_valid():

            send_mail(
                f'Съобщение до мен от: {message_form.cleaned_data["name"]}',
                message_form.cleaned_data['message'],
                message_form.cleaned_data['email'],
                ["rrirrirri08@gmail.com"],
                fail_silently=False
            )

    decorated_book = AllProducts.objects.filter(product_description='Стилна декорирана книга').first()
    elephant_soap = AllProducts.objects.get(product_description='Сапун във формата на слон')
    elegant_cups_with_soaps = AllProducts.objects.get(product_description='Сапунени цветя в чашки')

    context = {
        'player_search_form': player_search_form,
        'queryset': queryset,
        'message_form': message_form,
        'decorated_book': decorated_book,
        'elephant_soap': elephant_soap
    }

    return render(request, "index.html", context)


def subscribe_for_news(request):
    sign_for_news_form = SubscribeForNewsForm(request.POST or None)

    if sign_for_news_form.is_valid():
        if request.user.is_authenticated:
            send_mail(
                f"Абониране за новини от: {sign_for_news_form.cleaned_data['email']}",
                'Ти успешно се абонира за нашите новини! Очаквай имейл при появата на нов продукт!',
                'rrirrirri08@gmail.com',
                [sign_for_news_form.cleaned_data['email']],
                fail_silently=False
            )

            send_mail(
                f"Абониране за новини от: {sign_for_news_form.cleaned_data['email']}",
                'Нов абониран човек за новините на нашия магазин',
                'rrirrirri08@gmail.com',
                ['rrirrirri08@gmail.com'],
                fail_silently=False
            )

        else:
            return redirect('register')

    return redirect(request.META['HTTP_REFERER'])