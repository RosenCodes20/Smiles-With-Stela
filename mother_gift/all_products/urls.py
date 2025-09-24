from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.static import serve

from mother_gift import settings
from mother_gift.all_products import views

urlpatterns = [
    path('', views.all_products, name='all-products'),
    path('product-details/<int:pk>/', views.product_details, name='product-details'),
    path('add-product/', views.create_products, name='add-product')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

elif not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]