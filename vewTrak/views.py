#jenkins: https://blogs.aws.amazon.com/application-management/post/Tx34AXRMYLXG5OT/Building-Continuous-Deployment-on-AWS-with-AWS-CodePipeline-Jenkins-and-AWS-Elas
from django.shortcuts import render, render_to_response
from vewTrak.models import RelationalHits
from django.template import RequestContext
from helpers import rds_increase, dynamo_increase
from boto3.dynamodb.conditions import Key, Attr
from django.conf import settings
import boto3
import redis


def home(request):
	# for redis views
	r = redis.StrictRedis()
	cache_hit_count = r.get("num")
	# for psql views
	hit_object = RelationalHits.objects.get(id=1)
	rds_hit_count = hit_object.hits
	# for dynamo views
	DYNAMO_ENDPOINT = getattr(settings, "DYNAMO_ENDPOINT", None)
	dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url=DYNAMO_ENDPOINT)
	table = dynamodb.Table('DynamoHits')
	response = table.query(
		KeyConditionExpression=Key('id').eq(1)
	)
	for i in response['Items']:
		nosql_hit_count = i['hits']
	# pass data to template
	contextDict = {'rds_hit_count': rds_hit_count, 'cache_hit_count': cache_hit_count, 'nosql_hit_count': nosql_hit_count}
	return render_to_response('vewTrak/index.html', contextDict)

def cache_hits(request):
	context = RequestContext
	if request.method == 'GET':
		try:
			r = redis.StrictRedis()
			r.incr("num")
		except:
			pass
	return render_to_response('vewTrak/cache.html', {})

def rds_hits(request):
	context = RequestContext(request)
	if request.method == 'GET':
		try:
			rds_increase()
		except:
			pass
	return render_to_response('vewTrak/db.html', {})

def nosql_hits(request):
	context = RequestContext(request)
	if request.method == 'GET':
		try:
			dynamo_increase()
		except:
			pass
	return render_to_response('vewTrak/nosql.html', {})

