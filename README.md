# Phrase Classification API on AWS

This project provides a Python API built using the Serverless framework to classify customer phrases based on intent
categories provided in a CSV file. The API uses embeddings to find the most relevant intents based on the input phrase.

## Overview

The API:

    Accepts a customer phrase and an intent database (CSV file) with columns Intent and Description.
    Returns the 0-3 most relevant intent categories based on the input phrase.
    Is optimized for efficient deployment using AWS Lambda.

## Features

    Phrase Classification: Matches a phrase with intent descriptions in a CSV to classify the intent.
    AWS Lambda Compatible: Uses Serverless framework for deployment.
    Environment Configuration: Loads sensitive data from environment variables or a .env file.

## Requirements

    Python 3.8+
    Node.js (for Serverless framework)
    Serverless framework (npm install -g serverless)
    AWS account with appropriate IAM permissions
    AWS CLI configured locally

# Setup Instructions

Clone the Repository:

```bash
    git clone https://github.com/Daniil-Pankieiev/classify_intents.git

```

```bash
    cd classify_intents

```

Configuration Environment Variables

The API configuration uses environment variables. Update these varialbes in serverless.yml:

API_URL: "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
AUTH_TOKEN: "Bearer hf_YOUR_TOKEN"

Install Python Dependencies:

```bash
pip install -r requirements.txt

```

Install Serverless (if not already installed):

```bash
npm install -g serverless
```

```bash
serverless plugin install -n serverless-python-requirements
```

```bash
serverless plugin install -n serverless-offline
```

Configure AWS CLI (if not configured):

```bash
aws configure

```

Running the API Locally

To test the API locally, use the Serverless invoke local command. This simulates Lambda locally with the provided event
data.

Start Serverless Offline:

```bash
    serverless offline

```

POST request should contain the test data with the phrase and base64-encoded CSV file:

    {
        "body": {
            "phrase": "Test phrase",
            "intents": "<base64 encoded CSV content>"
        }
    }

Deploying to AWS

Deploy: Deploy the API to AWS using Serverless with:

```bash
    serverless deploy

```

Remove Deployment: When finished, remove the deployment from AWS to avoid charges:

```bash
    serverless remove

```

Testing

```bash
  cp .env_example .env
```

Modify .env with the appropriate values for API_URL, AUTH_TOKEN, etc. for testing

Run Tests: Run all tests using pytest with:

```bash
    pytest tests/

```

    Environment Variables for Tests:
        The .env file is automatically loaded by pytest with python-dotenv.
        If you’re overriding environment variables in tests, use monkeypatch.

Additional Notes

Logging: AWS Lambda logging is set up in handler.py and utils. Logs are output to CloudWatch when deployed.
Cost Management: Make sure to remove the deployment from AWS when no longer in use to avoid unexpected charges.

Happy coding!
