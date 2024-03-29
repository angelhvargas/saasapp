from djstripe.models import Customer, Subscription, Card, Plan

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils.timezone import now
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail

from saas_app.payments.plan import FreePlan, TrialPlan
from saas_app.payments.defaults import (
    SAAS_SUBSCRIPTION_TYPE as DEFAULT_SAAS_SUBSCRIPTION_TYPE,
    SAAS_TRIAL_LENGTH as DEFAULT_SAAS_TRIAL_LENGTH,
)


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(_("Full Name"), blank=True, max_length=255)
    email = models.EmailField(_("email address"), unique=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["id"]

    @property
    def is_on_trial_plan(self):
        return isinstance(self.plan, TrialPlan)

    @property
    def is_on_free_plan(self):
        return isinstance(self.plan, FreePlan)

    @property
    def is_on_paid_plan(self):
        return isinstance(self.plan, Plan)
        return False

    @property
    def is_customer(self):
        return Customer.objects.filter(id=self.id).exists()

    @property
    def trial_ends(self):
        return self.date_joined + getattr(
            settings, "SAAS_TRIAL_LENGTH", DEFAULT_SAAS_TRIAL_LENGTH
        )

    @property
    def is_trial_active(self):
        return now() < self.trial_ends

    @property
    def plan(self):
        if self.subscription:
            plan = self.subscription.plan
        else:
            sub_type = getattr(
                settings, "SAAS_SUBSCRIPTION_TYPE", DEFAULT_SAAS_SUBSCRIPTION_TYPE
            )
            if sub_type == "freemium":
                plan = FreePlan()
            elif sub_type == "trial" and self.is_trial_active:
                plan = TrialPlan()
            else:
                plan = None

    @property
    def plan_meta(self):
        return settings.SAAS_PLANS[self.plan.stripe_id]

    @property
    def card(self):
        try:
            return self.customer.card_set.last()
        except (Customer.DoesNotExist, Card.DoesNotExist):
            return None
        return None

    @property
    def invoices(self):
        try:
            return self.customer.invoices.all()
        except Customer.DoesNotExist:
            return []
        return []

    @property
    def subscription(self):
        try:
            return self.customer.subscription_set.first()
        except (Subscription.DoesNotExist, Customer.DoesNotExist):
            return None
        return None
