from attr import fields
from django import forms
from .models import Habit, Record



class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'name',
            'goal',
        ]

class RecordFrom(forms.ModelForm):
    date = forms.DateField(input_formats=["%m/%d/%Y"])

    class Meta:
        model = Record
        fields = ["date"]