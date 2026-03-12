from django.urls import path
from restapp import views

urlpatterns = [
    path('cat',views.add_category,name='category'),
    path("cat_view/<int:id>/",views.demo_details,name='demo'),
    # path('cake',views.add_cake,name='cakes'),
    # path("cake_view/<int:id>/",views.cake_details,name='cakes_view'),
    ]