from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('new_search/', views.new_search_view, name='new_search'),

]