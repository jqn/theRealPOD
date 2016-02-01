import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
view_table = dynamodb.Table('DynamoHits')

response = view_table.update_item(
	Key={
		'id': 1
	},
	UpdateExpression="set hits = :h",
	ExpressionAttributeValues={
		':h': 1
	},
	ReturnValues="UPDATED_NEW"
)




# view_table.put_item(
# 	Item={
# 		'id': 1,
# 		'views': 1,
# 	}
# )