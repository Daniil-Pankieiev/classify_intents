import requests
from config.settings import API_URL, AUTH_TOKEN

headers = {"Authorization": AUTH_TOKEN}

def query(payload):
    """Sends a POST request to the external model API with the provided payload."""
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()  # Raises an HTTPError if the response code was unsuccessful
    return response.json()
