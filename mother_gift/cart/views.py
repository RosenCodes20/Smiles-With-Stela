import datetime
import smtplib
import ssl
from email.header import Header
from email.mime.text import MIMEText

from decouple import config
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from mother_gift.accounts.models import User
from mother_gift.all_products.models import AllProducts, BoughtProducts
from mother_gift.cart.forms import CreateCartForm
from mother_gift.cart.models import Cart, OrderUserModel


# Create your views here.

@login_required
def cart(request, pk):
    cart_queryset_for_user = Cart.objects.filter(user_cart_id=pk)
    product_prices = []

    for product in cart_queryset_for_user:
        product_prices.append(float(product.product_price_cart))

    sum_of_products = sum(product_prices)

    sum_with_delivery = sum_of_products + 3

    context = {
        'cart_queryset_for_user': cart_queryset_for_user,
        'sum_of_products': sum_of_products,
        'sum_with_delivery': sum_with_delivery,
    }

    return render(request, 'product/../../templates/cart/cart.html', context)

@login_required
def add_to_cart(request, pk):
    product = AllProducts.objects.get(id=pk)

    Cart.objects.create(
        product_image_cart=product.product_image,
        product_description_cart=product.product_description,
        product_price_cart=product.product_price,
        user_cart=request.user,
    )

    return redirect(request.META['HTTP_REFERER'])

def remove_product_from_cart(request, pk):
    product = Cart.objects.get(id=pk)

    product.delete()

    return redirect(request.META['HTTP_REFERER'])

@login_required
def create_deliver_cart(request):
    form = CreateCartForm(request.POST or None)
    user = User.objects.get(id=request.user.id)
    products = Cart.objects.filter(user_cart_id=user.id)

    filtered_products_descriptions = [p.product_description_cart for p in products]
    products_prices = [float(p.product_price_cart) for p in products]

    sum_prices = []

    for product in products:
        sum_prices.append(float(product.product_price_cart))

    if request.method == "POST":
        if form.is_valid():
            finish_cart = form.save(commit=False)

            finish_cart.user_finish_cart = request.user

            finish_cart.save()

            EMAIL = "rrirrirri08@gmail.com"
            PASSWORD = config("GOOGLE_PASSWORD")

            def send_mail_ssl(subject, message, recipient_list):
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(EMAIL, PASSWORD)
                    for recipient in recipient_list:
                        msg = MIMEText(message, "plain", "utf-8")
                        msg['Subject'] = Header(subject, "utf-8")
                        msg['From'] = EMAIL
                        msg['To'] = recipient

                        server.sendmail(EMAIL, recipient, msg.as_string())
            subject = (
                f'Поръчка от: {user.email}, {user.profile.get_profile_full_name()} '
                f'На дата: {datetime.datetime.now()}'
            )

            message = (
                f'{user.email} си поръча: {filtered_products_descriptions}\n'
                f'На цени {products_prices}\n'
                f'На цена: {float(sum(sum_prices))}лв/{float(sum(sum_prices) / 1.95583):.2f}евро\n'
                f'До град: {finish_cart.town_name}\n'
                f'До адрес: {finish_cart.speedy_address}\n'
                f"Име и фамилия: {form.cleaned_data['first_name']} {form.cleaned_data['last_name']}\n"
                f"Въведен имейл: {form.cleaned_data['address_email']}"
            )

            send_mail_ssl(subject, message, ['rrirrirri08@gmail.com'])

            cart_objects = Cart.objects.filter(user_cart_id=request.user.id)

            for cart in cart_objects:
                got_order = OrderUserModel.objects.create(
                    product_description_order_user=cart.product_description_cart,
                    date=datetime.date.today(),
                    status='В процес',
                    user_order=request.user,
                )

                BoughtProducts.objects.create(
                    product=got_order,
                    user=request.user
                )

                cart.delete()

            return redirect('thanks-for-choosing')

    context = {
        'form': form
    }

    return render(request, 'product/../../templates/cart/create_cart.html', context)

def thanks_for_choosing(request):

    return render(request, 'thanks/thanks_for_choosing_this_page.html')