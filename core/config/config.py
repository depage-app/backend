"""
Configuration file with bot settings and API keys from third-party services
"""
import os
from dotenv import load_dotenv

# Loading env variables from .env file
load_dotenv('.env')

# Optional variables
MONGODB_CONNECTION_URI = os.getenv('MONGODB_CONNECTION_URI')  # URI for connecting to MongoDB
MONGODB_DATABASE_NAME = os.environ.get('MONGODB_DATABASE_NAME')  # DB name in MongoDB
