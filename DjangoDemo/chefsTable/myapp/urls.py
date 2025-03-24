from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('drinks/<str:coffeeName>/', views.drinks)
]