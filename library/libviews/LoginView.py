from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as user_login, logout as user_logout

class View(View):
    def get(self, request):
        context = {
            'form': 'form',
            'active': 'login'
        }
        return render(request, 'library/login.html', context)
    
    def post(self, request):
        context = {
            'form': 'form'
        }
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '' and password == '':
            return JsonResponse({ 'app_status': False, 'message': "All fields are required to proceed!" })
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                user_login(request, user)
                # return HttpResponseRedirect("/library/home/")
                return JsonResponse({ 'app_status': True, 'status_code': 1, 'redirect_url': "/library/home/" })
            else:
                # return HttpResponse(password)
                return JsonResponse({ 'app_status': False, 'message': "Wrong Username and Password combination" })