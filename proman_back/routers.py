from rest_framework import routers
from project import views as project_views
from project.task import views as task_views
from project.attachments import views as attachment_views
from note import views as note_views

router = routers.DefaultRouter()

router.register('tasks',task_views.TaskViewSet)
router.register('comment',task_views.CommentViewSet)
router.register('projects',project_views.ProjectViewSet)
router.register('memberships',project_views.MembershipViewSet)
router.register('task_statuses',project_views.TaskStatusViewSet)
router.register('attachments',attachment_views.AttachmentsViewSet)
router.register('notes',note_views.NoteViewSet)