from __future__ import unicode_literals
from django.db import models

class RelationalHits(models.Model):
	hits = models.IntegerField()

	# class Meta:
	# 	app_label = 'RelationalHits'

