
from django.contrib import admin
from django.urls import path

from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewStudent/', viewStudent, name='viewStudent'),
]
