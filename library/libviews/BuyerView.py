from datetime import date
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as user_login, logout as user_logout

class View(View):
    def get(self, request):
        current_year = date.today().year
        context = {
            'page': 'New Buyer',
            'title': 'Create Buyer',
            'active': 'new_buyer'
        }
        return render(request, 'library/new_buyer.html', context)
    
    # def post(self, request):
        