from django.views.generic.detail import DetailView

from adhocracy4.projects.models import Project
from liqd_product.apps.partners.models import Partner

from . import models


class ProfileView(DetailView):
    model = models.User
    slug_field = 'username'

    @property
    def projects(self):
        return Project.objects.filter(follow__creator=self.object,
                                      follow__enabled=True)

    @property
    def partners(self):
        return Partner.objects.filter(
            organisation__project__follow__creator=self.object,
            organisation__project__follow__enabled=True
        ).distinct()
