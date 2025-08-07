from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('loginPage/', views.login_view, name='loginPage'),
    path('', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]