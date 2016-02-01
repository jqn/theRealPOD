import boto3
import decimal
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8080")
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



