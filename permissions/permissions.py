from rest_framework import permissions


class TaskPermission(permissions.BasePermission):

        def has_object_permission(self, request, view, obj):
            project = obj.project
            memberships = project.memberships.filter(user=request.user).first()
            perms = []
            if not memberships:
                return False
            else:
                if memberships.is_admin:
                    return True
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


class CommentPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        project = obj.task.project
        memberships = project.memberships.filter(user=request.user).first()

        perms = []
        if not memberships:
            return False
        else:
            if memberships.is_admin:
                return True
            perms = memberships.role.permissions
        if view.action == 'create':
            return False
        if view.action != 'retrieve':
            return 'comment_task' in perms
        else:
            return False


class ProjectAdminPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        memberships = obj.memberships.filter(user=request.user).first()
        perms = []
        if not memberships:
            return False
        else:
            if memberships.is_admin:
                return True
            perms = memberships.role.permissions

        if view.action in ['update', 'partial_update']:
            return 'change_project' in perms
        elif view.action == 'destroy':
            return 'delete_project' in perms
        else:
            return False


class ProjectMembershipPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        project = obj.project
        memberships = project.memberships.filter(user=request.user).first()

        perms = []
        if not memberships:
            return False
        else:
            if memberships.is_admin:
                return True
            perms = memberships.role.permissions

        if view.action in ['create','update', 'partial_update']:
            return 'add_member' in perms
        elif view.action == 'destroy':
            return 'remove_project' in perms
        else:
            return False
