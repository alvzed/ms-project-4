from django.shortcuts import render, redirect
from .models import UserProfile


# Create your views here.
def userpage(request):
    if not request.user.is_authenticated:
        return redirect('/')

    user = request.user
    user_profile = UserProfile.objects.get(user=user)

    context = {
        'user_profile': user_profile,
        'user': user,
    }

    return render(request, 'user_profile/userpage.html', context)
