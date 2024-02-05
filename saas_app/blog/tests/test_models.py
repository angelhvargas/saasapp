from test_plus.test import TestCase
from django.urls import reverse

from saas_app.blog.models import Entry


class EntryTestCase(TestCase):
    def test_str(self):
        entry = Entry.objects.create(title="foo")
        self.assertEqual(entry.__str__(), entry.title)

    def test_get_absolute_url(self):
        entry = Entry.objects.create(title="foo")
        entry.save()
        self.assertEqual(
            entry.get_absolute_url(), reverse("blog:entry", kwargs={"slug": entry.slug})
        )
