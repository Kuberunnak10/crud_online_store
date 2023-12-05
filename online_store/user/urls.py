from django.urls import path

from user.views import home_page, profile, register

urlpatterns = [
    path('', home_page, name='home'),
    path('profile/', profile, name='profile'),
    path('registration/', register, name='registration'),
]