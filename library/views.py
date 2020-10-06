from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q, F
from .models import Video, Category, Review
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from .forms import ReviewForm


# Create your views here.
def library(request):
    """ a view to to return the landing page """
    if not request.user.is_authenticated:
        return redirect('/')

    user = request.user
    user_profile = UserProfile.objects.get_or_create(user=user)

    videos = Video.objects.all()
    categories = Category.objects.all()
    # Genre is used to filter between categories
    genre = None
    current_category = None
    # Query is used for the search funtion
    query = None
    query_count = None
    # this is used in case the query turns up empty
    search_message = None

    # Gets the 5 most viewed videos from the library
    most_viewed = videos.order_by('views').reverse()[0:5]
    # Gets the 3 most clicked cartegories from the library
    popular_categories = categories.order_by('clicks').reverse()[0:3]
    # These get the 5 most viewed videos in the 3 most popular categories
    top_category_videos = videos.filter(category=popular_categories[0])\
        .order_by('views').reverse()[0:5]
    second_category_videos = videos.filter(category=popular_categories[1])\
        .order_by('views').reverse()[0:5]
    third_category_videos = videos.filter(category=popular_categories[2])\
        .order_by('views').reverse()[0:5]

    if request.GET:
        if 'genre' in request.GET:
            genre = request.GET['genre']

            videos = videos.filter(category__slug__iexact=genre)

            # The statements below increment a click counter in the model
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
            query_count = videos.count()

            if not videos.exists():
                search_message = 'No matches'

    context = {
        'videos': videos,
        'most_viewed': most_viewed,
        'categories': categories,
        'current_category': current_category,
        'popular_categories': popular_categories,
        'top_category_videos': top_category_videos,
        'second_category_videos': second_category_videos,
        'third_category_videos': third_category_videos,
        'search_term': query,
        'query_count': query_count,
        'search_message': search_message,
        'user_profile': user_profile,
    }

    return render(request, 'library/library.html', context)


def player(request, video_id):
    """ a view to return the video player for individual videos """
    if not request.user.is_authenticated:
        return redirect('/')

    video = get_object_or_404(Video, pk=video_id)

    video.views = F('views') + 1
    video.save()

    # Current session user
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    nickname = request.user.username

    """ This will return all the reviews for the video """
    reviews = Review.objects.all().filter(video=video_id)

    """ From here on is what happend when you submit a review """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_review = Review(
                rating=data['rating'],
                description=data['description'],
                video=video,
                user=user
            )
            new_review.save()

    context = {
        'video': video,
        'reviews': reviews,
        'user': user,
        'nickname': nickname,
        'form': ReviewForm,
    }

    return render(request, 'library/player.html', context)
