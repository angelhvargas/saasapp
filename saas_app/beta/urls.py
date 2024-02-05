from django.urls import re_path
from . import views

app_name = "beta"

urlpatterns = [
    re_path(
        r"^request-invite/$",
        views.RequestInviteView.as_view(),
        name="request-invite",
    ),
    re_path(
        r"^request-success/$",
        views.RequestInviteSuccess.as_view(),
        name="request-success",
    ),
]
