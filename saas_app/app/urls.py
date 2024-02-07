# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.urls import re_path

from saas_app.app import views

app_name = "app"

urlpatterns = [
    re_path(r"^$", views.DashboardView.as_view(), name="dashboard"),
]
