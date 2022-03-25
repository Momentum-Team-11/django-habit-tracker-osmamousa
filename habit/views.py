import imp
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import Habit, User, Record
# from .forms import HabitForm, RecordFrom

# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect ("home.html")
    else:
        return render(request, "login.html")

def home(request):
    habits = Habit.objects.all()
    return render (request, "home.html",)