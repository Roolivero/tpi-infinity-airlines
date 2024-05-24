from django.urls import path
from .views import UserView


urlpatterns = [
    path('register/',UserView.create_user, name='register'),
    path('login/', UserView.login_user, name='login'),
]
