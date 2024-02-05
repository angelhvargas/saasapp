from django.urls import re_path

from saas_app.blog import views

app_name = "blog"

urlpatterns = [
    re_path(r"^$", views.EntryListView.as_view(), name="entries"),
    re_path(r"^(?P<slug>[-\w]+)/$", views.EntryView.as_view(), name="entry"),
]
