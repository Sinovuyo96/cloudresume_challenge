import boto3

client = boto3.client('dynamodb')
def handler_name(event, context): 
response = client.put_item(
    TableName='string',
    Item={
        'string': {
            'S': 'string',
            'N': 'string',
            'SS': [
                'string',
            ]
        }
    },
