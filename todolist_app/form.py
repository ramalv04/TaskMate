from django import forms
from todolist_app.models import TaskList

class TaskForm(forms.ModelForm):
    class Meta: # This is the meta class that will be used to define the model and the fields that will be used in the form
        model = TaskList
        fields = ['task', 'done']