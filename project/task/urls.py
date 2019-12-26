from rest_framework.routers import SimpleRouter
from .views import TaskViewSet

app_name = 'task'

router = SimpleRouter()
router.register('tasks',TaskViewSet)

urlpatterns = router.urls
