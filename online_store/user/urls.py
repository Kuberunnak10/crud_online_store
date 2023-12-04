from django.urls import path

from user.views import home_page, profile

urlpatterns = [
    path('', home_page, name='home'),
    path('profile/', profile, name='profile'),

]