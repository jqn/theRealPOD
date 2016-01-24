from django.shortcuts import render, render_to_response
from vewTrak.models import RelationalHits
from django.template import RequestContext
from test_script import test_rds

def home(request):
	hit_object = RelationalHits.objects.get(id=1)
	hit_count = hit_object.hits
	contextDict = {'hit_count': hit_count}
	return render_to_response('vewTrak/index.html', contextDict)

def rds_hits(request):
	test_rds()		# testing to see if this will work on EB
	# context = RequestContext(request)
	# if request.method == 'GET':
	# 	try:
	# 		hit = RelationalHits.objects.get(id=1)
	# 		hit.hits = hit.hits + 1
	# 		hit.save()
	# 	except:
	# 		pass
	return render_to_response('vewTrak/index.html', {})

