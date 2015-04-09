from django.db import models
from django.conf import settings


class TourStop(models.Model):
    """Stop Model"""
    title = models.CharField( max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
		return self.title
