from django.urls import path     
from . import views
urlpatterns = [
    path('', views.begin_game),	   
    path('process_money', views.process_money),	 
    path('reset', views.reset),	 
]