from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    """ a view to to return the landing page """
    if request.user.is_authenticated:
        return redirect('/library/')
    else:
        return render(request, 'landing/index.html')
