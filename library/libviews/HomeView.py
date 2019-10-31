from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as user_login, logout as user_logout

class View(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/login/")
        else:
            context = {
                'page': 'Dashboard',
                'title': 'Library',
                'active': 'dashboard'
            }
            return render(request, 'library/home.html', context)
    
    # def post(self, request):
        