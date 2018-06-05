from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# def index(request):
#     if request.method == 'POST':
#         # if post, then authenticate (user submitted username and password)
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             u = form.cleaned_data['username']
#             p = form.cleaned_data['password']
#             user = authenticate(username=u, password=p)
#             if user is not None:
#                 if user. is_active:
#                     login(request, user)
#                     return HttpResponseRedirect('/')
#                 else:
#                     print("The account has been disabled.")
#             else:
#                 print("The username and/or password is incorrect.")
#     else:
#         form = LoginForm()
#         return render(request, 'login.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def signout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def profile_view(request, username):
    user = User.objects.get(username=username)
    # cats = Cat.objects.filter(user=user)
    return render(request, 'profile.html', {'user': user})


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            e = form.cleaned_data['email']
            p = form.cleaned_data['password']
            # user = User.objects.create_user(ln, fn, u, e, p)
            user = User.objects.create_user(u, e, p)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})
        # return HttpResponse('signup.html')


def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def entries_view(request, username):
    return render(request, 'entries.html')