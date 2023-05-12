from django .contrib import admin
from django.urls import path
from lists import views

urlpatterns = [
    path('',views.index.as_view(),name="home"),
    path('todo/<int:id>/view', views.view.as_view(), name='view'),
    path('todo/',views.add.as_view(),name="add"),
    path('todo/<int:id>/delete',views.delete.as_view(),name="delete"),
    path('todo/<int:id>/edit',views.edit.as_view(),name="edit"),
    # path('edit_it/<int:id>',views.edit_it.as_view(),name="edit_it")

    
]