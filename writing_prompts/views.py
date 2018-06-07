from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, SignupForm, EntryForm
from django.contrib.auth.models import User
from .models import Entry
from django.contrib.auth import authenticate, login, logout
import datetime
now = datetime.datetime.now()

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
    entries = Entry.objects.filter(author=user)
    form = EntryForm()
    return render(request, 'profile.html', {'user': user, 'entries': entries, 'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            e = form.cleaned_data['email']
            p = form.cleaned_data['password']
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


# def post_entry(request):
#     form=EntryForm(request.POST)
#     if form.is_valid():
#         new_entry = form.save(commit=False)
#         new_entry.user=request.user
#         new_entry.save()
#     return HttpResponseRedirect('/')

def post_entry(request):
    draft = request.POST['draft']
    notes = request.POST['notes']
    prompt = request.POST['prompt']
    pub_date = now.strftime("%Y-%m-%d")
    author = request.user
    new_entry = Entry.objects.create(draft=draft, notes=notes, prompt=prompt, pub_date=pub_date, author=author)
    print(new_entry)
    return HttpResponseRedirect('/')
