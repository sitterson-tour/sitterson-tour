from django.db import models
import qrcode
from django.template.defaultfilters import slugify
from os.path import join, normpath
from tour.settings.base import SITE_ROOT


class Stop(models.Model):
    """Stop Model"""
    title = models.CharField( max_length=100)
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField( max_length=100)
    content = models.TextField(null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def url(self):
        url = 'http://tournamint.cs.unc.edu/stop/{self.slug}/'.format(self=self)
        return url

    def qrcode(self):
        url = self.url()
        img = qrcode.make(url)
        filename = normpath(join(SITE_ROOT, 'assets/qrcodes/{self.slug}.png'.format(self=self)))
        with open(filename, 'w') as f:
            img.save(f)

        qr_path = 'http://tournamint.cs.unc.edu/static/qrcodes/{self.slug}.png'.format(self=self)
        return qr_path

    def __unicode__(self):
		return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Stop, self).save(*args, **kwargs)
