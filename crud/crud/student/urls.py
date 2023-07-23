from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<id>', views.delete, name="delete"),
    path('add/', views.add, name="add"),
    path('edit/<id>', views.edit, name="edit"),
]