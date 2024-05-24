from django.urls import path
from .views import UserView


urlpatterns = [
    path('login/',UserView.createUser, name='login'),
    path('save/', UserView.createUser, name="save")
]
