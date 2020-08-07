from django.shortcuts import render


# Create your views here.
def library(request):
    """ a view to to return the landing page """
    return render(request, 'library/library.html')
