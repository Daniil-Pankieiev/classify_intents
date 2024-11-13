# Phrase Classification API on AWS

This project provides a Python API built using the Serverless framework to classify customer phrases based on intent categories provided in a CSV file. The API uses embeddings to find the most relevant intents based on the input phrase.

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

git clone https://github.com/yourusername/phrase-classification-api.git
cd phrase-classification-api

Configuration Environment Variables

The API configuration uses environment variables. Update in [serverless.yml]
Variable	Description	Example Value
    API_URL: "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
    AUTH_TOKEN: "Bearer hf_YOUR_TOKEN"

Install Python Dependencies:

pip install -r requirements.txt

Install Serverless (if not already installed):

npm install -g serverless

Configure AWS CLI (if not configured):

aws configure


Running the API Locally

To test the API locally, use the Serverless invoke local command. This simulates Lambda locally with the provided event data.

    Start Serverless Offline:

    serverless offline

Invoke Lambda Locally:

serverless invoke local -f classify -p event.json

    event.json should contain the test data with the phrase and base64-encoded CSV file:

    {
        "body": {
            "phrase": "Test phrase",
            "intents": "<base64 encoded CSV content>"
        }
    }



Deploying to AWS

    Deploy: Deploy the API to AWS using Serverless with:

    serverless deploy


Remove Deployment: When finished, remove the deployment from AWS to avoid charges:

    serverless remove

Testing


Run Tests: Run all tests using pytest with:

    pytest tests/

    Environment Variables for Tests:
        The .env file is automatically loaded by pytest with python-dotenv.
        If you’re overriding environment variables in tests, use monkeypatch.



Project Structure
classify_intents/
├── handler.py               # Main Lambda handler code
├── config/
│   └── settings.py          # Loads environment variables
├── utils/
│   ├── classifier.py        # Classification logic and helper functions
│   ├── csv_parser.py        # Functions to parse CSV content
├── tests/
│   ├── test_handler.py      # Test suite for the lambda handler
│   ├── test_classifier.py   # Test suite for classifier utilities
├── requirements.txt         # Python dependencies for the project
├── requirements-test.txt    # Python dependencies for testing
├── serverless.yml           # Serverless configuration for deployment
├── .env_example             # Example environment file for setup
└── README.md                # Project documentation

Additional Notes

    Logging: AWS Lambda logging is set up in handler.py and utils. Logs are output to CloudWatch when deployed.
    Cost Management: Make sure to remove the deployment from AWS when no longer in use to avoid unexpected charges.

Happy coding!
