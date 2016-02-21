from django.test import TestCase

from vewTrak.models import RelationalHits

class RelationalHitsMethodTests(TestCase):
	def test_ensure_views_are_positive(self):
		'''
		Should result in True if hits are zero or positive
		'''
		rds_hits = RelationalHits(hits=-1)
		rds_hits.save()
		self.assertEqual((rds_hits.hits >= 0), True)
