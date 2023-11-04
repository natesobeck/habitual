from django.shortcuts import render
from .models import Habit
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

def home(request):
  return render(request, 'home.html')

class HabitList(ListView):
  model = Habit

class HabitDetail(DetailView):
  model = Habit

class HabitCreate(CreateView):
  model = Habit
  fields = ['habit', 'category', 'description']