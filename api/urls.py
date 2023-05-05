from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.urls import path, include
from . import views

urlpatterns = [
    path('drf-auth/', include('rest_framework.urls')),
    path('get-restaurants/', views.getRestaurants, name='get-restaurants'),
    path('add-restaurants/', views.addRestaurants, name='create-restaurants'),
    path('update-restaurants/<str:pk>/', views.updateRestaurants, name='update-restaurants'),
    path('delete-restaurants/<str:pk>/', views.deleteRestaurants),
    path('get-menu/', views.getMenu, name='get-menu'),
    path('add-menu/', views.addMenu, name='add-menu'),
    path('update-menu/<str:pk>/', views.updateMenu),
    path('get-employee/', views.getEmployees, name='get-employee'),
    path('add-employee/', views.addEmployees, name='add-employee'),
    path('update-employee/<str:pk>/', views.updateEmployees),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
