from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.user_profile, name='user-profile'),
    path('github-oauth/', views.github_oauth_login, name='github-oauth-login'),
]
