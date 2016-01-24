from django.shortcuts import render, render_to_response
from vewTrak.models import RelationalHits
from django.template import RequestContext
from helpers import rds_increase

def home(request):
	hit_object = RelationalHits.objects.get(id=1)
	hit_count = hit_object.hits
	contextDict = {'hit_count': hit_count}
	return render_to_response('vewTrak/index.html', contextDict)

def rds_hits(request):
	context = RequestContext(request)
	rds_increase()
	if request.method == 'GET':
		try:
			rds_increase()
		except:
			pass
	return render_to_response('vewTrak/index.html', {})

