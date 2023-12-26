from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from user.forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request,
                  'registration/registration.html',
                  {'form': form})


def home_page(request):
    return render(request, 'home/home.html')


@login_required(login_url='/user/login')
def profile(request):
    return render(request, 'user/profile.html')


def contacts_page(request):
    return render(request, 'home/contacts.html')
