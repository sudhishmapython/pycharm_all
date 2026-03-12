from . import views
from django.urls import path

urlpatterns = [

    path('index1', views.index, name='index1'),
    path('view1', views.product_view, name='product_view'),
    path('student',views.student_view,name='student_view'),
    path('stud', views.stud, name='stud_view'),

    path('view',views.demo,name='demo_data'),

]
