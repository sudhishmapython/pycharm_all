from django.urls import path

from TodoApp import views

urlpatterns = [
       path('',views.stud_add,name='stud_add'),
       path('update/<int:id>',views.Student_update,name='stud_update'),
       path('dele/<int:id>',views.Student_delete,name='stud_delete'),




]