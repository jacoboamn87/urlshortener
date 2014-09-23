from django.db import models
from django.core.urlresolvers import reverse

from .basechanger import decimal2base_n, base_n2decimal


class Link(models.Model):
    url = models.URLField()

    @staticmethod
    def shorten(link):
        # get_or_create return a tuple like this: (obj, boolean)
        l, created = Link.objects.get_or_create(url=link.url)

        return str(decimal2base_n(l.pk))

    @staticmethod
    def expand(slug):
        link_id = int(base_n2decimal(slug))

        l = Link.objects.get(pk=link_id)

        return l.url

    def get_absolute_url(self):
        return reverse('shorturls:link_show', kwargs={'pk': self.id})

    def short_url(self):
        return reverse(
            'shorturls:redirect_short_url',
            kwargs={'short_url': Link.shorten(self)}
        )
