# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import employViewSet

# router = DefaultRouter()

# router.register(
#     r'employ',
#     employViewSet,
#     basename='employ'
# )

# urlpatterns = [
#     path('', include(router.urls)),
# ]




from django.urls import path
from . import views

urlpatterns = [
    path('', views.employ_list, name='employ_list'),

    path('register/', views.register_view, name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

    path('add/', views.employ_add, name='employ_add'),
    path('edit/<int:pk>/', views.employ_edit, name='employ_edit'), #primary key pk
    path('delete/<int:pk>/', views.employ_delete, name='employ_delete'),
]