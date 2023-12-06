from django.urls import path

from user.views import home_page, profile, register, contacts_page

urlpatterns = [
    path('', home_page, name='home'),
    path('profile/', profile, name='profile'),
    path('registration/', register, name='registration'),
    path('contacts/', contacts_page, name='contacts')
]