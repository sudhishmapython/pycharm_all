from staticapp import views
from django.urls import path



urlpatterns = [
    path('', views.index,name='index'),
    path('cust_reg/', views.cust_reg,name='cust_reg'),
    path('login/', views.login_view,name='login'),
    path('admin_page/',views.admin_page,name='admin_page'),
    path('customer_page/',views.customer_page,name='customer_page'),
    path('physician_page/',views.physician_page,name='physician_page'),
    path('logout/', views.logout_view, name='logout'),
    path('physician_reg',views.physician_reg,name='physician_reg'),


]

