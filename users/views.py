from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import ProfileForm

def user_login(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def user_account(request):
    profile = request.user.profile
    context = {
        "profile": profile,
    }
    return render(
        request,
        "users/account.html",
        context,
    )

def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'users/account_form.html', context)

def user_profile(request, pk):
    profile=UserProfile.objects.get(id=pk)
    context={'user':profile}
    return render(request, 'users/user_profile.html', context)
    
def user_account(request):
    profile = request.user.profile
    context = {'profile': profile}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def profiles(request):
    return render(request, 'users/profiles.html')