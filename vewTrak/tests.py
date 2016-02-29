from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
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

# class HomeViewTests(TestCase):
# 	def test_home_view(self):
# 		rds_hits = RelationalHits(id=1)
# 		rds_hits.save()
# 		response = self.client.get('http://carpod.us-west-2.elasticbeanstalk.com')
# 		self.assertEqual(response.status_code, 200)
# 		self.assertTemplateUsed(response, 'vewTrak/index.html')

# class CacheViewTests(TestCase):
# 	def test_cache_view(self):
# 		response = self.client.get('/cache/')
# 		self.assertEqual(response.status_code, 200)
# 		self.assertTemplateUsed(response, 'vewTrak/cache.html')

# class RDSViewTests(TestCase):
# 	def test_rds_view(self):
# 		response = self.client.get('/db/')
# 		self.assertEqual(response.status_code, 200)
# 		self.assertTemplateUsed(response, 'vewTrak/db.html')

# class NoSQLViewTests(TestCase):
# 	def test_nosql_view(self):
# 		response = self.client.get('/dynamo/')
# 		self.assertEqual(response.status_code, 200)
# 		self.assertTemplateUsed(response, 'vewTrak/nosql.html')

