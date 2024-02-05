# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.conf.urls import include, url
from django.urls import include, re_path

app_name = "api"

urlpatterns = [
    re_path(r"^v1/", include("saas_app.api.v1.urls", namespace="v1")),
]
