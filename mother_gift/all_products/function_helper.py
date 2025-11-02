from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginator_function_helper(request, queryset):
    products_per_page = 8

    paginator = Paginator(queryset, products_per_page)

    page = request.GET.get('page')

    try:
        queryset = paginator.page(page)

    except PageNotAnInteger:
        queryset = paginator.page(1)

    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    return queryset