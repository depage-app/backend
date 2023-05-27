import json
import requests

from core.chains import chains


class Explorer:
    def __init__(self, chain: str):
        self.chain: str = chain

    def get_abi(self, address: str):
        api_key = ''
        if apikey := chains[self.chain]['api_key']:
            api_key = f'&apikey={apikey}'

        response = requests.get(chains[self.chain]['abi_api_request_url'] + address + api_key)
        data = response.json()
        return json.loads(data['result'])
