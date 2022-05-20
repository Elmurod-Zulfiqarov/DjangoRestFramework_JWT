from django.urls import path
from .views import RegisterAPIView, LoginAPIView, UserAPIView, UserAPIView, LogoutAPIView

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('user', UserAPIView.as_view(), name='users'),
    path('logout', LogoutAPIView.as_view(), name='logout')
]