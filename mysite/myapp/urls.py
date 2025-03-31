from django.urls import path
from .views import *
app_name = 'myapp'
urlpatterns = [
    path('login', UserLoginView.as_view(), name = 'UserLoginView'),
    path('logout/', UserLogoutView.as_view(), name='UserLogoutView'),
    path('DashboardView/', DashboardView.as_view(), name='DashboardView'),
]