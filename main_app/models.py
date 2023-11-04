from django.db import models
from django.urls import reverse

class Habit(models.Model):
  habit = models.CharField(max_length=100)
  category = models.CharField(max_length=100)
  description = models.TextField()
  current_streak = 0
  best_streak = 0

  def __str__(self):
    return self.habit
  
  def get_absolute_url(self):
    return reverse('habit-detail', kwargs={'pk': self.id})