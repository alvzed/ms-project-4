from django.shortcuts import render


# Create your views here.
def index(request):
    """ a view to to return the landing page """
    return render(request, 'landing/index.html')
