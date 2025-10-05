from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('modules/', views.modules, name='modules'),
    path('quizzes/', views.quizzes, name='quizzes'),

]
