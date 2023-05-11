from django .contrib import admin
from django.urls import path
from lists import views

urlpatterns = [
    path('',views.index,name="home"),
    path('add',views.add,name="add"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('edit_it/<int:id>',views.edit_it,name="edit_it")

    
]