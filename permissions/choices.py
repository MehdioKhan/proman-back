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
    ('add_project', _('Add project')),
    ('change_project',_('Modify project')),
    ('delete_project',_('Delete project')),
    # Task permissions
    ('view_task', _('View task')),
    ('add_task', _('Add task')),
    ('change_task', _('Modify task')),
    ('comment_task', _('Comment task')),
    ('delete_task', _('Delete task')),
]

ADMINS_PERMISSIONS = [
    ('change_project', _('Change project')),
    ('delete_project', _('Delete project')),
    ('add_member', _('Add member')),
    ('remove_member', _('Remove member')),
    ('admin_project_values', _('Admin project values')),
    ('admin_roles', _('Admin roles')),
]