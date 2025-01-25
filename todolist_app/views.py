from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required 
def todolist(request): # This is the view function that will be called when the URL is visited
    if request.method == 'POST':
        form = TaskForm(request.POST or None) # This will create a form object and will populate it with the data that is in the request.POST dictionary
        if form.is_valid():
            form.save(commit=False).owner = request.user
            form.save()
        messages.success(request, ('New Task Added!'))
        return redirect('todolist') # This will redirect the user to the todolist page after the form has been submitted
    else:    
        all_tasks = TaskList.objects.filter(owner=request.user) # This will get all the tasks from the database
        paginator = Paginator(all_tasks, 8) # Show 5 tasks per page
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
    return render(request, 'todolist.html', {'all_tasks':all_tasks}) # This will render the todolist.html template

@login_required
def delete_task(request, task_id): # This is the view function that will be called when the URL is visited
    task = TaskList.objects.get(pk=task_id) # This will get the task from the database that has the primary key of task_id
    if task.owner == request.user:
        task.delete() # This will delete the task from the database
    else:
        messages.error(request, ('Access Restricted, You Are Not Allowed.'))
    return redirect('todolist') # This will redirect the user to the todolist page after the task has been deleted

@login_required
def edit_task(request, task_id):
    if request.method == 'POST':
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task) # This will create a form object and will populate it with the data that is in the request.POST dictionary
        if form.is_valid():
            form.save()
        
        messages.success(request, ('Task Edited!'))
        return redirect('todolist') 
    else:    
        task_obj = TaskList.objects.get(pk=task_id)
    return render(request, 'edit.html', {'task_obj':task_obj})

@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, ('Access Restricted, You Are Not Allowed.'))
    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, ('Access Restricted, You Are Not Allowed.'))
    return redirect('todolist')

def contact(request): 
    context = {'contact_text':'Welcome to contact page',} 
    return render(request, 'contact.html', context) 

def about(request): 
    context = {'about_text':'Welcome to about us page',} 
    return render(request, 'about.html', context) 

def index(request): 
    context = {'index_text':'Welcome to index page',} 
    return render(request, 'index.html', context) 