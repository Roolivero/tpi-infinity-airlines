from django.urls import path
from .views import UserViews


urlpatterns = [
    #path('login/', UserView.login_user, name='login'),
    path('register/', UserViews.register, name='register'),
    path('login/', UserViews.login_view, name="login"),
    path('logout/', UserViews.logout_view, name="logout"),

]
