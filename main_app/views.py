from django.shortcuts import render, redirect
from .models import Habit
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView

class Home(LoginView):
  template_name = 'home.html'

class HabitList(ListView):
  model = Habit

class HabitDetail(DetailView):
  model = Habit

  def increase_streak(self):
    print('hello')

class HabitCreate(CreateView):
  model = Habit
  fields = ['habit', 'category', 'description']

class HabitUpdate(UpdateView):
  model = Habit
  fields = ['habit', 'category', 'description']

class HabitDelete(DeleteView):
  model = Habit
  success_url = '/habits/'

def increase_streak(request, habit_id):
  habit = Habit.objects.get(id=habit_id)
  habit.current_streak += 1
  if habit.current_streak > habit.best_streak:
    habit.best_streak = habit.current_streak
  habit.save()
  return redirect('habit-detail', pk=habit_id)

def reset_streak(request, habit_id):
  habit=Habit.objects.get(id=habit_id)
  habit.current_streak = 0
  habit.save()
  return redirect('habit-detail', pk=habit_id)