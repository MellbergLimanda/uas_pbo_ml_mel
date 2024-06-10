from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordChangeView
from .views import mobil_list, edit_mobil

urlpatterns = [
    path('', views.home_view, name='home'),
    path('tambah-mobil/', views.tambah_mobil, name='tambah_mobil'),
    path('jenis-ajax/', views.jenis_ajax, name='jenis_ajax'),   
    path('mobil-list/', views.MobilListView.as_view(), name='mobil_list'),
    path('home', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-mobil/<int:pk>/', edit_mobil, name='edit_mobil'),
    path('delete-mobil/<int:id>/', views.delete_mobil, name='delete_mobil'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/changepassdone.html'), name='password_change_done'),
    

    
]
