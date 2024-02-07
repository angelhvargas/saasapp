from django.urls import path
from django.views.generic import RedirectView
from django.urls import reverse_lazy

from djstripe import views as djstripe_views

from . import views

urlpatterns = [
    path(
        "subscriptions/",
        djstripe_views.SubscriptionListView.as_view(),
        name="djstripe_subscription_list",
    ),
    path(
        "checkout/",
        views.CheckoutView.as_view(),
        name="djstripe_subscription_create",
    ),
    path(
        "subscriptions/<int:pk>/delete/",
        djstripe_views.SubscriptionDeleteView.as_view(),
        name="djstripe_subscription_delete",
    ),
    path(
        "subscriptions/<int:pk>/update/",
        views.CustomSubscriptionUpdateView.as_view(),
        name="djstripe_subscription_update",
    ),
    path(
        "payment-methods/create/",
        views.CustomPaymentMethodCreateView.as_view(),
        name="djstripe_payment_method_create",
    ),
    path(
        "payment-methods/<int:pk>/update/",
        djstripe_views.PaymentMethodUpdateView.as_view(),
        name="djstripe_payment_method_update",
    ),
    path(
        "webhook/",
        djstripe_views.ProcessWebhookView.as_view(),  # Make sure to use the correct view for processing webhooks
        name="djstripe_webhook",
    ),
    path(
        "payment-methods/",
        RedirectView.as_view(
            url=reverse_lazy("djstripe_subscription_list"), permanent=True
        ),
        name="djstripe_payment_method_list",
    ),
]
