from django.urls import path
from first_app import views


urlpatterns = [
    path('',views.index, name='index'),
    path('add',views.add,name='add'),
    path('view',views.product_view,name='view'),
    path('edit/<int:id>', views.product_edit, name='edit'),
    path('product_delete/<int:id>', views.product_delete, name='product_delete'),





    path('img_add',views.demo, name='demo'),
    path('img_view',views.student_view, name='student_view'),
    path('img_update/<int:up>',views.student_update, name='student_update'),
    path('img_delete/<int:dl>',views.student_delete,name='student_delete'),

    path('upload', views.fileupload, name = "File_Uploads"),
    path('upload_view',views.upload_view, name='upload_view'),

]
