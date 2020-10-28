"""Math URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from problems.views import problems_view, problem_page_view
from user_profile.views import profile_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', problems_view),
    path('problems', problems_view, name="problems"),
    path('problems/<int:id>', problem_page_view, name="problem-details"),
    path('profile', profile_view, name="profile"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', register_view, name="register")
]
