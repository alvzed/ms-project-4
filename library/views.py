from django.shortcuts import render, redirect, get_object_or_404
from .models import Video, Category


# Create your views here.
def library(request):
    """ a view to to return the landing page """
    if not request.user.is_authenticated:
        return redirect('/')

    videos = Video.objects.all()
    categories = Category.objects.all()

    context = {
        'videos': videos,
        'categories': categories,
    }

    return render(request, 'library/library.html', context)


def player(request, video_id):
    """ a view to return the video player for individual videos """
    if not request.user.is_authenticated:
        return redirect('/')

    video = get_object_or_404(Video, pk=video_id)

    context = {
        'video': video,
    }

    return render(request, 'library/player.html', context)


def category(request, category):
    if not request.user.is_authenticated:
        return redirect('/')

    context = {
        'category': category,
    }

    return render(request, 'library/category.html', context)
