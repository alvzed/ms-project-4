from django.shortcuts import render, redirect


# Create your views here.
def library(request):
    """ a view to to return the landing page """
    if request.user.is_authenticated:
        return render(request, 'library/library.html')
    else:
        return redirect('/')
