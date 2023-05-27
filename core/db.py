"""
Initializing connection with MongoDB
"""
import motor.motor_asyncio

from core.config import config
from core.config.logger import log

if config.MONGODB_CONNECTION_URI is not None:
    client = motor.motor_asyncio.AsyncIOMotorClient(config.MONGODB_CONNECTION_URI)
    db = client[config.MONGODB_DATABASE_NAME]
    log.info(f'MongoDB [{config.MONGODB_DATABASE_NAME}] initialized')
else:
    client, db = None, None
    log.warning(f'[service] MongoDB URI is not defined')