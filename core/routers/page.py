from fastapi import APIRouter

from core import helpers
from core import models

router = APIRouter()


@router.get('/page', response_model=models.PageAPIResponseModel, tags=['Pages'])
async def get_page(page_id: str):
    """ Get page configuration """
    page = await helpers.get_page(page_id)
    return page


@router.post('/page', response_model=models.PageAPIResponseModel, tags=['Pages'])
async def create_page(creator_address: str, smart_contract_address: str, chain: str):
    """ Initialize page """
    await helpers.get_abi(smart_contract_address, chain)
    page = await helpers.create_smart_contract_page(smart_contract_address, chain, creator_address)
    return page


@router.patch('/page', response_model=models.PageAPIResponseModel, tags=['Pages'])
async def update_page(body: models.UpdatePageRequestBody):
    """ Updating page configuration """
    await helpers.update_page(**body.dict())
    return body

