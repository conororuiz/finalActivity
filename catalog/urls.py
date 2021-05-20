from django.urls import path
from catalog import views


urlpatterns = [
    path('register', views.register_view, name='register'),
    path('home', views.home, name='home'),
    path('edit/<str:vi>/', views.edit_view, name='edit'),
    path('delete/<str:vi>/', views.delete_view, name='delete'),
]
