from django.db import models
from django.conf import settings


class Stop(models.Model):
	"""Stop Model"""
	title = models.CharField(_('title'), max_length=100)
