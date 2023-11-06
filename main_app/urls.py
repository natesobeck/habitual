from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('habits/', views.habit_index, name='habit-index'),
  path('habits/<int:pk>/', views.HabitDetail.as_view(), name='habit-detail'),
  path('habits/create/', views.HabitCreate.as_view(), name='habit-create'),
  path('habits/<int:pk>/update/', views.HabitUpdate.as_view(), name='habit-update'),
  path('habits/<int:pk>/delete', views.HabitDelete.as_view(), name='habit-delete'),
  path('habits/<int:habit_id>/increase_streak/', views.increase_streak, name='increase-streak'),
  path('habits/<int:habit_id>/reset_streak/', views.reset_streak, name='reset-streak'),
  path('accounts/signup/', views.signup, name='signup')
]