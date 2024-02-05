# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.urls import re_path
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.http import HttpResponse

from saas_app.views import PricingView


app_name = "saas_app"
urlpatterns = [
    re_path(r"^$", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    re_path(
        r"^health_check/$",
        lambda r: HttpResponse("ok"),
    ),
    re_path(
        r"^terms-and-conditions/$",
        TemplateView.as_view(template_name="pages/terms_and_conditions.html"),
        name="terms_and_conditions",
    ),
    re_path(
        r"^privacy-policy/$",
        TemplateView.as_view(template_name="pages/privacy_policy.html"),
        name="privacy_policy",
    ),
    re_path(r"^pricing/$", PricingView.as_view(), name="pricing"),
    re_path(
        r"^features/$",
        TemplateView.as_view(template_name="pages/features.html"),
        name="features",
    ),
    # Django Admin, use {% url 'admin:index' %}
    re_path(settings.ADMIN_URL, admin.site.urls),
    re_path(r"^api/", include("saas_app.api.urls", namespace="api")),
    re_path(r"^auth/", include("allauth.urls")),
    re_path(
        r"^blog/",
        include("saas_app.blog.urls", namespace="blog"),
    ),
    re_path(r"^tinymce/", include("tinymce.urls")),
    re_path(
        r"^app/",
        include("saas_app.app.urls", namespace="app"),
    ),
    re_path(r"^users/", include("saas_app.users.urls", namespace="users")),
    re_path("", include("saas_app.beta.urls", namespace="beta")),
    # re_path(r"^payments/", include("saas_app.payments.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        re_path(
            r"^400/$",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        re_path(
            r"^403/$",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        re_path(
            r"^404/$",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        re_path(r"^500/$", default_views.server_error),
    ]
