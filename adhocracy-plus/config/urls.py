"""adhocracy+ URL Configuration."""

from ckeditor_uploader import views as ck_views
from django.conf import settings
from django.conf.urls import i18n
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.views.decorators.cache import never_cache
from django.views.defaults import server_error
from django.views.generic import TemplateView
from django.views.i18n import JavaScriptCatalog
from rest_framework import routers
from wagtail.contrib.sitemaps import views as wagtail_sitemap_views
from wagtail.contrib.sitemaps.sitemap_generator import \
    Sitemap as WagtailSitemap
from wagtail.documents import urls as wagtaildocs_urls

from adhocracy4.api import routers as a4routers
from adhocracy4.comments.api import CommentViewSet
from adhocracy4.follows.api import FollowViewSet
from adhocracy4.ratings.api import RatingViewSet
from adhocracy4.reports.api import ReportViewSet
from apps.contrib import views as contrib_views
from apps.contrib.sitemaps.product_organisations_sitemap import \
    ProductOrganisationsSitemap
from apps.contrib.sitemaps.product_projects_sitemap import \
    ProductProjectsSitemap
from apps.contrib.sitemaps.static_sitemap import StaticSitemap
from apps.documents.api import DocumentViewSet
from apps.likes.api import LikesViewSet
from apps.likes.routers import LikesDefaultRouter
from apps.moderatorremark.api import ModeratorRemarkViewSet
from apps.polls.api import PollViewSet
from apps.polls.api import VoteViewSet
from apps.polls.routers import QuestionDefaultRouter
from apps.questions.api import QuestionViewSet
from apps.users.decorators import user_is_project_admin

router = routers.DefaultRouter()
router.register(r'follows', FollowViewSet, basename='follows')
router.register(r'reports', ReportViewSet, basename='reports')
router.register(r'polls', PollViewSet, basename='polls')

module_router = a4routers.ModuleDefaultRouter()
# FIXME: rename to 'chapters'
module_router.register(r'documents', DocumentViewSet, basename='chapters')
module_router.register(r'questions', QuestionViewSet, basename='questions')

likes_router = LikesDefaultRouter()
likes_router.register(r'likes', LikesViewSet, basename='likes')

orga_router = a4routers.OrganisationDefaultRouter()

ct_router = a4routers.ContentTypeDefaultRouter()
ct_router.register(r'comments', CommentViewSet, basename='comments')
ct_router.register(r'ratings', RatingViewSet, basename='ratings')
ct_router.register(r'moderatorremarks', ModeratorRemarkViewSet,
                   basename='moderatorremarks')

question_router = QuestionDefaultRouter()
question_router.register(r'vote', VoteViewSet, basename='vote')

sitemaps = {
    'organisations': ProductOrganisationsSitemap,
    'projects': ProductProjectsSitemap,
    'wagtail': WagtailSitemap,
    'static': StaticSitemap
}

urlpatterns = [
    # General platform urls
    re_path(r'^django-admin/', admin.site.urls),
    re_path(r'^admin/', include('wagtail.admin.urls')),
    re_path(r'^documents/', include(wagtaildocs_urls)),

    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^account/', include('apps.account.urls')),
    re_path(r'^embed/', include('apps.embed.urls')),
    re_path(r'^profile/', include('apps.users.urls')),
    re_path(r'^questions/', include('apps.questions.urls')),
    re_path(r'^i18n/', include(i18n)),

    # API urls
    re_path(r'^api/', include(ct_router.urls)),
    re_path(r'^api/', include(module_router.urls)),
    re_path(r'^api/', include(orga_router.urls)),
    re_path(r'^api/', include(question_router.urls)),
    re_path(r'^api/', include(likes_router.urls)),
    re_path(r'^api/', include(router.urls)),

    re_path(r'^upload/', user_is_project_admin(ck_views.upload),
            name='ckeditor_upload'),
    re_path(r'^browse/', never_cache(user_is_project_admin(ck_views.browse)),
            name='ckeditor_browse'),

    re_path(r'^components/$', contrib_views.ComponentLibraryView.as_view()),
    re_path(r'^jsi18n/$', JavaScriptCatalog.as_view(),
            name='javascript-catalog'),

    re_path(r'^(?P<organisation_slug>[-\w_]+)/', include([
        path('budgeting/',
             include(('apps.budgeting.urls', 'a4_candy_budgeting'),
                     namespace='a4_candy_budgeting')),
        path('dashboard/', include('apps.dashboard.urls')),
        path('ideas/', include(('apps.ideas.urls', 'a4_candy_ideas'),
                               namespace='a4_candy_ideas')),
        path('mapideas/', include(('apps.mapideas.urls', 'a4_candy_mapideas'),
                                  namespace='a4_candy_mapideas')),
        path('offlineevents/',
             include(('apps.offlineevents.urls', 'a4_candy_offlineevents'),
                     namespace='a4_candy_offlineevents')),
        path('projects/', include('apps.projects.urls')),
        path('text/', include(('apps.documents.urls', 'a4_candy_documents'),
                              namespace='a4_candy_documents')),
        path('topicprio/',
             include(('apps.topicprio.urls', 'a4_candy_topicprio'),
                     namespace='a4_candy_topicprio')),
        path('subjects/',
             include(('apps.debate.urls', 'a4_candy_debate'),
                     namespace='a4_candy_debate')),
    ])),

    path('sitemap.xml', wagtail_sitemap_views.index,
         {'sitemaps': sitemaps, 'sitemap_url_name': 'sitemaps'}),
    re_path(r'^sitemap-(?P<section>.+)\.xml$', wagtail_sitemap_views.sitemap,
            {'sitemaps': sitemaps}, name='sitemaps'),
    path('robots.txt',
         TemplateView.as_view(template_name='robots.txt',
                              content_type="text/plain"), name="robots_file"),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += [
        path('403/', TemplateView.as_view(template_name='403.html')),
        path('404/', TemplateView.as_view(template_name='404.html')),
        path('500/', server_error),
    ]

    # Serve static and media locally
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    try:
        import debug_toolbar
    except ImportError:
        pass
    else:
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns


# generic patterns at the very end
urlpatterns += [
    re_path(r'', include('apps.organisations.urls')),
    re_path(r'', include('wagtail.core.urls')),
]
