from django.urls import path
from todolist_app import views

urlpatterns = [
    path('', views.todolist, name='todolist'), # This is the URL for the main page of the app
    path('delete/<task_id>', views.delete_task, name='delete_task'), # This is the URL for the delete task function
    path('edit/<task_id>', views.edit_task, name='edit_task'), # This is the URL for the edit task function
    path('complete/<task_id>', views.complete_task, name='complete_task'), # This is the URL for the complete task function
    path('pending/<task_id>', views.pending_task, name='pending_task'), # This is the URL for the pending
]