from rest_framework import permissions


class TaskPermission(permissions.BasePermission):

        def has_object_permission(self, request, view, obj):
            project = obj.project
            memberships = project.memberships.filter(user=request.user).first()
            perms = []
            if not memberships:
                return False
            else:
                perms = memberships.role.permissions
            if view.action == 'retrieve':
                return 'view_tasks' in perms
            elif view.action == 'create':
                return 'add_task' in perms
            elif view.action in ['update', 'partial_update']:
                return 'modify_task' in perms
            elif view.action == 'destroy':
                return 'delete_task' in perms
            else:
                return False

