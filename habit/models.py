from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class User(AbstractBaseUser):
    def __repr__(self):
        return f"<User username={self.username}>"
    
    def __str__(self):
        return self.username


class Habit(models.Model):
    habit_name = models.CharField(max_length=50)
    habit_goal = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="habit_user"
    )


class record(models.Model):
    date = models.DateField(auto_now_add=datetime.now)
    habit = models.ForeignKey(
        Habit, on_delete=models.CASCADE, null=True, blank=True, related_name="habit"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="habit_record_user"
    )

    class meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'date'], name='only_once')
        ]