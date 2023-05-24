from django.urls import path

from home.views import HomePage, change_view

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('change/', change_view, name='change'),

]
