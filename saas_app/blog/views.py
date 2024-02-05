from django.views.generic import ListView, DetailView

from saas_app.blog.models import Entry


class EntryListView(ListView):

    model = Entry
    context_object_name = "entries"
    paginate_by = 5


class EntryView(DetailView):

    model = Entry
    slug_field = "slug"
    slug_url_kwarg = "slug"
