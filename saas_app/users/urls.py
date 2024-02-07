# -*- coding: utf-8 -*-

from django.urls import re_path, path, include

from . import views

app_name = "users"

urlpatterns = [
    # URL pattern for the UserUpdateView
    path("stripe/", include("djstripe.urls", namespace="djstripe")),
    re_path(r"^~update/$", view=views.UserUpdateView.as_view(), name="update"),
]
