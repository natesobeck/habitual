from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

CATEGORIES = (
  ('L', 'Lifestyle'),
  ('H', 'Home'),
  ('W', 'Work'),
  ('R', 'Personal Relationships'),
  ('F', 'Health & Fitness'),
  ('B', 'Hobbies'),
  ('E', 'Environmental'),
  ('M', 'Miscellaneous')
)

class Habit(models.Model):
  habit = models.CharField(max_length=100)
  category = models.CharField(
    max_length=1,
    choices=CATEGORIES,
    default=CATEGORIES[0][0]
  )
  description = models.TextField()
  current_streak = models.IntegerField(default=0)
  best_streak = models.IntegerField(default=0)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.habit
  
  def get_absolute_url(self):
    return reverse('habit-detail', kwargs={'pk': self.id})