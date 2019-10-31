from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django import forms
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login, logout as user_logout

# Create your views here.

def index(request):
    form = UserForm()
    if request.method == 'POST':
        context = {
            'form': form
        }

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        # forms.is_valid
        # if form.is_valid():
        #     username = form.cleaned_data['username']
        #     email = form.cleaned_data['email']
        #     password = form.cleaned_data['password']
        #     user = User.objects.create_user(username, email, password)
        #     user.save()
        #     return HttpResponseRedirect('/users/')
    else:
        # post = Posts.objects.get(id=id)
        context = {
            'form': form
        }
    return render(request, 'library/register.html', context)

def login(request):
    if request.method == 'POST':
        context = {
            'form': 'form'
        }
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_login(request, user)
            return HttpResponseRedirect("/library/home/")
        else:
            # return HttpResponse(password)
            return JsonResponse(context)
    else:
        context = {
            'form': 'form'
        }
    return render(request, 'library/login.html', context)

def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/library/login/")
    else:
        context = {
            'user': request.user
        }
        return render(request, 'library/home.html')

def logout(request):
    user_logout(request)
    return HttpResponseRedirect("/library/login/")