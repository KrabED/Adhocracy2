from argparse import ArgumentParser

from django.core.management.base import BaseCommand

from apps.projects.insights import create_insights
from apps.projects.models import Project


class Command(BaseCommand):
    help = "Resets the insights and participation tables."

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument(
            "--project",
            help="project slug, resets data for this project only",
        )

    def handle(self, *args, **options):
        slug = options["project"]

        if slug:
            project = Project.objects.filter(slug=slug).first()
            if not project:
                known = sorted(Project.objects.values_list("slug", flat=True))
                print(f"unknown project slug: {slug=}, {known=}")
                return

            projects = [project]
        else:
            projects = Project.objects.all()

        if not projects:
            print("no projects found")
            return

        insights = create_insights(projects=projects)

        print(f"created insights: {len(projects)=}, {len(insights)=}")
