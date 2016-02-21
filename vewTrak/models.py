from __future__ import unicode_literals
from django.db import models

class RelationalHits(models.Model):
	hits = models.IntegerField()
	def save(self, *args, **kwargs):
		if self.hits < 0:
			self.hits = 0
		super(RelationalHits, self).save(*args, **kwargs)

