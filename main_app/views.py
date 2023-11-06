from django.shortcuts import render, redirect
from .models import Habit
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
  template_name = 'home.html'

class HabitList(LoginRequiredMixin, ListView):
  model = Habit

class HabitDetail(LoginRequiredMixin, DetailView):
  model = Habit

class HabitCreate(LoginRequiredMixin, CreateView):
  model = Habit
  fields = ['habit', 'category', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class HabitUpdate(LoginRequiredMixin, UpdateView):
  model = Habit
  fields = ['habit', 'category', 'description']

class HabitDelete(LoginRequiredMixin, DeleteView):
  model = Habit
  success_url = '/habits/'

@login_required
def increase_streak(request, habit_id):
  habit = Habit.objects.get(id=habit_id)
  habit.current_streak += 1
  if habit.current_streak > habit.best_streak:
    habit.best_streak = habit.current_streak
  habit.save()
  return redirect('habit-detail', pk=habit_id)

@login_required
def reset_streak(request, habit_id):
  habit=Habit.objects.get(id=habit_id)
  habit.current_streak = 0
  habit.save()
  return redirect('habit-detail', pk=habit_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('habit-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)