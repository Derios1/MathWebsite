from django.shortcuts import render
from django.contrib.auth import get_user


def profile_view(request):
    user = get_user(request)
    return render(request, "user_profile/index.html")

