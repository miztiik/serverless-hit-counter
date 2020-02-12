import json


def handler(event, context):
    print('request: {}'.format(json.dumps(event)))

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': f"Hello, Mystique! You have hit {event['path']}"
    }