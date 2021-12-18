
import json

# import simplejson as json

import boto3

from boto3.dynamodb.conditions import Key, Attr



dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('basicinfo')

def lambda_handler(event, context):

    name = event['firstname']

    response = table.scan(
    FilterExpression = Attr('First name').eq(name)
    )
    response1 = table.scan(
    FilterExpression = Attr('last name').eq(name)
    )

    if len(response['Items']) == 0:
        if len(response1['Items']) == 0:
            return {
        'body': json.dumps('No data')
    }
        else:
          
            return {
               
        'body': json.dumps(response1['Items'])
    }
    else:
        
        return {
           
        'body': json.dumps(response['Items'])
    }
