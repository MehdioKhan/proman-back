from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('login',views.login)
router.register('logout',views.logout)
router.register('signup',views.UserSignUp.as_view())
