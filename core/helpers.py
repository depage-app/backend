from bson import ObjectId
from typing import Optional

from core.db import db
from core import chains
from core.explorer import Explorer
from core.config.logger import log


async def get_abi(address: str, chain: str) -> list:
    """ Returns smart contract ABI by its address and chain """

    contract = await db.contracts.find_one({'address': address, 'chain': chain})
    if contract:
        return contract['abi']

    abi = Explorer(chain).get_abi(address)
    await db.contracts.insert_one({'address': address, 'chain': chain, 'abi': abi})

    return abi


async def create_smart_contract_page(address: str, chain: str, creator_wallet_address: str) -> Optional[dict]:
    """ Creating custom page for the smart contract with a unique id """

    contract = await db.contracts.find_one({'address': address, 'chain': chain})

    _page_config = reformat_abi_to_config(contract['abi'])
    page = await db.pages.insert_one(
        {'contract': contract['_id'],
         'creator': creator_wallet_address,
         'config': _page_config,
         'name': '',
         'description': ''}
    )

    return {'id': str(page.inserted_id), 'config': _page_config, 'name': '', 'description': ''}


async def update_page(page_id: str, config: list, name: str, description: str):
    """ Creating custom page for the smart contract with a unique id """
    await db.pages.update_one({'_id': ObjectId(page_id)},
                              {'$set': {'config': config,
                                        'name': name,
                                        'description': description}})


async def get_page(page_id: str) -> Optional[dict]:
    """ Returns page configuration by id """
    try:
        page = await db.pages.find_one({'_id': ObjectId(page_id)})
        return {'id': str(page['_id']), 'config': page['config']}
    except Exception as e:
        log.warning(f'Error in get_page: {e}')
        return None


def get_supported_chains() -> list:
    """ Returns list of supported chains """
    supported_chains = list()

    for chain in chains.chains.keys():
        supported_chains.append(
            {'id': chain,
             'name': chains.chains[chain]['name']}
        )

    return supported_chains


def reformat_abi_to_config(data: list) -> list:
    """ Filters out config (write functions) from ABI to separate dict """
    filtered = list()

    for obj in data:
        if obj.get('type') == 'function' and obj.get('stateMutability') in ('payable', 'nonpayable'):
            inputs = list()

            # Adding a field for payable amount
            if obj.get('stateMutability') == 'payable':
                inputs.append(
                    {'id': '$value',
                     'name': 'payable value',
                     'description': None,
                     'type': 'payable',
                     'hidden': False,

                     'value': None,
                     'multiply_by': None}
                )

            for _input in obj['inputs']:
                inputs.append(
                    {'id': _input['name'],
                     'name': _input['name'],
                     'description': None,
                     'type': _input['type'],
                     'hidden': False,

                     'value': None,
                     'multiply_by': None}
                )

            filtered.append(
                {'id': f'{obj["name"]}-{data.index(obj)}',
                 'name': obj["name"],
                 'description': None,
                 'inputs': inputs}
            )

    return filtered
