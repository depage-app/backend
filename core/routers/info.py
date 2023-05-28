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


@router.get('/metadata/{token_id}', tags=['Info'])
async def nft_metadata(token_id):
    """ Returning NFT metadata """
    return {
        'name': f'DePage NFT # {token_id}',
        'description': 'Visit us at https://depage.app',
        'image': 'ipfs://QmQAxNndsVGVC4crFJLUHcg9tkwodUbbGKVm2oahs2jMZU'
    }