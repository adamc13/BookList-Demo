from django.contrib import admin
from . import views
from django.urls import path

admin.autodiscover()

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_book, name='create_book'),
    path('update/', views.update_books, name='update_books'),
    path('delete/', views.delete_book, name='delete_book'),
    path('sort/', views.sort, name='sort'),
]
