from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.models import User
from django.db.models import Q

class View(View):
    def get(self, request):
        context = {
            'page': 'Register',
            'title': 'Library',
            'active': 'new_admin'
        }
        return render(request, 'library/user.html', context)
    
    def post(self, request):
        context = {
            'form': 'form'
        }
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        # phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password_confirmation')
        if first_name == '' or last_name == '' or email == '' or username == '' or password == '':
            return JsonResponse({ 'app_status': False, 'message': "All fields are required to proceed!" })
        else:
            if (confirm_password != password):
                return JsonResponse({ 'app_status': False, 'message': "Password confirmation doesnot match!" })
            else:
                if len(User.objects.filter(Q(username=username) | Q(email=email))) > 0:
                    return JsonResponse({ 'app_status': False, 'message': "Email or Username already exists!" })
                else:
                    user = User.objects.create_user(username, email, password)
                    # user.phone = phone
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()
                    return JsonResponse({ 'app_status': True, 'status_code': 2, 'message': "User created successfully" })