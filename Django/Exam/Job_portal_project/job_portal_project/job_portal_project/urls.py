
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_auth_app.urls')),
    path('employer/', include('employer_app.urls')),
]
