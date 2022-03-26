from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"
    
    def __str__(self):
        return self.username


class Habit(models.Model):
    name = models.CharField(max_length=50)
    goal = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="habits"
    )


class Record(models.Model):
    date = models.DateField(auto_now_add=datetime.now)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="habit_record_user"
    )
    goal_complete = models.BooleanField(default=False)

    class meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'date'], name='only_once')
        ]