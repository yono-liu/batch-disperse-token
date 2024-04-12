from web3 import Web3
import json
import config
from util import parse_main_address_file, parse_target_address_file, parse_network, parse_target_address

class disperse:
    def __init__(self, network, abi, contract_address, rpc, main_account_pk) -> None:
        self.network = network
        # 根据 network 选择出对应的 contract_address，abi，rpc
        self.abi, self.contract_address, self.rpc = abi, contract_address, rpc
        self.web3 = Web3(Web3.HTTPProvider(self.rpc))
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.abi)
        self.main_account = self.web3.eth.account.from_key(main_account_pk)
        self.main_account_pk = main_account_pk
        # self.target_address = target_address_list
        # self.values = [self.web3.to_wei(value, 'ether') for value in values]
    
    def disperse_eth_unique(self, target_address: list, target_values: list):
        target_values = [self.web3.to_wei(value, 'ether') for value in target_values]
        call_function = self.contract.functions.disperseEther(target_address, target_values).build_transaction(
            {'nonce': self.web3.eth.get_transaction_count(self.main_account.address),
            'from': self.main_account.address,
            'value': sum(target_values),
            'gasPrice': int(self.web3.eth.gas_price * 1.2),
            'chainId': self.web3.eth.chain_id,
            }
        )
        # call_function[]
        signed_tx_disperse = self.web3.eth.account.sign_transaction(call_function, self.main_account_pk)
        send_tx = self.web3.eth.send_raw_transaction(signed_tx_disperse.rawTransaction)
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(send_tx)
        print(tx_receipt)
        return tx_receipt


if __name__ == '__main__':
    # choose network
    # network_list = ['sepolia', 'base']
    # # 选择一个
    # choose_network = network_list[0]
    
    # if choose_network == 'sepolia':
    #     contract_address = config.sepolia_contract_address
    #     abi = config.sepolia_abi
    #     rpc = config.sepolia_rpc
    
    # web3 = Web3(Web3.HTTPProvider(rpc))
    # contract = web3.eth.contract(address=contract_address, abi=abi)
    
    # # 填写对应的address和主要地址私钥
    # main_account_pk_list = parse_main_address_file('./main_address.txt')
    # target_address_list = parse_target_address_file('./address.txt')
    
    # 输入对应的钱
    # value = web3.to_wei(0.001, 'ether')
    # values = [value, value, value, value, value]
    # for main_account_pk in main_account_pk_list:
    #     disperse_eth_unique(main_account_pk=main_account_pk, target_address_list=target_address_list, values=values)
    print(1)