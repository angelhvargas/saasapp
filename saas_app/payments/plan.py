from djstripe.models import Price
from decimal import Decimal
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from saas_app.payments.defaults import SAAS_SUBSCRIPTION_TYPE as DEFAULT_SAAS_SUBSCRIPTION_TYPE

def get_plans(free_plan=False):
    plans = []
    saas_plans = getattr(settings, "SAAS_PLANS", {})
    for plan in Price.objects.all():
        try:
            plans.append({"plan": plan, "meta": saas_plans[plan.id]})
        except KeyError as exc:
            raise ImproperlyConfigured(
                f"Your stripe plan with the id '{plan.id}' is not in SAAS_PLANS.\n\n"
                "Make sure to add SAAS_PLANS to config/settings/common.py and add the plan "
                f"'{plan.id}' as a key."
            ) from exc

    if getattr(settings, "SAAS_SUBSCRIPTION_TYPE", DEFAULT_SAAS_SUBSCRIPTION_TYPE) == "freemium" and free_plan:
        try:
            plans.append({"plan": FreePlan(), "meta": saas_plans["free"]})
        except KeyError as exc:
            raise ImproperlyConfigured(
                "Your SAAS_SUBSCRIPTION_TYPE is 'freemium', but there is no 'free' plan in "
                "SAAS_PLANS.\n\n"
                "Make sure to add SAAS_PLANS to config/settings/common.py and add the plan "
                "'free' as a key."
            ) from exc

    return sorted(plans, key=lambda p: p["plan"].unit_amount)

class FreePlan:
    def __init__(self):
        self.amount = Decimal("0")
        self.name = "Free"

    @property
    def stripe_id(self):
        return self.name.lower()
    
    @property
    def unit_amount(self):
        return self.unit_amount

class TrialPlan(FreePlan):
    def __init__(self):
        super().__init__()
        self.name = "Trial"
