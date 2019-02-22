from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from adhocracy4.dashboard import DashboardComponent
from adhocracy4.dashboard import ProjectFormComponent
from adhocracy4.dashboard import components

from . import forms
from . import views


class ParticipantsComponent(DashboardComponent):
    identifier = 'participants'
    weight = 30
    label = _('Participants')

    def is_effective(self, project):
        return not project.is_draft and project.is_private

    def get_base_url(self, project):
        return reverse('a4dashboard:dashboard-participants-edit', kwargs={
            'project_slug': project.slug
        })

    def get_urls(self):
        return [(
            r'^projects/(?P<project_slug>[-\w_]+)/participants/$',
            views.DashboardProjectParticipantsView.as_view(component=self),
            'dashboard-participants-edit'
        )]


class ModeratorsComponent(DashboardComponent):
    identifier = 'moderators'
    weight = 32
    label = _('Moderators')

    def is_effective(self, project):
        return True

    def get_base_url(self, project):
        return reverse('a4dashboard:dashboard-moderators-edit', kwargs={
            'project_slug': project.slug
        })

    def get_urls(self):
        return [(
            r'^projects/(?P<project_slug>[-\w_]+)/moderators/$',
            views.DashboardProjectModeratorsView.as_view(component=self),
            'dashboard-moderators-edit'
        )]


class TopicComponent(ProjectFormComponent):
    identifier = 'topics'
    weight = 33
    label = _('Topics')

    form_title = _('Edit topics')
    form_class = forms.TopicForm
    form_template_name = 'liqd_product_projects/project_topics.html'


components.register_project(ModeratorsComponent())
components.register_project(ParticipantsComponent())
components.register_project(TopicComponent())
