from django import forms
from .models import *


class AddForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('task_name', 'status', 'discription', 'deadline')
        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-control' ,'placeholder':"Add Task"}),
            'status': forms.TextInput(attrs={'class': 'form-control','placeholder':"In Progress - Completed - Deleted - Not Interested"}),
            'discription': forms.TextInput(attrs={'class': 'form-control' ,'placeholder':"Discription"}),
            'deadline': forms.DateTimeInput(attrs={'class': 'form-control' ,'placeholder':"yyyy-mm-dd"}),
        }