from test_plus.test import TestCase

from saas_app.beta.forms import InviteForm, RequestForm
from saas_app.beta.models import Request, Invite


class InviteTestCase(TestCase):
    def test_str(self):
        req = Request.objects.create(email="foo@bar.com")
        inv = Invite.objects.create(request=req)
        self.assertEqual(inv.__str__(), inv.code)


class RequestTestCase(TestCase):
    def test_str(self):
        req = Request.objects.create(email="foo@bar.com")
        self.assertEqual(req.__str__(), req.email)
