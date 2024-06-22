from django.urls import path
from .views.Register import RegisterView
from .views.CustomLogout import CustomLogoutView
from .views.Login import LoginView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
]
