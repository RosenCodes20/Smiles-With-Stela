from django.shortcuts import render

# Create your views here.

def soaps(request):

    return render(request, 'soaps.html')