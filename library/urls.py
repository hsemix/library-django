from django.urls import path
from . import views, libviews
from .libviews import LoginView, HomeView, AdminView, MovieView, BuyerView

urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.login, name='login'),
    path('login/', libviews.LoginView.View.as_view(), name='login'),
    path('home/', libviews.HomeView.View.as_view(), name='home'),
    path('user/new/', libviews.AdminView.View.as_view(), name='user.new'),
    # path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('movie/new/', libviews.MovieView.View.as_view(), name='movie.new'),
    path('buyer/new/', libviews.BuyerView.View.as_view(), name='buyer.new'),
    # path('test/', libviews.TestView.as_view(), name='test'),
    # path('test2/', Test.Test.as_view(), name='test2'),
]