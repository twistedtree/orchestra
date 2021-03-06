from django.conf.urls import url

from orchestra.interface_api.project_management import views

urlpatterns = [
    url(r'^projects/$',
        views.ProjectList.as_view(),
        name='projects'),

    url(r'^assign_task/$',
        views.assign_task_api,
        name='assign_task'),

    url(r'^complete_and_skip_task/$',
        views.complete_and_skip_task_api,
        name='complete_and_skip_task'),

    url(r'^create_subsequent_tasks/$',
        views.create_subsequent_tasks_api,
        name='create_subsequent_tasks'),

    url(r'^edit_slack_membership/$',
        views.edit_slack_membership_api,
        name='edit_slack_membership'),

    url(r'^end_project/$',
        views.end_project_api,
        name='end_project'),

    url(r'^project_information/$',
        views.project_information_api,
        name='project_information'),

    url(r'^reassign_assignment/$',
        views.reassign_assignment_api,
        name='reassign_assignment'),

    url(r'^revert_task/$',
        views.revert_task_api,
        name='revert_task'),
]
