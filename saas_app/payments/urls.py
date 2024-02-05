from djstripe import views as djstripe_views

from django.urls import path, include
from django.views.generic import RedirectView
from django.urls import reverse_lazy

from . import views

urlpatterns = [
    path(
        r"^subscriptions/$",
        djstripe_views.SubscriptionListView.as_view(),
        name="djstripe_stripe_subscription_list",
    ),
    path(
        r"^checkout/$",
        views.CheckoutView.as_view(),
        name="djstripe_stripe_subscription_create",
    ),
    path(
        r"^subscriptions/(?P<pk>\d+)/delete/$",
        djstripe_views.SubscriptionDeleteView.as_view(),
        name="djstripe_stripe_subscription_delete",
    ),
    path(
        r"^subscriptions/(?P<pk>\d+)/update/$",
        views.CustomSubscriptionUpdateView.as_view(),
        name="djstripe_stripe_subscription_update",
    ),
    path(
        r"^payment-methods/create/$",
        views.CustomPaymentMethodCreateView.as_view(),
        name="djstripe_stripe_payment_method_create",
    ),
    path(
        r"^payment-methods/(?P<pk>\d+)/update/$",
        djstripe_views.PaymentMethodUpdateView.as_view(),
        name="djstripe_stripe_payment_method_update",
    ),
    path(
        r"^webhook/$", djstripe_views.Webhook.as_view(), name="djstripe_stripe_webhook"
    ),
    path(
        r"^payment-methods/$",
        RedirectView.as_view(
            url=reverse_lazy("djstripe_stripe_subscription_list"), permanent=True
        ),
        name="djstripe_stripe_payment_method_list",
    ),
]
