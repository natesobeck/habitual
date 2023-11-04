from django.db import models

class Habit(models.Model):
  habit = models.CharField(max_length=100)
  category = models.CharField(max_length=100)
  description = models.TextField()
  current_streak = 0
  best_streak = 0

  def __str__(self):
    return self.habit