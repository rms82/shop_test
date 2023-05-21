from django.urls import path

from .views import CustomAuthToken, LogoutApiView

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='api_login'),
    path('logout/', LogoutApiView.as_view(), name='api_logout'),
]

