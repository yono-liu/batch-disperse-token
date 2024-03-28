from config import network_configs

def parse_target_address_file(file_path):
    with open(file_path, 'r') as file:
        # 初始化一个空列表来存储解析后的数据
        addresses = []
        # 逐行读取文件
        for line in file:
            # 将字典添加到列表中
            address = line.rstrip('\n')
            addresses.append(address)
        print(addresses)
        return addresses

def parse_target_address(target_addresses) -> list:
    # 将地址文本按换行符分割成列表
    addresses_list = target_addresses.strip().split('\r\n')
    
    # 移除列表中的空字符串（如果有的话）
    addresses_list = [address for address in addresses_list if address]
    
    return addresses_list
    
def parse_main_address_file(file_path):
    pk = []
    with open(file_path, 'r') as file:
        for line in file:
            # private_key = line.strip().split(',')
            address = line.rstrip('\n')
            pk.append(address)
    print(pk)
    return pk

def parse_network(network: str):
    # 根据网络名称获取配置
    config = network_configs.get(network.upper())
    if not config:
        return None, "Network not supported"

    # 获取 ABI, address, rpc
    abi = config["abi"]
    contract_address = config["contract_address"]
    rpc = config["rpc"]
    
    return abi, contract_address, rpc

if __name__ == '__main__':
    # 打印结果
    # for address in addresses_list:
    #     print(address)
    print("hello")
    abi, contract_address, rpc = parse_network("arbitrum")
    print(type(rpc))