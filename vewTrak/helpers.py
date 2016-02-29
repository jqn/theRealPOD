import os
import django
import boto3
import decimal
from boto3.dynamodb.conditions import Key, Attr
from vewTrak.models import RelationalHits
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'theRealPOD.settings')
django.setup()

def rds_increase():
	hit = RelationalHits.objects.get(id=1)
	hit.hits = hit.hits + 1
	hit.save()

def dynamo_increase():
	DYNAMO_ENDPOINT = getattr(settings, "DYNAMO_ENDPOINT", None)
	dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url=DYNAMO_ENDPOINT)
	view_table = dynamodb.Table('DynamoHits')
	response = view_table.update_item(
		Key={
			'id': 1
		},
		UpdateExpression="set hits = hits + :val",
		ExpressionAttributeValues={
			':val': decimal.Decimal(1)
		},
		ReturnValues="UPDATED_NEW"
	)

def dynamo_get_value():
	DYNAMO_ENDPOINT = getattr(settings, "DYNAMO_ENDPOINT", None)
	dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url=DYNAMO_ENDPOINT)
	table = dynamodb.Table('DynamoHits')
	response = table.query(
		KeyConditionExpression=Key('id').eq(1)
	)
	for i in response['Items']:
		nosql_hit_count = i['hits']
	return nosql_hit_count
