from django.urls import path
from .views import UserView


urlpatterns = [
    #path('login/', UserView.login_user, name='login'),
    path('register/', UserView.register_user, name='register'),

]
