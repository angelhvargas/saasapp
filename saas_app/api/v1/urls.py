from rest_framework import routers
from django.urls import path, include
from graphene_django.views import GraphQLView
from saas_app.api.v1.views import CurrentUserView  # Assuming you have a UserViewSet

app_name = "api.v1"

# Initialize the router and register any viewsets
router = routers.DefaultRouter()
# Example: router.register(r'users', UserViewSet)  # Assuming you have a UserViewSet

urlpatterns = [
    # GraphQL endpoint
    path("graphql/", GraphQLView.as_view(graphiql=True), name='graphql'),
    
    # Include DRF router URLs
    path("", include(router.urls)),
    
    # REST API endpoint for current user
    path("user/", CurrentUserView.as_view(), name="current-user"),
    
    # DRF auth URLs
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
