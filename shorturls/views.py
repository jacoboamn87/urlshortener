from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, RedirectView

from shorturls.models import Link


class LinkCreate(CreateView):
    model = Link
    fields = ["url"]
    success_url = 'shorturls:link_show'

    def form_valid(self, form):
        # Check if the Link object already exists
        prev = Link.objects.filter(url=form.instance.url)

        if prev:
            self.object = prev[0]

            return redirect(self.get_success_url())

        return super(LinkCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse(self.success_url, kwargs={'pk': self.object.id})


class LinkShow(DetailView):
    model = Link


class RedirectToLongURL(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        short_url = kwargs['short_url']
        return Link.expand(short_url)
