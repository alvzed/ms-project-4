from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q, F
from .models import Video, Category


# Create your views here.
def library(request):
    """ a view to to return the landing page """
    if not request.user.is_authenticated:
        return redirect('/')

    videos = Video.objects.all()
    categories = Category.objects.all()
    genre = None
    query = None

    most_viewed = videos.order_by('views').reverse()[0:4]

    if request.GET:
        if 'genre' in request.GET:
            genre = request.GET['genre']

            videos = videos.filter(category__slug__iexact=genre)

            current_category = categories.get(slug=genre)
            current_category.clicks = F('clicks') + 1
            current_category.save()

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                print('Search query empty')
                return redirect(reverse('library'))
            queries = Q(title__icontains=query) | \
                Q(description__icontains=query)
            videos = videos.filter(queries)

    context = {
        'videos': videos,
        'categories': categories,
        'search_term': query,
        'most_viewed': most_viewed,
    }

    return render(request, 'library/library.html', context)


def player(request, video_id):
    """ a view to return the video player for individual videos """
    if not request.user.is_authenticated:
        return redirect('/')

    video = get_object_or_404(Video, pk=video_id)

    video.views = F('views') + 1
    video.save()

    context = {
        'video': video,
    }

    return render(request, 'library/player.html', context)
