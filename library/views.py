from django.shortcuts import render, redirect
from .models import Video


# Create your views here.
def library(request):
    """ a view to to return the landing page """
    if request.user.is_authenticated:
        videos = Video.objects.all()

        context = {
            'videos': videos,
        }

        return render(request, 'library/library.html', context)
    else:
        return redirect('/')
