from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('habits/', views.HabitList.as_view(), name='habit-index'),
  path('habits/<int:pk>/', views.HabitDetail.as_view(), name='habit-detail'),
  path('habits/create/', views.HabitCreate.as_view(), name='habit-create')
]