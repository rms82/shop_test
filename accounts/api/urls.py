from django.urls import path

from .views import CustomAuthToken, LogoutApiView, RegisterApiView

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='api_login'),
    path('logout/', LogoutApiView.as_view(), name='api_logout'),
    path('register/', RegisterApiView.as_view(), name='api_register'),
]

