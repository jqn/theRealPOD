import boto3
import decimal
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8080")
view_table = dynamodb.Table('DynamoHits')

response = view_table.query(
	KeyConditionExpression=Key('id').eq(1)
)

for i in response['Items']:
	print i['hits']