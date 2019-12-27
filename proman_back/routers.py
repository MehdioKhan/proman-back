from rest_framework import routers
from project import views as project_views
from project.task import views as task_views


router = routers.DefaultRouter()

router.register('tasks',task_views.TaskViewSet)
router.register('projects',project_views.ProjectViewSet)
router.register('memberships',project_views.MembershipViewSet)
router.register('task_statuses',project_views.TaskStatusViewSet)
