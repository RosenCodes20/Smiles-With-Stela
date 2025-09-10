from django.shortcuts import render

# Create your views here.

def gift_sets(request):

    return render(request, 'gift_sets.html')