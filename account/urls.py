from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('login',views.login),
    path('logout',views.logout),
    path('signup',views.UserSignUp.as_view()),
]