import os

chains = {
    'ethereum': {
        'name': 'Ethereum',
        'rpc_url': 'https://eth.llamarpc.com',
        'abi_api_request_url': 'https://api.etherscan.io/api?module=contract&action=getabi&address=',
        'api_key': os.environ.get('ETHERSCAN_API_KEY'),
        'chain_id': 1,
        'disabled': False
    },
    
    'bsc': {
        'name': 'Binance Smart Chain',
        'rpc_url': '',
        'abi_api_request_url': 'https://api.bscscan.com/api?module=contract&action=getabi&address=',
        'api_key': os.environ.get('BSCSCAN_API_KEY'),
        'chain_id': 56,
        'disabled': False
    },

    'polygon': {
        'name': 'Polygon',
        'rpc_url': 'https://polygon.llamarpc.com',
        'abi_api_request_url': 'https://api.polygonscan.com/api?module=contract&action=getabi&address=',
        'api_key': os.environ.get('POLYGONSCAN_API_KEY'),
        'chain_id': 137,
        'disabled': False
    },

    'mantle-testnet': {
        'name': 'Mantle Testnet',
        'rpc_url': 'https://rpc.testnet.mantle.xyz',
        'abi_api_request_url': 'https://explorer.testnet.mantle.xyz/api?module=contract&action=getabi&address=',
        'api_key': None,
        'chain_id': 5001,
        'disabled': False
    }
}
