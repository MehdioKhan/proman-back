from django.utils.translation import ugettext_lazy as _

ANON_PERMISSIONS = [
    ('view_project', _('View project')),
    ('view_milestones', _('View milestones')),
    ('view_epics', _('View epic')),
    ('view_us', _('View user stories')),
    ('view_tasks', _('View tasks')),
    ('view_issues', _('View issues')),
    ('view_wiki_pages', _('View wiki pages')),
    ('view_wiki_links', _('View wiki links')),
]

MEMBERS_PERMISSIONS = [
    ('view_project', _('View project')),
    # Task permissions
    ('view_tasks', _('View tasks')),
    ('add_task', _('Add task')),
    ('modify_task', _('Modify task')),
    ('comment_task', _('Comment task')),
    ('delete_task', _('Delete task')),
]

ADMINS_PERMISSIONS = [
    ('modify_project', _('Modify project')),
    ('delete_project', _('Delete project')),
    ('add_member', _('Add member')),
    ('remove_member', _('Remove member')),
    ('admin_project_values', _('Admin project values')),
    ('admin_roles', _('Admin roles')),
]