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
            'page': 'New Movie',
            'title': 'Create Movie',
            'years': range(current_year - 20, current_year + 2),
            'categories': [
                {'id': 1, 'name': 'Love story'},
                {'id': 2, 'name': 'Horror'},
                {'id': 3, 'name': 'Action'},
                {'id': 4, 'name': 'Blue Movie'}
            ],
            'active': 'new_movie'
        }
        return render(request, 'library/new_movie.html', context)
    
    # def post(self, request):
        