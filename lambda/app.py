import json
import boto3
import os

dynamodb = boto3.resource("dynamodb")

table_name = os.environ.get("TABLE_NAME", "serverless-users")
table = dynamodb.Table(table_name)

def lambda_handler(event, context):

    response = table.scan()

    return {
        "statusCode": 200,
        "body": json.dumps(response["Items"])
    }
