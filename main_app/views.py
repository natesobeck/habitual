from django.shortcuts import render
from .models import Habit
from django.views.generic import ListView, DetailView

def home(request):
  return render(request, 'home.html')

class HabitList(ListView):
  model = Habit
  fields = '__all__'

class HabitDetail(DetailView):
  model = Habit
  fields = '__all__'