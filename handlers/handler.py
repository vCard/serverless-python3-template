import lib.hello
import json

def handler(event, context):
    payload = event.get("body")

    response = {
        "statusCode": 200,
        "body": json.dumps("hello " + payload.get("hello"))
    }

    return response