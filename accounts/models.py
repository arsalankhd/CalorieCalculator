from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    calorie_goal = models.DecimalField(max_digits=7, decimal_places=2, default=1000.0, blank=True)

