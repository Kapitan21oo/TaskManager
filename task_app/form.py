from django import forms
from .models import *


class TaskForm(forms.Form):
    name = forms.CharField(label='Введи название задачи', max_length=156)
    description = forms.CharField(label='Введи описание задачи', max_length=156)







class TaskEditForm(forms.Form):
    name = forms.CharField(label='Введи название задачи', max_length=156)
    description = forms.CharField(label='Введи описание задачи', max_length=156)