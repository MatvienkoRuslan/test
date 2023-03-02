from django import forms
from .models import *


class TaskForm(forms.Form):
    title = forms.CharField(max_length=255, label="Task Title")
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Description')
    completed = forms.BooleanField(required=False, initial=True, label='Completed')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = forms.ChoiceField(choices=[
        ('home', 'Home'),
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('health', 'Health'),
        ('finance', 'Finance'),
        ('education', 'Education'),
        ('leisure', 'Leisure'),
        ('other', 'Other')
    ], label='Category')

    def save(self):
        pass
