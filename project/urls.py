from django.urls import path,include
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'project'

router = SimpleRouter()
router.register('project',views.ProjectViewSet)
router.register('task_status',views.TaskStatusViewSet)
router.register('membership',views.MembershipViewSet)


urlpatterns = [
    path('',include('project.task.urls',namespace='task')),
] + router.urls