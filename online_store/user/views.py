from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'home/home.html')


@login_required(login_url='/user/login')
def profile(request):
    return render(request, 'user/profile.html')
