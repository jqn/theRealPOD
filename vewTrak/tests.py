from django.test import TestCase
from django.core.urlresolvers import resolve
from vewTrak.models import RelationalHits
from vewTrak.views import home, cache_hits, rds_hits, nosql_hits

class RelationalHitsMethodTests(TestCase):
	def test_ensure_views_are_positive(self):
		'''
		Should result in True if hits are zero or positive
		'''
		rds_hits = RelationalHits(hits=-1)
		rds_hits.save()
		self.assertEqual((rds_hits.hits >= 0), True)

class HomeViewTests(TestCase):
	def test_home_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home)

class CacheViewTests(TestCase):
	def test_cache_view(self):
		found = resolve('/cache/')
		self.assertEqual(found.func, cache_hits)

class RDSViewTests(TestCase):
	def test_rds_view(self):
		found = resolve('/db/')
		self.assertEqual(found.func, rds_hits)

class NoSQLViewTests(TestCase):
	def test_nosql_view(self):
		found = resolve('/dynamo/')
		self.assertEqual(found.func, nosql_hits)








		
