import json

# Eth_Sepolia
sepolia_abi = json.loads('[{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseTokenSimple","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseToken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseEther","outputs":[],"payable":true,"stateMutability":"payable","type":"function"}]')
sepolia_contract_address = "0xD152f549545093347A162Dce210e7293f1452150"
sepolia_rpc = "https://public.stackup.sh/api/v1/node/ethereum-sepolia"

# Eth
eth_contract_address = "0xD152f549545093347A162Dce210e7293f1452150"
eth_abi = json.loads('[{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseTokenSimple","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseToken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseEther","outputs":[],"payable":true,"stateMutability":"payable","type":"function"}]')
eth_rpc = "https://eth-pokt.nodies.app"

# Bsc
bsc_contract_address = "0xD152f549545093347A162Dce210e7293f1452150"
bsc_abi = json.loads('[{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseTokenSimple","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseToken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseEther","outputs":[],"payable":true,"stateMutability":"payable","type":"function"}]')
bsc_rpc = "https://bsc-mainnet.public.blastapi.io"

# OP_BNB
opbnb_contract_address = "x"

# Base
base_contract_address = "0xD152f549545093347A162Dce210e7293f1452150"
base_abi = json.loads('[{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseTokenSimple","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseToken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseEther","outputs":[],"payable":true,"stateMutability":"payable","type":"function"}]')
base_rpc = "https://base.llamarpc.com"

# Polygon
polygon_contract_address = "0xD152f549545093347A162Dce210e7293f1452150"
polygon_abi = json.loads('[{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseTokenSimple","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseToken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseEther","outputs":[],"payable":true,"stateMutability":"payable","type":"function"}]')
polygon_rpc = "https://1rpc.io/matic"

# Optimism
op_contract_address = "0xD152f549545093347A162Dce210e7293f1452150"
op_abi = json.loads('[{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseTokenSimple","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseToken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseEther","outputs":[],"payable":true,"stateMutability":"payable","type":"function"}]')
op_rpc = "https://rpc.ankr.com/optimism"

# Arbitrum
arb_contract_address = "0xD152f549545093347A162Dce210e7293f1452150"
arb_abi = json.loads('[{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseTokenSimple","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseToken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseEther","outputs":[],"payable":true,"stateMutability":"payable","type":"function"}]')
arb_rpc = "https://arbitrum-one-rpc.publicnode.com"

# Avalance(C-Chain)
avax_contract_address = "0x46f18045a6Bdb15Ff14d8e48944C7ca5c9D01636"
avax_abi = json.loads('[{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseTokenSimple","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"token","type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseToken","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],"name":"disperseEther","outputs":[],"payable":true,"stateMutability":"payable","type":"function"}]')
avax_rpc = "https://avalanche.public-rpc.com"


network_configs = {
    "SEPOLIA": {
        "abi": sepolia_abi,
        "contract_address": sepolia_contract_address,
        "rpc": sepolia_rpc
    },
    
    "ETH": {
        "abi": eth_abi,
        "contract_address": eth_contract_address,
        "rpc": eth_rpc
    },
    
    "BASE": {
        "abi": base_abi,
        "contract_address": base_contract_address,
        "rpc": base_rpc
    },
    
    "POLYGON": {
        "abi": polygon_abi,
        "contract_address": polygon_contract_address,
        "rpc": polygon_rpc
    },
    
    "OPTIMISM": {
        "abi": op_abi,
        "contract_address": op_contract_address,
        "rpc": op_rpc
    },
    
    "ARBITRUM": {
        "abi": arb_abi,
        "contract_address": arb_contract_address,
        "rpc": arb_rpc
    },
    
    "AVALANCHE": {
        "abi": avax_abi,
        "contract_address": avax_contract_address,
        "rpc": avax_rpc
    },
    
    "CUSTOM": {
        "abi": sepolia_abi,
        "contract_address": '',
        "rpc": ''
    },
    
}