from django.shortcuts import render, redirect
from django.contrib.auth import get_user, authenticate, login
from user_profile.forms import RegisterForm


def profile_view(request):
    return render(request, "user_profile/index.html")


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.bio = form.cleaned_data.get('bio')
            user.save()
            # user = authenticate(username=user.username, password=raw_password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('problems')
    else:
        form = RegisterForm()
    return render(request, "registration/signup.html", {"form": form})

