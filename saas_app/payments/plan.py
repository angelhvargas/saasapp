from djstripe.models import Price
from decimal import Decimal
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def get_plans(free_plan=False):
    plans = []
    saas_plans = getattr(settings, "SAAS_PLANS", {})

    for plan in Price.objects.all():
        plan_id = str(
            plan.id
        )  # Ensure the key is a string, as JSON keys are always strings
        if plan_id not in saas_plans:
            raise ImproperlyConfigured(
                f"Your stripe plan with the id '{plan_id}' is not in SAAS_PLANS.\n\n"
                "Make sure to add SAAS_PLANS to config/settings/common.py and add the plan "
                f"'{plan_id}' as a key."
            )
        plans.append({"plan": plan, "meta": saas_plans[plan_id]})

    if (
        getattr(settings, "SAAS_SUBSCRIPTION_TYPE", "default") == "freemium"
        and free_plan
    ):
        if "free" not in saas_plans:
            raise ImproperlyConfigured(
                "Your SAAS_SUBSCRIPTION_TYPE is 'freemium', but there is no 'free' plan in "
                "SAAS_PLANS.\n\n"
                "Make sure to add SAAS_PLANS to config/settings/common.py and add the plan "
                "'free' as a key."
            )
        plans.append({"plan": FreePlan(), "meta": saas_plans["free"]})

    return sorted(plans, key=lambda p: p["plan"].unit_amount)


class FreePlan:
    def __init__(self):
        self._unit_amount = Decimal("0")
        self.name = "Free"

    @property
    def stripe_id(self):
        return self.name.lower()

    @property
    def unit_amount(self):
        return self._unit_amount


class TrialPlan(FreePlan):
    def __init__(self):
        super().__init__()
        self.name = "Trial"
