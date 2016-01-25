from django.shortcuts import render, render_to_response
from vewTrak.models import RelationalHits
from django.template import RequestContext
from helpers import rds_increase
import redis

def home(request):
	r = redis.StrictRedis()
	cache_hit_count = r.get("num")
	hit_object = RelationalHits.objects.get(id=1)
	rds_hit_count = hit_object.hits
	contextDict = {'rds_hit_count': rds_hit_count, 'cache_hit_count': cache_hit_count}
	return render_to_response('vewTrak/index.html', contextDict)

def cache_hits(request):
	context = RequestContext
	r = redis.StrictRedis()
	r.incr("num")
	return render_to_response('vewTrak/cache.html', {})

def rds_hits(request):
	context = RequestContext(request)
	if request.method == 'GET':
		try:
			rds_increase()
		except:
			pass
	return render_to_response('vewTrak/db.html', {})

