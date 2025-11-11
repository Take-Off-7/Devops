import json
import wikipedia

def lambda_handler(event, context):
    """Wikipedia Summarizer"""
    entity = event.get("entity", "Amazon (company)")
    res = wikipedia.summary(entity, sentences=1)
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": res})
    }
