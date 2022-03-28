import imp
from ast import If
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Habit, User, Record
from .forms import HabitForm, RecordForm
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


@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save()

            return redirect('home')
    else:
        form = HabitForm()

        return render(request,'habit/add_habit.html', {'form': form})


@login_required
def delete_habit(request, habit_pk):
    habit = get_object_or_404(habit, pk=habit_pk)
    if request.method == 'POST':
        habit.delete()
        return redirect(to='home')
    return render(request, "habit/delete_habit.html", {"habit": habit})


@login_required
def edit_habit(request, habit_pk):
    habit = get_object_or_404(habit, pk=habit_pk)
    if request.method == 'GET':
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect(to='home')

    return render(request, "habit/edit_habit.html", {
        "form": form,
        "habit": habit
    })


@login_required
def add_record(request, pk):
    habit = get_object_or_404(habit, pk=pk)
    if request.method == 'GET':
        form = RecordForm()
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.habit = habit
            record.save()
            return redirect(to='home', pk=habit.pk)

    return render(request, "habit/add_record.html", {"form": form, "habit": habit})

@login_required
def edit_record(request, record_pk):
    record = get_object_or_404(record, pk=record_pk)
    if request.method == 'GET':
        form = RecordForm(instance=record)
    else:
        form = RecordForm(data=request.POST, instance=record)
        if form.is_valid():
            habit_pk = record.habit.pk
            form.save()
            return redirect(to='card_list', pk=habit_pk)

    return render(request, "habit/edit_record.html", {
        "form": form,
        "record": record
    })