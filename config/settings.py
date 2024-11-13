from dotenv import load_dotenv
import os

# Load .env file if it exists
load_dotenv()

# Use environment variables if they are set, otherwise use .env values
API_URL = os.getenv('API_URL')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
