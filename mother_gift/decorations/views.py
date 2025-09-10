from django.shortcuts import render

# Create your views here.

def decorations(request):

    return render(request, 'decorations.html')