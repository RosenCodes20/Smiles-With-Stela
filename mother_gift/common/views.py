import smtplib
import ssl
from email.header import Header
from email.mime.text import MIMEText

from decouple import config
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from mother_gift.all_products.models import AllProducts
from mother_gift.common.forms import SearchForm, SendInfoForm, SubscribeForNewsForm

EMAIL = "rrirrirri08@gmail.com"
PASSWORD = config("GOOGLE_PASSWORD")

# Create your views here.

def send_mail_ssl(subject, message, from_email, recipient_list):
    """
    Sends email using Gmail SMTP_SSL with Unicode support.
    """
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(EMAIL, PASSWORD)
        for recipient in recipient_list:
            msg = MIMEText(message, "plain", "utf-8")
            msg['Subject'] = Header(subject, "utf-8")
            msg['From'] = from_email
            msg['To'] = recipient
            server.sendmail(from_email, recipient, msg.as_string())

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
            subject = f'Съобщение до мен от: {message_form.cleaned_data["name"]}'
            message = message_form.cleaned_data['message']
            from_email = message_form.cleaned_data['email']

            send_mail_ssl(subject, message, from_email, ["rrirrirri08@gmail.com"])

    decorated_book = AllProducts.objects.filter(product_description='Стилна декорирана книга').first()
    elephant_soap = AllProducts.objects.get(product_description='Сапун във формата на слон')
    elegant_cups_with_soaps = AllProducts.objects.get(product_description='Сапунени цветя в чашки')

    context = {
        'player_search_form': player_search_form,
        'queryset': queryset,
        'message_form': message_form,
        'decorated_book': decorated_book,
        'elephant_soap': elephant_soap,
        'elegant_cups_with_soaps': elegant_cups_with_soaps,
    }

    return render(request, "index.html", context)


def subscribe_for_news(request):
    sign_for_news_form = SubscribeForNewsForm(request.POST or None)

    if sign_for_news_form.is_valid():
        if request.user.is_authenticated:
            subject = f'Абониране за новини от: {sign_for_news_form.cleaned_data['email']}'
            message = 'Ти успешно се абонира за нашите новини! Очаквай имейл при появата на нов продукт!'
            from_email = "rrirrirri08@gmail.com"
            send_mail_ssl(subject, message, from_email, [sign_for_news_form.cleaned_data['email']])

            subject = f'Абониране за новини от: {sign_for_news_form.cleaned_data['email']}'
            message = 'Нов абониран човек за новините на нашия магазин'
            from_email = "rrirrirri08@gmail.com"
            send_mail_ssl(subject, message, from_email, 'rrirrirri08@gmail.com')

        else:
            return redirect('register')

    return redirect(request.META['HTTP_REFERER'])