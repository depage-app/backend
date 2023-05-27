from fastapi import APIRouter
from core import models, helpers

router = APIRouter()


@router.get('/ping', tags=['Ping'])
async def ping():
    """ Ping pong """
    return 'Pong'


@router.get('/chains', response_model=models.ChainsListAPIResponse, tags=['Info'])
async def get_chains():
    """ Get list of supported chains """
    return {'data': helpers.get_supported_chains()}
