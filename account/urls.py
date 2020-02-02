from django.urls import path,include
from . import views
from .routers import router


app_name = 'account'

urlpatterns = [
    path('api/v1/',include(router.urls)),
]