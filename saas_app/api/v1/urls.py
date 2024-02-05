from rest_framework import routers
from django.urls import path, re_path, include

from graphene_django.views import GraphQLView
from saas_app.api.v1 import views

app_name = "api.v1"
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"user", views.CurrentUserView, basename="api.v1")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("graphql", GraphQLView.as_view(graphiql=True)),
    re_path(r"^", include(router.urls)),
    re_path(r"user/", views.CurrentUserView, name="user"),
    re_path(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
