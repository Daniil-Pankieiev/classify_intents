import json
import requests
from utils.api_client import query

def test_query_success(mocker):
    payload = {"inputs": {"source_sentence": "test", "sentences": ["example"]}}
    mock_response = mocker.patch('requests.post', return_value=mocker.Mock(
        status_code=200, json=lambda: [0.9]))

    result = query(payload)
    assert result == [0.9]

def test_query_failure(mocker):
    payload = {"inputs": {"source_sentence": "test", "sentences": ["example"]}}
    mocker.patch('requests.post', return_value=mocker.Mock(
        status_code=500, json=lambda: {"error": "API error"}))

    try:
        query(payload)
    except requests.HTTPError:
        assert True
