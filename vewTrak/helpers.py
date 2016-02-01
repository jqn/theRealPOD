import os
import django
import boto3
import decimal
from boto3.dynamodb.conditions import Key, Attr
from vewTrak.models import RelationalHits
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8080")
view_table = dynamodb.Table('DynamoHits')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'theRealPOD.settings')
django.setup()

def rds_increase():
	hit = RelationalHits.objects.get(id=1)
	hit.hits = hit.hits + 1
	hit.save()

def dynamo_increase():
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
