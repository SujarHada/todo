from django .contrib import admin
from django.urls import path
from lists import views

urlpatterns = [
    path('' , views.God().index, name="index"),
    path('todo/', views.God().add , name="add"),
    path('todo/<int:id>/edit', views.God().edit , name="edit"),
    path('todo/<int:id>/delete', views.God().delete , name="delete"),
  
    # path('edit_it/<int:id>',views.edit_it.as_view(),name="edit_it")

    
]