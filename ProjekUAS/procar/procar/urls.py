from django.contrib import admin
from django.urls import path, include  # Add include
from aplikasi.views import home_view, about_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplikasi.urls')),  # Include the urls from the aplikasi app
    
    
]
    