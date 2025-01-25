from django.contrib import admin
from django.urls import path, include
from todolist_app import views as tl_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tl_views.index, name='index'), # This is the URL for the main page of the app
    path('todolist/', include('todolist_app.urls')), # This is the URL for the main page of the app
    path('account/', include('users_app.urls')), # This is the URL for the main page of the app
    path('contact/', tl_views.contact, name='contact'), # This is the URL for the contact page
    path('about/', tl_views.about, name='about'), # This is the URL for the about page
]
