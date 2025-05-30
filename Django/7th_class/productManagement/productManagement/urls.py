
from django.contrib import admin
from django.urls import path
from productManagement.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('books/', books, name='books'),
    path('user/', user, name='user'),
    path('studentList/', studentList, name='studentList'),
    path('addStudent/', addStudent, name='addStudent'),
    path('addBook/', addBook, name='addBook'),
]
