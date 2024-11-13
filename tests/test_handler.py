import base64
import json
from handler import lambda_handler

def test_lambda_handler_success(mocker):
    # Mock the event input and context
    mock_event = {
        "body": json.dumps({
            "phrase": "Test phrase",
            "intents": base64.b64encode(b"Intent,Description\nTestIntent,Test description").decode("utf-8")
        })
    }
    mock_context = {}

    # Call the handler
    response = lambda_handler(mock_event, mock_context)
    body = json.loads(response['body'])

    # Check if the response is successful
    assert response['statusCode'] == 200
    assert 'categories' in body

def test_lambda_handler_missing_body():
    # Test missing body
    response = lambda_handler({}, {})
    body = json.loads(response['body'])
    assert response['statusCode'] == 400
    assert 'error' in body
