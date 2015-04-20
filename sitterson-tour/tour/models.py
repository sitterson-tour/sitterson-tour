from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify


class TourStop(models.Model):
    """Stop Model"""
    title = models.CharField( max_length=100)
    slug = models.SlugField( max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    
    def __unicode__(self):
		return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(TourStop, self).save(*args, **kwargs)
