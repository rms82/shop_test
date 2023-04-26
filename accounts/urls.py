from django.urls import path, include

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('checkcode/<str:token>/', views.CheckCodeView.as_view(), name='checkcode'),
    # path('login/', views.login_view, name='login')
]
