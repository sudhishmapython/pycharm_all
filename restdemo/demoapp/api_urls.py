from django.urls import path
from demoapp import views
from demoapp.views import UserViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [

    path("demo",views.index,name='index'),
    path("demo_view/<int:id>/",views.demo_details,name='demo'),

    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),

    path("genericadd/", views.EmployeeList.as_view()),
    path("genericview/<int:pk>/", views.EmployeeDetail.as_view()),

    ]

# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')
# urlpatterns = router.urls

