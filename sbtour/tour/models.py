from django.db import models
from django.template.defaultfilters import slugify


class TourStop(models.Model):
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
        url = 'tour.cs.unc/stop/{self.slug}'.format(self=self)
        return url

    
    def __unicode__(self):
		return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(TourStop, self).save(*args, **kwargs)
